# Tag 26, 23.02.2026

Prompt-Engineering

---
## __Grundlegender Überblick__

* Einführung und Anekdote
* LLMs
* Wie Prompts funktionieren
* Prompt-Vorlagen

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:25|Daily Review|
|10:00 - 11:15|Erste theoretische Inputs|
|11:15 - 12:15|Mittagspause| 
|13:30 - 16:00|Praktische Übungen|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|


---
## __Erste inhaltliche Notizen__


### Anekdote
Die Fluglinie Air Canada, deren ChatBot behauptete 90 Tage dauerte  eine Rücküberweisung


# Lexikon #
|Wording|Definition|
|---|---|
|Emergentes Phänomen|Emergente Phänomene sind neu auftretende Eigenschaften oder Verhaltensmuster, die in komplexen Systemen durch das Zusammenspiel einfacher Komponenten entstehen. Sie sind nicht direkt aus den Eigenschaften der Einzelteile ableitbar.|


## Einführung
- LLMs sind Transformer mit unglaublich viel mehr Paramenter, Daten und Rechenleistung
- Emergentes Phänomen

#### Abgrenzung zu standadisierten Transformern
- Unterschiede zwischen LLM und Transformern: Skalierung 
- LLMs haben rekursiven Schritt aus Reinforcement Learning (Feedbackschleife: Belohnung und Bestrafung, Bei LLMs durch unser Feedback)

## Was sind LLMs
- Überwachte Modelle
- Beispiel: Vorhersage von dem nächsten Wort in einem Satz

### Text generieren
- Es wird ein Ausgangspunkt benötigt
- Die Eingabe ist unser Ausgangspunkt/Ausgangstext
- Das nennt man Prompt

### Gandalf-AI-Game
https://gandalf.lakera.ai/baseline <br />

![alt text](images/image.png)


### Prompt-Struktur
- Systemnachricht
- Benutzernachricht
- Assistentennachricht

### Prompt-Elemente
- Anweisung
- Kontext
- Eingabedaten
- Ausgabeindikatoren

#### Beispiel:
__Prompt:__<br />
```Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

__Output__<br />
`Neutral`

### Zero-Shot-Prompting<br />
KI-Prompting-Methode, bei der das Modell eine Aufgabe ohne vorherige Beispiele oder Trainingsdaten löst

__Prompt:__<br />
```Classify the text into neutral, negative or positive.
Text: I think the vacation is okay.
Sentiment:
```

__Output__<br />
`Neutral`

### Few-Shot-Prompting<br />
KI-Technik, bei der dem Sprachmodell (LLM) zusätzlich zur Aufgabenstellung mehrere Beispiele (meist 2-10) im Prompt übergeben werden

__Prompt:__<br />
```Classify the text into neutral, negative or positive. 
Follow these examples:

Example 1: 
Text: I think the movie is very bad
Sentiment: Negative

Example 2:
Text: Today was a good day!
Sentiment: Positive

Example 3:
Text: Today we learnt about Machine Learning
Sentiment: Neutral

Now classify the following text:

Text: I think the vacation is okay.
Sentiment:
```

__Output__<br />
`Neutral`

### Chain-of-Thought-Prompting (CoT)<br />
Prompt-Engineering-Technik, die große Sprachmodelle (LLMs) anleitet, komplexe Aufgaben durch schrittweises logisches Denken zu lösen, anstatt direkt eine Antwort zu generieren
