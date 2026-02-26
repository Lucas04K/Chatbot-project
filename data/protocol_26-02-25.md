# Tag 28, 25.02.2026

## Protokoll — LLM-Halluzinationen und Retrieval Augmented Generation (RAG)

---

### 1. Fallbeispiel: Halluzinationen im juristischen Kontext (2023)

Im Jahr 2023 reichte ein New Yorker Anwalt einen Schriftsatz mit zahlreichen angeblichen Präzedenzfällen bei Gericht ein. Präzedenzfälle sind im US-Rechtssystem üblich und stellen eine zentrale Argumentationsgrundlage dar.

Bei der gerichtlichen Prüfung fiel auf, dass die angeführten Fälle ungewöhnlich gut zur Argumentation passten. Obwohl die Angaben formal korrekt wirkten (z. B. Datums- und Zitiermuster), stellte sich heraus:

* **Keiner der Fälle existierte tatsächlich.**
* Die Fälle wurden von **ChatGPT** generiert.
* Das System erzeugte realistisch wirkende, jedoch vollständig erfundene Referenzen (Halluzinationen).

Die Verteidigung begründete den Fehler mit mangelndem Verständnis der Funktionsweise großer Sprachmodelle (LLMs). Das Gericht verhängte eine hohe Strafe, da der Anwalt die Inhalte ungeprüft übernommen hatte.

**Zentrale Erkenntnisse:**

* LLMs greifen nicht aktiv auf reale Datenbanken zu.
* Sie besitzen primär **probabilistisches und syntaktisches Wissen**.
* Es fehlt ein direkter Bezug zur Realität oder zu verifizierten Faktenquellen.

---

### 2. Grundlegende Eigenschaften und Probleme von LLMs

**Funktionsprinzip (historisch):**

* Vorhersage des wahrscheinlich nächsten Tokens/Wortes.
* Stilistische Korrektheit und überzeugende Darstellung, auch ohne faktische Grundlage.

**Typische Probleme:**

* **Halluzinationen:** Modelle beantworten Fragen auch bei fehlender Information.
* **Überzeugende Formulierungen:** Fehler werden schwer erkannt.
* **Begrenzte Aktualität:** Training erfolgt auf statischen Datensätzen.
* **Domänenspezifische Wissenslücken:** Allgemeines Wissen vorhanden, spezifische Detailinformationen fehlen.
* **Schwächen beim Erinnern exakter Zahlen oder zuvor genannter Details.**

---

### 3. Umgang mit fehlender Aktualität

#### 3.1 Finetuning

**Vorteile:**

* Integration neuer Informationen in das Modellwissen.

**Nachteile:**

* Zugriff auf Modell erforderlich
* Hoher Zeit- und Kostenaufwand
* Hoher Expertenbedarf
* Kontinuierliche Veralterung der Daten

Praxisbeispiel: Ständige Gesetzesänderungen machen wiederholtes Finetuning unpraktikabel.

---

### 4. Retrieval Augmented Generation (RAG)

RAG ist eine Architektur zur Kombination von Sprachmodellen mit externen Wissensquellen.

**Grundidee:**
Ein LLM wird an eine **Source of Truth** angebunden und nutzt Dokumente als Kontext für Antworten.

**Analogie:**
Ein Student versucht, alles auswendig zu wissen vs. ein Student, der in einer Prüfung ein Buch zur Recherche nutzt.

---

### 5. RAG-Architektur

**Ablauf:**
0. Relevante Dokumente werden verarbeitet, in Chunks zerlegt und in eine Datenbank eingespielt.
1. Nutzeranfrage wird gestellt.
2. Anfrage wird zusätzlich an einen Dokumentenspeicher weitergeleitet.
3. Möglichst passende Texte werden entnommen und als Kontext zur Anfrage bereitgestellt.
4. Das LLM generiert auf Basis dieses Kontexts die Antwort.

---

### 6. Zentrale Komponenten

#### 6.1 Dokumentenspeicher

* Vektor-Datenbanken (besonders geeignet)
* Alternativ klassische SQL-Datenbanken

#### 6.2 Dokumenten-Retriever

* Auswahl relevanter Dokumente mittels:

  * Vektorähnlichkeit
  * Stichwortsuche
  * hybriden Verfahren

#### 6.3 Prompt & Modellgenerierung

* Kontext + Prompt werden kombiniert
* LLM generiert die Antwort

---

### 7. Vektor-Datenbanken und Embeddings

**Funktionsweise:**

* Texte werden tokenisiert und als Vektoren repräsentiert.
* Semantisch ähnliche Begriffe liegen im Vektorraum nahe beieinander.
* Suche erfolgt über Ähnlichkeitsmessungen.

**Beispiel:**
Eine Suche nach „Urlaub Kanaren“ kann auch Begriffe wie *Freizeit*, *Flüge* oder *Vacation* berücksichtigen.

---

### 8. Pipeline: Ingestion Stage vs. Inference Stage

#### 8.1 Ingestion Stage

* Dokumentensammlung und -aufbereitung
* Text-Preprocessing
* Chunking (Aufteilung aufgrund begrenzter Kontextfenster)

**Chunking-Methoden:**

