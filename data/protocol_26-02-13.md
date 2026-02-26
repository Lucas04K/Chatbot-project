# Tag 18, 13.02.2026

## __RNNs und Transformer__


## __Grundlegender Überblick__
**Sequenzielle Daten**: Verarbeitung von Daten, bei denen die Reihenfolge entscheidend ist (z. B. Text, Zeitreihen).   
**Recurrent Neural Networks (RNN)**: Grundlagen der Architektur und das Konzept des "Hidden State" als Gedächtnis.  
**Probleme von RNNs**: Herausforderungen wie "Vanishing Gradients" bei langen Abhängigkeiten.   
**LSTMs & GRUs**: Fortgeschrittene RNN-Zellen zur besseren Speicherung langfristiger Informationen.   
**Transformer & Attention**: Paradigmenwechsel weg von sequenzieller hin zu paralleler Verarbeitung durch den Aufmerksamkeitsmechanismus.   
**Praktische Anwendung**: Implementierung von Textklassifikation und Named Entity Recognition (NER).

---
## 1. Intuition: Warum Sequenzen schwierig sind
**Vergleich: Mensch ohne Gedächtnis**
- Geschichte ohne richtige Reihenfolge ergibt keinen Sinn  
- Satz anfangen und vergessen, worauf man hinauswollte  

→ Genau dieses Problem haben einfache neuronale Netze bei Sequenzen.

---

## 2. Sequenzdaten vs. Nicht-Sequenzdaten

### Reihenfolge egal:
- Bilder (räumliche Struktur wichtig: Lokalität, Stationarität)  
- Ob ein Auto im Bild links oder rechts steht, ist egal – wichtig ist **dass** ein Auto da ist  

### Reihenfolge wichtig:
- Natürliche Sprache  
  - „Der Mann biss den Hund“ ≠ „Der Hund biss den Mann“  
  - In Geschichten/Krimis ist die Reihenfolge entscheidend  
- Zeitreihen  
  - Börsenkurse  
  - Wetter  
  - Sensorwerte  
- Audio & Video  
  - Bedeutung entsteht über die Zeit  

---

## 3. Warum Feed-Forward-Netze nicht reichen
**Probleme:**
1. Reihenfolge wird nicht beachtet  
2. Sequenzen sind unterschiedlich lang  
3. Eingabegröße muss immer gleich sein (Sätze sind unterschiedlich lang)

**Lösung**:  
Spezielle Netze für Sequenzen → **RNNs & Transformer**

---

## 4. Rekurrente Neuronale Netze (RNN)
**Idee:**  
RNNs haben ein internes Gedächtnis (**Hidden State**).  
Der vorherige Zustand fließt in die nächste Berechnung ein.

**Beispiel (Experiment über mehrere Tage):**  
> Wir machen ein Experiment und arbeiten an zwei Tagen daran.  
> Am ersten Tag schreiben wir ein Protokoll mit den wichtigsten Ergebnissen –  
> nicht alle Rohdaten, sondern nur eine Zusammenfassung.  
>  
> Am zweiten Tag beginnen wir direkt mit den Ergebnissen vom ersten Tag  
> und machen von dort weiter.

**Fazit (Übertragung auf RNNs):**  
> Anstatt alle bisherigen Daten immer mitzunehmen,  
> behalten wir einen **Hidden State**, der aus dem vorherigen Zustand entsteht.  
> Dieser Hidden State fasst die Vergangenheit zusammen  
> und beeinflusst den nächsten Schritt.  

→ Der Hidden State ist also wie eine **komprimierte Erinnerung** an alles,  
was vorher passiert ist.

**Vereinfachte Darstellung:**  
Neuer Zustand = Funktion(Eingabe + vorheriger Zustand)

---

##  Probleme von RNNs
- Verlust wird für **jeden Zeitschritt** berechnet  
- Gesamtverlust = Summe über alle Zeitschritte  
- Gradienten werden durch die Zeit zurückpropagiert  

**Problem: Vanishing Gradient**
- Je weiter zurück, desto kleiner die Gradienten  


→ Frühere Informationen gehen beim Training verloren  
→ Schwierigkeit, **lange Abhängigkeiten** zu lernen  
→ Langsames Training, da Berechnung **nicht parallelisierbar**

---

##  Lösung: LSTM & GRU (Long Short-Term Memory & Gated Recurrent Unit)
**Ziel:**  
Langfristige Abhängigkeiten besser speichern.

Mechanismen:
- **Input-Gate:** Welche Info ist wichtig?  
- **Forget-Gate:** Was kann vergessen werden?  
- **Output-Gate:** Was wird weitergegeben?

