# Tag 27, 24.02.2026

Halluzination, Feedback-Loop, Security & AI-Agents

---
## __Grundlegender Überblick__

Unsere Arbeit besteht nicht darin lediglich Modelle oder Agents zu bauen, sondern dass wir als Professionals Verantwortung für die kritischen Ebenen darüber und darunter übernehmen müssen: Wir müssen Halluzinationen durch sauberes Prompting und klare Confidence-Angaben begrenzen, Sicherheitsmechanismen gegen Prompt Injection und Datenlecks etablieren, Tool-Zugriffe bewusst kontrollieren und gleichzeitig systematisch aus Nutzerfeedback lernen, um Qualität, Verlässlichkeit und Sicherheit der Systeme kontinuierlich zu verbessern.

---

# Lexikon #

|Wording|Definition|
|---|---|
|Halluzination|Plausible, aber faktisch falsche Modellantwort|
|Grounding|Beschränkung auf Referenztext|
|Zero-Shot|Wir geben dem Modell eine Anweisung, aber keine Beispiele. Es muss aus seinem Training generalisieren.|
|Few-Shot|Wir geben zusätzlich konkrete Beispiele vor, wie die Antwort aussehen soll, zum Beispiel inklusive einer Sicherheitsangabe wie „hoch“, „mittel“ oder „niedrig“|
|PPO|Proximal Policy Optimization ist ein Verfahren aus dem Reinforcement Learning. Es sorgt dafür, dass Anpassungen am Modell kontrolliert und stabil passieren. Das Modell wird verbessert, aber nicht radikal verändert.| 
|Prompt Injection|Manipulative Eingabe zur Umgehung von Systemregeln|
|Defense in Depth|Mehrschichtige Sicherheitsstrategie|
|ReAct|Reason → Act → Observe Zyklus|
|Human-in-the-Loop|Menschliche Bestätigung vor kritischer Aktion|

---
## __Notizen__

### Halluzination ###
Halluzination bedeutet, dass ein LLM eine plausibel klingende, aber faktisch falsche Antwort generiert, weil es statistisch die wahrscheinlichste Wortfolge auswählt.

* LLMs arbeiten probabilistisch (nächstwahrscheinliches Token)
* Plausibilität ≠ Wahrheit
* Beispiel:  Alan Turing veröffentlichte 1950 „Minds and Machines“, das klingt logisch, existiert aber nicht (korrekt: *Computing Machinery and Intelligence*).


### Strategien gegen Halluzination ###
Ziel ist es, den Antwortspielraum des Modells gezielt einzugrenzen. Halluzination kann nie vollständig ausgeschlossen werden, bei kritischen Themen immer "Double-Check" (z. B. Medikamente)

- **1. Grounding:**
  - Referenztext vorgeben
  - Beantworte nur auf Basis des Textes, sonst sage: "Auf Grundlage der verfügbaren Informationen kann keine eindeutige Aussage getroffen werden.“
  - Reduziert freien Assoziationsraum
- **2. Chain-of-Thought**
  - Schritt-für-Schritt argumentieren lassen
  - Am Ende Unsicherheit kennzeichnen
  - Optional: „Falls unsicher, markiere als unsicher“
- **3. Confidence-Abfrage**
  - Sicherheit explizit angeben (hoch/mittel/niedrig)
  - Zero-Shot oder Few-Shot mit Beispielen
  - Beispielstruktur vorgeben (z. B. Antwort + Sicherheit)

---

### Prompt Injection & Sicherheit ###
Prompt Injection bezeichnet Manipulationen durch User-Input, die das Modell dazu bringen, Systemanweisungen zu ignorieren oder sensible Daten preiszugeben.

Sobald ein Agent Zugriff auf Datenbank oder System hat, existiert kein 100 %iger Schutz.


### Mehrschichtige Sicherheitsstrategie (Defense in Depth) ###
Mehrere Schutzschichten werden kombiniert, um Risiken zu minimieren.

* Whitelisting erlaubter Eingaben (sicher, aber unflexibel)
* Trennung von System- und User-Input (z. B. JSON/XML-Struktur)
* Validierungsschicht zwischen Input & Output, ggf. zweites Modell zur Prüfung
* Logging aller Prompts & Outputs
* Anomalie-Erkennung und Alerts bei ungewöhnlichem Verhalten
* Human-in-the-Loop bei sensiblen Aktionen
* Berechtigungssysteme für Datenbankzugriffe
* Trade-Off:  Je mehr Sicherheit desto weniger Flexibilität.

---

### Feedback-Loop zur Modellverbesserung ###
User-Feedback kann strukturiert gesammelt und zur Optimierung des Modells verwendet werden.

Prozess:

