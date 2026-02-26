# Tag 08, 28.01.2026

KNN & Distanzmetriken

---
## __Grundlegender Überblick__

- Überwachtes Lernen:
    - Arbeitet mit gelabelten Daten
    - Zwei Hauptaufgaben:
        - Klassifikation (diskrete Klassen)
        - Regression (kontinuierliche Werte)
- Unüberwachtes Lernen:
    - Keine Labels
    - Ziel: Strukturen, Cluster oder Muster finden
- KNN (k-Nearest Neighbors):
    - Algorithmus des überwachten Lernens
    - Kann für Klassifikation und Regression verwendet werden
    - Grundannahme:
        - „Ähnliche Dinge befinden sich nahe beieinander“

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:45|Daily Review|
|10:00 - 11:08|Erste theoretische Inputs|
|11:16 - 12:10|Weitere theoretische Inputs|
|12:10 - 13:30|Mittagspause| 
|13:30 - 16:00|Praktische Übungen|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|


---
## __Erste inhaltliche Notizen__
KNN ist ein sehr intuitiver Algorithmus:

Um eine neue Beobachtung vorherzusagen, schaut man sich einfach die K nächsten Nachbarn im Merkmalsraum an und entscheidet basierend auf diesen.
- Keine explizite Modellfunktion
- Keine Annahme über Datenverteilung
- Entscheidungen entstehen lokal durch Nachbarschaften

➡️ Deshalb eignet sich KNN besonders gut für unregelmäßige Entscheidungsgrenzen.

---
**Beispiel (Party-Analogie)**

**Situation:**
Ich bin zu einer Party eingeladen von einer Person, die ich nur über Freunde kenne.
Ich weiß nicht direkt, welches Geschenk passt.

**Gedanke:**
- Ich schaue mir an, was die Freunden der Personen mögen
- Ich suche nach Ähnlichkeiten
- Je näher/Ähnlich die Fruende an die Personen → desto relevanter ihre Vorlieben

➡️ Genau so funktioniert KNN:
Neue Punkte werden anhand ähnlicher bekannter Punkte eingeschätzt.

---

**Wie funktioniert KNN?**

**Eingabe**
- Trainingsdaten mit:
    - vergleichbaren Features
    - Zielvariable (Label)

**Ablauf**
1. Alle Trainingsdaten werden gespeichert
2. Für eine neue Beobachtung:
    - Distanz zu allen Trainingspunkten berechnen
    - Die K nächsten Nachbarn auswählen

➡️ Lazy Algorithmus:
- Training: sehr schnell (nur Speichern)
- Vorhersage: langsam (Distanzberechnung)

---

**Vergleich zu anderen Algorithmen**

**KNN:**
- Keine Trainingsphase im klassischen Sinn
- Rechenaufwand bei der Vorhersage
- kein Annahmen über Datenverteilung
- ähnliche Beobachtungen haben die gleiche Klasse oder ähnliches Ergebniss
- **Nicht-parametrischer Algorithmus**

**Lineare / Logistische Regression:**
- Rechenaufwand beim Training (Gewichte lernen)
- Schnelle Vorhersagen
- Starke Annahmen über Datenverteilung

---

**Hyperparameter von KNN**
- K (Anzahl der Nachbarn)
- Distanzmetrik
- Gewichtung der Nachbarn

---

**Einfluss von K**
- K = 1:
    - Sehr flexibel
    - Lernt Daten „auswendig“
    - **→ Overfitting**

- Mittleres K:
    - Gute Generalisierung
- Sehr großes K:
    - Zu grobe Entscheidungen
    - **→ Underfitting**

---
**Distanzmetriken**
Warum Distanz wichtig ist:

KNN basiert vollständig auf der Frage:       **„Was ist nah und was ist fern?“**

Welche  Distanzmetriken gibt es?
- **Euklidische Distanz**
    - Luftlinie zwischen zwei Punkten
    - Standard für: 
        - kontinuierliche
        - dichte Daten
- **Manhattan-Distanz**
    - Summe der absoluten Differenzen
    - Wie ein Taxi in Manhattan
    - Gut für:
        - hochdimensionale (z.B bilogische/ wissenschafliche Daten)
        - spärliche Daten
- **Minkowski-Distanz**
    - Verallgemeinerung:
        - p = 1 → Manhattan
        - p = 2 → Euklidisch
        - p = ∞ → Tschebyschow
- **Tschebyschow-Distanz** (nicht revant für uns, Flugzeugbewegungen)
- **Kosinus-Ähnlichkeit / -Distanz**
    - Misst den Winkel zwischen Vektoren
    - Unabhängig von der Länge
    - Besonders geeignet für:
        - Textdaten
        - NLP
        - hochdimensionale Vektoren
        - Bilder Klassifizierung 

---

**Feature Engineering & Skalierung**

Problematische Features
- Nominale Daten (z.B. Ländernamen)
- Keine natürliche Distanz
- Rangfolgen ohne echte Abstände

Lösung
- Feature Engineering:
    - Umwandeln in numerische Features
    - Extraktion relevanter Eigenschaften
- Skalierung:
    - Sehr wichtig bei Distanzmetriken
- Feature-Auswahl:
    - Nur relevante, vergleichbare Features verwenden

### Fazit ###
KNN ist ein einfaches, aber mächtiges Verfahren des überwachten Lernens.
Seine Stärke liegt in der lokalen Betrachtung von Daten und der Fähigkeit, komplexe Entscheidungsgrenzen abzubilden. Gleichzeitig ist KNN stark abhängig von:
- der Wahl von K
- der Distanzmetrik
- gutem Feature Engineering
- Skalierung der Daten

Richtig eingesetzt ist KNN besonders effektiv in Bereichen wie Bild- und Textverarbeitung.



# Lexikon #
|Wording|Definition|
|---|---|
|KNN|Überwachter Lernalgorithmus, der Vorhersagen anhand der nächsten Nachbarn trifft|
|Überwachtes Lernen|Lernen mit gelabelten Daten|
|Lazy Algorithmus|Training günstig, Vorhersage teuer|
|Distanzmetrik|Mathematische Definition von „Nähe“|
|Overfitting|Modell lernt Trainingsdaten zu genau|
|Underfitting|Modell ist zu einfach|
|Hyperparameter|Vom Nutzer festgelegte Parameter|



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