**Beispiel:**  
> „Der Mann, der sehr skeptisch ist und gestern spät gekommen ist, war da.“  
→ Subjekt und Verb liegen weit auseinander  
→ Braucht Langzeitgedächtnis  

**Vorteil:**  
Besseres Merken wichtiger Informationen über längere Zeiträume.

**GRU:**   vereinfachte Alternative zu LSTM
- schneller  
- weniger flexibel  
- kombiniert Input- und Output-Gates  

---

## Grenzen von RNNs
- Keine Parallelisierung möglich  
- Langsam bei langen Sequenzen  
- Für lange Texte ungeeignet  
- Vorteil:  
  - wenig Speicher  
  - gut für Echtzeit & kleine Geräte  

---
##  5. Transformer – neue Idee
**Statt:** Wort für Wort lesen  
**Jetzt:** Alle Wörter gleichzeitig betrachten  

→ Parallele Verarbeitung  
→ Globaler Kontext

Kernmechanismus: **Attention**

---

## Attention – Intuition (Party-Beispiel)
Du bist auf einer Party und willst über Machine Learning reden:

- **Query (Q):** „Ich suche Gespräche über ML“  
- **Keys (K):**
  - Fußball → 5 %  
  - Machine Learning → 80 %  
  - Technik → 15 %  
- **Values (V):**  
  Infos, die du von diesen Personen bekommst  

→ Attention entscheidet, wem du wie stark zuhörst.

---
## Attention als Matrix-Rechnung (Q, K, V)

Jedes Wort wird zu drei Vektoren:
- **Query (Q)**  
- **Key (K)**  
- **Value (V)**  

**Vereinfachte Formel:**  
Attention(Q, K, V) = softmax(Q · Kᵀ) · V

→ Jedes Wort „schaut“ auf alle anderen Wörter.  
→ Stärkste Beziehungen bekommen mehr Gewicht.

---

## Positionsinformation im Transformer
Problem:  
Transformer kennen keine Reihenfolge.

Lösung:  
**Positional Encoding**  
- Jeder Token bekommt einen Positionsvektor  
- Dieser wird zum Wortvektor addiert  

→ „Katze beißt Hund“ ≠ „Hund beißt Katze“

---
## Bedeutung entsteht durch Training
- Wörter liegen als Vektoren im Raum  
- Ähnliche Begriffe liegen näher beieinander  
  - „Roboter“ näher an „Maschine“ als an „weil“  
- Attention-Gewichte werden **gelernt**
---
## Aufbau eines Transformers
1. Tokens → Embeddings  
2. Positional Encoding  
3. Self-Attention  
4. Feed-Forward-Netz  
5. Mehrere Encoder-Layer  
6. Decoder erzeugt Ausgabe  

Alle Tokens sehen sich **gleichzeitig**.

---

## Vorteile von Transformern
- Sehr gut für lange Texte  
- Schnelleres Training  
- Globaler Kontext  
- Grundlage moderner KI-Systeme (z. B. Chatbots, Übersetzung, Textzusammenfassung)

---

## Grenzen von Transformern
- Sehr rechenintensiv  
- Benötigen viele Daten  
- Schwer interpretierbar  
- Attention erklärt nicht vollständig „Warum“  
- Modelle sind nur so gut wie die Trainingsdaten 

---

##  6. Vergleich: RNN vs Transformer


| Aspekt                 | RNN                    | Transformer              |
|-----------------------|------------------------|--------------------------|
| Verarbeitung          | Schrittweise           | Parallel                 |
| Lange Abhängigkeiten  | schwierig              | sehr gut                 |
| Training              | langsam                | schneller                |
| Rechenaufwand         | gering                 | hoch                     |
| Ressourcenbedarf      | gering                 | hoch                     |
| Geeignet für          | Echtzeit, kleine Geräte| NLP, lange Texte         |

