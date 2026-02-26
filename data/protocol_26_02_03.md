# Tag 12, 03.02.2026

Gradientenabstieg (Gradient Descent)

---
## __Grundlegender Überblick__

* Einordung in den Data Science Lifecycle
* Einleitung über OLS
* Analogie: Abstieg vom Berg
* Problemfälle: lokales Minimum und Plateau
* Lernrate 
* Varianten des Verfahrens

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:45|Daily Review|
|10:00 - 11:00|Gradient Descent|
|11:00 - 12:30|Notebooks zu Gradient Descent|
|12:10 - 13:30|Mittagspause| 
|13:30 - 16:00|Notebooks zu Gradient Descent|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Vertiefung|
---
##  __Haupt Take-Away__

Gradient Descent wird verwendet, wenn andere Optimierungsverfahren zu aufwendig sind. Dabei werden die Parameter jeweils in die Richtung geändert, in die sich die größte Modellverbesserung ergibt.
Probleme können lokale Minima und Plateaus sein.

---
## __Notizen__

### Einordnung
Zur Orientierung: im Schaubild 'Data Science Lifecycle' ist der Gradientabstieg bei 'Schritt 6: Predictive Modeling/Training' einzusortieren.

### Herleitung
Bei der Optimierung der lineare Regression wird die Kostenfunktion per Ordinary Least Squares minimiert:

$$ J(b_{0},b_{1})\ =\ \sum_i^n(y_{i}\ -\hat{y}_{i})^{2}$$

$$\frac{\partial J}{\partial b_{j}}\ =\ 0$$

D.h. die Kostenfunktion J(b<sub>0</sub>,b<sub>1</sub>) wird nach den Parametern b<sub>j</sub> abgeleitet und gleich 0 gesetzt.

Für komplexere Modell gibt es oft keine einfache Ableitung.
Dort greift dann ein iterativer Optimierungsalgorithmus.

### Analogie
Analogie: Abstieg vom Berg im Nebel. Wie kommt man am schnellsten ins Tal?   
=> Wo ist das steilste Gefälle? In diese Richtung wird gegangen. 

### Funktionsweise des Gradientenabstiegsverfahren
Für den iterativen Algorithmus des Gradientenabstiegs heißt das:   
- Beginne mit zufälligen Parametern b.   
- Suche die Richtung, in der die Parameteränderung eine größte Änderung der Kostenfunktion bringt,   
- ändere die Parameter entsprechend und fahre so fort,   
- bis eine Änderung nur noch eine sehr kleine oder gar keine Verbesserung mehr bringt.

### Verwendung

Wann wird Gradient Descent verwendet?
- einfaches Verfahren für viele ML-Algorithmen
- Backpropagation in neuronalen Netzen
- gut, wenn viele Features vorhanden und Normalengleichung zu langsam

### Probleme
- lokales Minimum: Ggf. wird das globale Minimum nicht gefunden, sondern nur ein lokales. 
- Plateau: Im Verlauf der Parameteränderungen gibt es ein Plateau. D.h. eine Änderung der Parameter bringt über eine längere Strecke keine Verbesserung der Kostenfunktion. Und der Gradientenabstieg bleibt dort 'hängen'.

Abhilfe:   
Änderung der Hyperparameter zum Start des Gradientenabstiegs:
- andere Ausgangswerte für den Start der Optimierung wählen
- Lernrate ändern: eine höhere Lernrate überspringt ggf. das lokale Minimum oder das Plateau

Dabei ist zu beachten:
- zu kleine Lernrate führt zu sehr kleinen Schritte, d.h. zu langer Rechenzeit
- zu große Lernrate: Minimum wird ggf. (mehrfach) übersprungen oder nie erreicht

Ein weiteres Problem können **unskalierte** Daten sein. Dies führt i.d.R. dazu, dass der Algorithmus mehr Zeit braucht.   
Visuell kann man sich das Vorgehen bei unskalierten Daten so vorstellen, dass die Steigungen in unterschiedliche Richtungen stark unterschiedlich sind.

### Varianten des Verfahrens

#### Batch Gradientenabstieg
Alle Instanzen werden verwendet, um den Gradienten zu berechnen.   
Vorteil: genauer

#### Stochastistischer GD
Nur eine zufällige Instanz wird verwendet.   
Vorteil: deutlich schneller

#### Mini-Batch-GD
Trainiert auf zufälliger Teilmenge anstatt auf allen Daten oder auf einzelnen. Besser als Stochastistischer Gradientenabstieg, da Hardware-Optimierung von Matrixoperationen verwendet werden kann.   
In der Praxis wird i.d.R. Mini Batch verwendet, weil dies normalerweise ein guter Kompromiss aus Rechenzeit und Genauigkeit ist.

---
## Lexikon
|Wording|Definition|
|---|---|
|Gradient Descent|Verfahren, bei dem die Parameter in Richtung des steilsten Abstiegs hin zum Minimum der Kostenfunktion schrittweise optimiert werden.|
|globales Minimum|Die absolut niedrigste Stelle der Kostenfunktion. Das ist i.d.R. das Ziel, das bei der Optimierung erreicht werden soll.|
|lokales Minimum|Eine Stelle, die umgeben ist von höheren Kosten aber nicht das globale Minimum der Kostenfunktion darstellt.|
|Plateau|Bereich in der Kostenfunktion, bei der über eine mehrfache Änderung der Parameter die Kostenfunktion denselben Wert beibehält.|
|Batch GD|Verfahren des Gradient Descent bei dem alle Instanzen werden um den Gradienten zu berechnen.|
|Stochastischer GD|Nur _eine_ zufällige Instanz wird verwendet, um den Gradienten zu berechnen.|
|Mini-Batch-GD|Trainiert auf zufälliger Teilmenge zur Gradientenberechnung.|
|Lernrate|Schrittweite der Parameteranpassung bei jedem Schritt (Hyperparameter)|
|Startwerte|Anfangswerte der Parameter (Hyperparameter)|

---

## Zusammenfassung 
- Gradient Descent verbessert die Modellparameter schrittweise in Richtung kleinerer Kosten, solange bis keine wesentliche Verbesserung mehr erreicht wird.
- Wird verwendet, wenn genaue mathematische Verfahren zu aufwendig bzw. rechenintensiv sind, z.B. in neuronalen Netzen.
- Gut bei vielen Features.
- Probleme können bei lokalen Minima oder Plateaus auftreten.
- Abhilfe schaffen dabei Variation der Startparameter und/oder Änderung der Lernrate.
- Varianten des Verfahrens sind Batch GD, Stochastischer GD und Mini-Batch-GD.
---
### Referenzen
[Kursmaterial zu Gradient Descent](https://literate-adventure-1e3gl8r.pages.github.io/sessions/14_Gradientenabstieg_DE.html)   
[StatQuest GradientDescent step-by-step auf youtube](https://www.youtube.com/watch?v=sDv4f4s2SB8)

