import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import DistanceStrategy
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

# ── Config ─────────────────────────────────────────────────────────────────────
load_dotenv()

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ── Cached resources (only load once) ─────────────────────────────────────────
@st.cache_resource
def load_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=1024,
        timeout=30,
        max_retries=2
    )

@st.cache_resource
def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        encode_kwargs={"normalize_embeddings": True}
    )

@st.cache_resource
def load_rag_chain():
    embedding = load_embedding_model()
    llm = load_llm()

    vectorstore = FAISS.load_local(
        folder_path="../vector_databases/vector_db_chatbot",
        embeddings=embedding,
        allow_dangerous_deserialization=True,
        distance_strategy=DistanceStrategy.COSINE
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 6, "fetch_k": 20}
    )

    system_prompt = """Du bist ein präziser Assistent, der Fragen ausschließlich auf Basis der bereitgestellten Dokumente beantwortet.

Regeln:
- Antworte immer auf Deutsch
- Beziehe dich konkret auf den bereitgestellten Kontext
- Wenn die Antwort nicht im Kontext enthalten ist, antworte exakt:
  "Diese Information ist in den bereitgestellten Dokumenten nicht enthalten."
- Nenne am Ende deiner Antwort die verwendete Quelldatei, sofern vorhanden

Kontext:
{context}
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    stuff_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    rag_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=stuff_chain)
    return rag_chain


# ── UI ─────────────────────────────────────────────────────────────────────────
st.title("🤖 RAG Chatbot")
st.caption("Fragen an deine Dokumente stellen")

# Chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Stelle eine Frage..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Suche in Dokumenten..."):
            try:
                chain = load_rag_chain()
                result = chain.invoke({"input": user_input})
                answer = result["answer"]

                # Show source documents in expander
                source_docs = result.get("context", [])
                st.markdown(answer)

                if source_docs:
                    with st.expander("📄 Verwendete Quellen"):
                        for i, doc in enumerate(source_docs):
                            source = doc.metadata.get("source_file", "unbekannt")
                            st.markdown(f"**Quelle {i+1}:** `{source}`")
                            st.markdown(doc.page_content[:300] + "...")
                            st.divider()

            except Exception as e:
                answer = f"⚠️ Fehler: {e}"
                st.error(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# Sidebar
with st.sidebar:
    st.header("⚙️ Einstellungen")
    st.markdown("**Modell:** `llama-3.1-8b-instant`")
    st.markdown("**Embedding:** `all-mpnet-base-v2`")
    st.markdown("**Suche:** MMR (k=6)")
    st.divider()
    if st.button("🗑️ Chat zurücksetzen"):
        st.session_state.messages = []
        st.rerun()