* Fixed-Size Chunking mit Overlap
* Satzbasiertes Chunking
* Semantisches Chunking (aufwendig, modellabhängig)

Die Wahl der Chunkgröße erfordert umfangreiche Experimente.

#### 8.2 Inference Stage (Retrieval)

* Embedding der Chunks
* Speicherung in Datenbank
* Query-Embedding
* Retrieval relevanter Inhalte
* Kontextintegration und Antwortgenerierung

Viele Schritte (Templates, Chunking, Embeddings) sind systemseitig vorgegeben.

---

### 9. Erweiterte Retrieval-Strategien

#### 9.1 Query Expansion

* Ergänzung der Anfrage durch Synonyme oder verwandte Begriffe

#### 9.2 Hypothetische Dokumenterweiterung

* LLM erzeugt eine hypothetische Antwort
* Suche erfolgt anschließend anhand dieser Antwort

---

### 10. Vorteile von RAG

* Dynamische Aktualisierung von Wissen
* Kein kontinuierliches Finetuning notwendig
* Präzisere und faktenbasierte Antworten
* Nutzung domänenspezifischer Dokumente

---

### 11. Nachteile und Herausforderungen

* Aufwendiges Preprocessing
* Schwieriges Dokument-Parsing
* Abhängigkeit von Modellqualität und Prompt-Design
* Risiko fehlerhafter oder widersprüchlicher Dokumente
* Retrieval muss korrekte Informationen finden

---

### 12. Fazit

Viele Schwächen klassischer LLMs — insbesondere Halluzinationen und fehlende Aktualität — lassen sich durch **Grounding mittels externer Dokumente** reduzieren.

RAG ermöglicht:

* faktenbasierte Antworten
* Nutzung spezifischer Wissensquellen
* Vermeidung kontinuierlicher Modell-Neutrainings

Damit stellt RAG einen praktikablen Ansatz für produktive und zuverlässige LLM-Anwendungen dar.

# Lexikon #

| Wording                              | Definition                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| LLM (Large Language Model)           | Ein KI-Modell, das auf großen Textmengen trainiert wird und Sprache probabilistisch verarbeitet, um Texte zu verstehen und zu generieren.   |
| Halluzination                        | Phänomen, bei dem ein Sprachmodell überzeugend klingende, aber faktisch falsche oder erfundene Informationen erzeugt.                       |
| Grounding                            | Anbindung eines Sprachmodells an verlässliche externe Datenquellen, um Antworten faktenbasiert zu machen.                                   |
| Finetuning                           | Nachträgliches Weitertrainieren eines Modells mit zusätzlichen Daten, um domänenspezifisches Wissen zu integrieren.                         |
| Retrieval Augmented Generation (RAG) | Architektur, die ein Sprachmodell mit einem Dokumentenabrufsystem kombiniert, sodass Antworten auf Basis externer Inhalte generiert werden. |
| Source of Truth                      | Verlässliche und autoritative Datenquelle, die als Grundlage für korrekte Informationen dient.                                              |
| Embedding                            | Vektorielle Repräsentation von Text, bei der semantisch ähnliche Inhalte im Vektorraum nahe beieinander liegen.                             |
| Vektor-Datenbank                     | Datenbank zur Speicherung und Suche von Embeddings mittels Ähnlichkeitsberechnung.                                                          |
| Retriever                            | Komponente eines RAG-Systems, die relevante Dokumente aus einem Speicher basierend auf einer Anfrage auswählt.                              |
| Chunking                             | Aufteilung von Dokumenten in kleinere Textabschnitte, um sie effizient in Kontextfenstern von Sprachmodellen zu nutzen.                     |
| Fixed-Size Chunking                  | Chunking-Strategie mit gleich großen Textabschnitten, häufig mit Überlappung zur Wahrung des Kontexts.                                      |
| Semantisches Chunking                | Aufteilung von Dokumenten anhand inhaltlicher Struktur wie Absätzen oder Themen.                                                            |
| Ingestion Stage                      | Pipelinephase, in der Dokumente gesammelt, aufbereitet, gechunkt und in einer Datenbank gespeichert werden.                                 |
| Inference Stage                      | Phase der Anfrageverarbeitung, in der relevante Inhalte abgerufen und zur Antwortgenerierung genutzt werden.                                |
| Query Expansion                      | Erweiterung einer Suchanfrage durch Synonyme oder verwandte Begriffe zur Verbesserung des Retrievals.                                       |
| Hypothetische Dokumenterweiterung    | Retrieval-Technik, bei der ein Modell zunächst eine mögliche Antwort generiert, um darauf basierend relevantere Dokumente zu finden.        |
| Prompt Template                      | Vordefinierte Struktur einer Anfrage an ein Sprachmodell, die Kontext, Instruktionen und Nutzereingaben kombiniert.                         |
| Kontextfenster                       | Maximale Textmenge, die ein Sprachmodell gleichzeitig verarbeiten kann.                                                                     |
| Keyword-Suche                        | Klassische Suchmethode, bei der Dokumente anhand exakter Begriffsübereinstimmungen gefunden werden.                                         |
| Hybride Suche                        | Kombination aus Keyword-Suche und Vektorsuche zur Verbesserung der Retrieval-Qualität.                                                      |
