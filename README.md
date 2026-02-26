# RAG-Chatbot – From Scratch

**Projektarbeit | KI-Modellierung Bootcamp**

---

| | |
|---|---|
| **Zeitrahmen** | 1 Tag (ca. 6–8 Stunden) |
| **Arbeitsform** | 3-4 Teilnehmende pro Gruppe |
| **Output** | Jupyter Notebook + kurze Reflexionen| **Voraussetzung** | Abgeschlossenes RAG-Exercise-Notebook |

---

## Aufgabenstellung

Ihr baut einen vollständigen RAG-Chatbot von Grund auf – ohne vorgegebene Funktionsstruktur. Ihr wählt euer eigenes Dokument, trefft eigene technische Entscheidungen und dokumentiert eure Überlegungen. Das Ziel ist nicht Perfektion, sondern ein funktionierendes System, das ihr selbst versteht und erklären könnt.

### Euer Ausgangsdokument

Wählt ein PDF-Dokument, das euch interessiert. Es sollte:

- mindestens 5–10 Seiten lang sein
- inhaltlich sinnvoll für ein Frage-Antwort-System sein (z.B. ein Handbuch, ein wissenschaftlicher Artikel, ein Report)
- auf Deutsch oder Englisch verfasst sein

Beispiele: Bedienungsanleitung, Wikipedia-Artikel als PDF, Forschungsbericht, Firmen-FAQ, Kochbuch.

---

## Was zu bauen ist

Euer Chatbot muss die folgenden Kernkomponenten enthalten:

| # | Komponente | Beschreibung |
|---|---|---|
| 1 | **Datenaufnahme** | PDF laden und Rohinhalt extrahieren |
| 2 | **Chunking** | Dokument in sinnvolle Textblöcke aufteilen |
| 3 | **Embeddings** | Chunks in Vektoren umwandeln und speichern |
| 4 | **Retrieval** | Relevante Chunks zu einer Frage abrufen |
| 5 | **LLM-Integration** | Antwort auf Basis der abgerufenen Chunks generieren |
| 6 | **Chatfunktion** | Einfache interaktive Abfrageschleife |

---

## Eure technischen Entscheidungen

Anders als in den vorigen Notebooks gibt es hier keine vorgegebene Struktur. Ihr entscheidet selbst:

- Welche Chunk-Größe und Überlappung macht für euer Dokument Sinn?
- Welches Embedding-Modell wählt ihr und warum?
- Wie viele Chunks ruft ihr pro Anfrage ab (`k`)?
- Wie formuliert ihr den Prompt an das LLM?
- Wie strukturiert ihr euren Code – Funktionen, Klassen, oder linear?

Jede Entscheidung ist eine Markdown-Zelle im Notebook wert. Schreibt kurz auf, was ihr gemacht habt und warum.

---

## Jupyter Notebook

Euer Notebook soll:

- vollständig ausgeführt sein (alle Outputs sichtbar)
- saubere Markdown-Erklärungen zwischen den Code-Zellen enthalten
- mindestens 5 Testfragen mit den jeweiligen Antworten des Chatbots zeigen
- keine sensiblen Daten oder API-Keys enthalten

## Reflexionen

Beantwortet kurz folgende Fragen (im Notebook oder euren Notizen):

- Was hat gut funktioniert?
- Wo habt ihr Probleme gehabt – und wie habt ihr sie gelöst?
- Welche Komponente war für euch die wichtigste Lerneinheit?
- Was würdet ihr verbessern, wenn ihr mehr Zeit hättet?



## Praktische Hinweise

- Fängt mit einem kleinen, einfachen PDF an. Ihr könnt es später gegen ein komplexeres austauschen.
- Wenn das Retrieval nicht funktioniert, liegt es meistens an Chunk-Größe oder `k` – experimentiert damit.
- Benutzt das Exercise-Notebook als Referenz

---

*Ein Chatbot, den ihr selbst gebaut und verstanden habt, ist wertvoller als ein perfekter, den jemand anderes geschrieben hat.*