---
# Lexikon #
|Wording|Definition|
|---|---|
|**Attention**|Ein Mechanismus, der es dem Modell erlaubt, sich auf relevante Teile der Eingabe zu konzentrieren, unabhängig von deren Position.|
|**BERT**|(Bidirectional Encoder Representations from Transformers) Ein vortrainiertes Modell, das Textkontext von links nach rechts und rechts nach links gleichzeitig liest.|
|**BPTT**|(Backpropagation Through Time) Die Methode zum Trainieren von RNNs, bei der Fehler über die Zeitschritte zurückgereicht werden.|
|**Fine-Tuning**|Der Prozess, ein bereits vortrainiertes Modell auf eine neue, spezifische Aufgabe (z. B. Sentiment-Analyse) zu trainieren.|
|**GRU**|(Gated Recurrent Unit) Eine effiziente Variante des LSTM mit weniger Parametern.|
|**Hidden State**|Der interne Vektor in einem RNN, der Informationen aus vergangenen Zeitschritten speichert.|
|**LSTM**|(Long Short-Term Memory) Eine RNN-Architektur, die durch spezielle "Gates" das Verschwinden von Gradienten verhindert.|
|**NER**|(Named Entity Recognition) Die Identifizierung und Klassifizierung von Eigennamen (Personen, Orte, Organisationen) in Texten.|
|**RNN**|(Recurrent Neural Network) Ein Typ von neuronalem Netz, das für die Verarbeitung von Sequenzen interne Schleifen nutzt.|
|**Tokenisierung**|Zerlegung von Rohtext in kleinere Einheiten (Tokens), die als numerische Eingabe für Modelle dienen.|
|**Transformer**|Eine moderne Architektur, die ausschließlich auf Attention-Mechanismen basiert und paralleles Training ermöglicht.|
|**Vanishing Gradient**|Ein Problem beim Training tiefer Netze, bei dem Gradienten gegen Null gehen und das Modell keine langfristigen Abhängigkeiten lernt.|





---
## __Markdown-Formatierung__

* eine Überschrift erstellst du mit #, ein # für eine Überschrift der Ebene 1 (die größte) – du kannst bis Ebene 6 gehen
* neue Zeile beginnen: zwei Leerzeichen verwenden
* benutze einfache Sternchen oder Unterstriche, um Wörter kursiv zu machen (\*Wörter* ergibt *Wörter*) 
* benutze doppelte Sternchen oder Unterstriche, um Wörter fett zu machen (\*\*dies** ergibt **dies**)
* benutze drei Sternchen oder Unterstriche, um beides gleichzeitig zu tun (\_\_\_ x ___ ergibt ___x___)
* eine Trennlinie erstellst du mit drei Bindestrichen (---)
* ungeordnete Listen erstellst du mit einem Sternchen (*) und geordnete Listen mit einer Zahl, einem Punkt und einem Leerzeichen (1. )  
(__sehr nützlich__: es spielt keine Rolle, welche Zahl du verwendest – sie wird automatisch als 1, 2 usw. angezeigt)
* du kannst die Textfarbe mit „span“-Tags ändern (\<span style="color:red"> Beispiel \</span> ergibt <span style="color:red">Beispiel</span>)  
(__Hinweis__: Schriftfarben werden auf GitHub nicht angezeigt)


---
## __Links, Zitate, Bilder und GIFs__

* du kannst Links in deinen Notizen mit folgender Formatierung verwenden:  
[Linktitel](Link-URL) wird zu [Neuefische Website](https://www.neuefische.de/)
* du kannst auch Bilder in deinen Notizen verwenden, mit dieser Formatierung:   
![Bildtext](Bild-URL) wird zu ![neuefische Logo](images/logo.png)
* Blockzitate: du kannst ein Zitat hervorheben, indem du eine spitze Klammer (>) verwendest, zum Beispiel: 
    > Ich glaube, es gibt einen Weltmarkt für vielleicht fünf Computer. – Thomas J. Watson Sr.
* verwende GIFs mit der gleichen Formatierung wie Links und Bilder. Die verwendete URL muss auf .gif enden, und wenn sie abläuft, wird dein GIF nicht mehr angezeigt  
    Beispiel:  
    ![Fisch-Gif](https://media.giphy.com/media/KAI3j7HLC93Lq/giphy.gif)


---
## __Gute Notizen schreiben__

* bleibe bei einem Stil, z. B. Links kursiv, Schlüsselbegriffe fett, Trennlinien zwischen Themen usw.  
* variiere deinen Textstil nicht zu stark – halte es einfach
* verwende fette und kursive Wörter sparsam, damit sie stärker hervorstechen


---
## __Code in Notizen__

Du kannst Codeblöcke in deine Notizen einfügen, indem du den Code mit Backticks (\`) umschließt, sodass \`from x import y\` zu `from x import y` wird


---
## __Hilfreiche Referenzen__

* [Markdown Cheatsheet auf Github](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
* [Leitfaden zu Markdown für Dokumentationsautor:innen](https://document360.com/blog/introductory-guide-to-markdown-for-documentation-writers/#p8)
* [Markdown Crashkurs von Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo)
* [Grundlegende Markdown-Einführung und Syntax von Mike Dane](https://www.youtube.com/watch?v=2JE66WFpaII)