1. Frontend (Upvote/Downvote)
2. Speicherung in Datenbank
3. Analyse (EDA auf Feedback-Daten)
4. Muster erkennen
5. Modell anpassen

**Verbesserungsoptionen:**

* Anpassung von System-Prompts
* Supervised Fine-Tuning mit guten Antworten
* Reinforcement Learning (Reward-Matrix, z. B. PPO)


---

## __AI-Agents__

### Unterschied zwischen LLM und Agent ###
Ein LLM kann Aufgaben verstehen und Text generieren, bleibt aber auf sprachliche Antworten beschränkt, während ein Agent zusätzlich mit Tools verbunden ist, planen, Entscheidungen treffen und reale Aktionen im System ausführen kann.

Das LLM ist dabei das „Gehirn“ oder der „Dirigent“, der plant und entscheidet, während die angebundenen Tools den „Körper“ bilden, der die geplanten Aktionen tatsächlich ausführt.

LLM = Gehirn (Denken)  
Agent = Gehirn + Werkzeuge (Handeln)

---

### Aufbau eines Agents ###

**Gehirn (LLM):**
* Ziel verstehen
* Plan erstellen
* Tool auswählen
* Ergebnis reflektieren

**Tools (Körper):**
* Web-APIs (z. B. Wetter)
* Datenbank-Zugriff
* Shell-Commands
* E-Mail senden/lesen
* Dateisystem

---

## __Agent-Typen__

### 1. ReAct-Agent ###
Denkt, handelt und beobachtet iterativ im Zyklus: Reason → Act → Observe → Repeat.

**Beispiele:**

* Wetter-Agent  
  → Fragt Wetter-API ab → generiert Antwort („15 Grad, bewölkt“)

* Reiseplan-Agent  
  → Prüft Flüge → vergleicht Zeiten → wählt beste Option → bucht → sendet Bestätigung

---

### 2. Plan-and-Execute-Agent ###
Erstellt zuerst einen vollständigen Plan und führt ihn dann strukturiert aus.

**Beispiele:**

* Geburtstagsparty organisieren  
  → Kalender prüfen  
  → Location reservieren  
  → Gästeliste erstellen  
  → Einladungen versenden  
  → Catering buchen  

* Reise planen (strukturierte Variante)  
  → Schritte komplett planen  
  → Danach systematisch ausführen

---

### 3. Reflection-Agent ###
Überprüft und verbessert eigenen Output iterativ.

**Beispiel:**

* Essay schreiben  
  → Essay generieren  
  → Fehler prüfen  
  → Stil verbessern  
  → Redundanzen entfernen  
  → finale Version ausgeben

---

### 4. Multi-Agent-System ###
Mehrere Agents übernehmen spezialisierte Rollen.

**Beispiel:**

* Agent 1: Feedback sammeln & in Datenbank speichern  
* Agent 2: Feedback analysieren  
* Agent 3: Kundensegmentierung  
* Agent 4: Marketing-E-Mail generieren und Mailing versenden  

---

## __Risiken von Agents__

Agents erhöhen das Risiko, da sie handeln können nicht nur Text erzeugen.

* Halluzination mit selbst Handlung ist ein reales Schadenspotenzial
* Endlosschleifen (z. B. ständige API-Abfragen)
* Hohe Tokenkosten
* Sicherheitsrisiken durch Systemzugriff
* Sensible Daten können weitergegeben werden
* Fehlkonfiguration durch unreflektiertes „Vibe-Coding“

**Empfehlungen:**

* Tool-Zugriffe klar definieren
* Rate-Limits setzen
* Confidence-Abfragen integrieren
* Human-in-the-Loop bei Geld oder sensiblen Daten

---

## __OpenClaw (Open-Source-Agent)__

OpenClaw ist ein Open-Source-Agent mit umfassendem Systemzugriff, der lokal oder mit Cloud-LLMs betrieben werden kann.

**GitHub:**
https://github.com/openclaw/openclaw  
→ Open-Source-Agent mit System-, Browser- und E-Mail-Zugriff

**Entwickler:**
https://github.com/steipete  
→ Peter Steinberger

**Eigenschaften:**

* Zugriff auf lokale Hardware
* Messaging-Integration
* Shell-Commands
* YAML-basierte Skills
* Verbindung mit Ollama oder Cloud-LLMs

**Probleme & Risiken:**

* Fehlinterpretation („Räume mein Postfach auf“ → alle Mails gelöscht)
* Hohe Tokenkosten durch Endlosschleifen
* Emergent Behavior
* Hohe Sicherheitsrisiken

---

## __Notebooks__

Deutsch:  
https://github.com/neuefische/ds-ai-agents-de.git  

Englisch:  
https://github.com/neuefische/ds-ai-agent.git  
