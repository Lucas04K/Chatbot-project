# Tag 16, 09.02.2026

Einführung in Neuronale Netze (Teil 1)

---
## __Grundlegender Überblick__

* Einordnung neuronaler Netze innerhalb von KI, Machine Learning und Deep Learning
* Biologische Inspiration: Neuronen, Gewichte und Aktivierungsfunktionen
* Historische Entwicklung: Perceptron, KI-Winter und Backpropagation
* Lineare vs. nicht-lineare Entscheidungsgrenzen
* Das XOR-Problem als zentrale Motivation für mehrschichtige Netzwerke
* Aufbau eines Dense (Fully Connected) Neural Networks
* Grundidee von Forward Propagation und Backpropagation
* Warum neuronale Netze heute praktikabel sind (Daten, Hardware, Frameworks)

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 10:00|Gruppenprojektarbeit mit Ensemble|
|10:10 - 11:20|Theoretische Einführung: Gehirn, Perceptron, Geschichte|
|11:30 - 12:30|XOR-Problem, Hidden Layers, Forward Pass, Loss, Backpropagation|
|12:10 - 13:30|Mittagspause| 
|13:30 - 16:30|Notebook day1, ds-artificial-neural-networks|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|

---

## __Erste inhaltliche Notizen__

### Was sind neuronale Netze?
Neuronale Netze sind ein Teilgebiet des **Machine Learning** und bilden die Grundlage von **Deep Learning**. Sie bestehen aus künstlichen Neuronen, die Eingaben gewichten, aufsummieren und mithilfe von **Aktivierungsfunktionen** auch nichtlineare Zusammenhänge modellieren können.


---

### Perceptron und historische Einordnung
- 1958: **Perceptron** als erstes künstliches Neuron  
    - Kann nur **lineare Probleme** lösen  
    - Scheitert am **XOR-Problem**  
- 1969: Kritik durch Minsky & Papert → erster KI-Winter
    - Darin zeigten sie mathematisch, dass einzelne Perceptrons nur lineare Probleme lösen können und nicht in der Lage sind, das XOR-Problem zu lernen.  
- 1980er: **Backpropagation** ermöglicht Training tiefer Netzwerke  
- Ab ~2012: Durchbruch durch GPUs, große Datenmengen, neue Architekturen und Softwares

---

### Das XOR-Problem
Das **XOR-Problem** ist nicht linear separierbar und kann daher nicht mit einem einzelnen Perceptron gelöst werden.  
→ Erst durch **mehrere Neuronen und Hidden Layers** wird eine Lösung möglich.

Beispiel aus dem Unterricht:
* „Entweder ins Kino gehen **oder** zu Hause bleiben – aber nicht beides gleichzeitig.“

Das XOR-Problem stammt aus der **Wahrheitstabelle (Truth Table)** der Logik.    

Dieses Problem zeigt, warum **Deep Learning** notwendig ist.

---

### Aufbau eines neuronalen Netzes
Ein neuronales Netz besteht aus:
* **Input Layer** – enthält die Eingabewerte  
* **Hidden Layer(s)** – lernen komplexe Feature-Interaktionen  
* **Output Layer** – liefert die Vorhersage  

Bei einem **Dense (Fully Connected) Netz** ist jedes Neuron mit allen Neuronen der nächsten Schicht verbunden.

---

### Aktivierungsfunktionen
Aktivierungsfunktionen entscheiden, **ob und wie stark** ein Neuron aktiviert wird, nachdem die gewichteten Eingaben aufsummiert wurden.  
Sie sind notwendig, um **Nichtlinearität** in das Netz zu bringen – ohne sie wäre auch ein tiefes neuronales Netz lediglich eine große lineare Funktion.

Beispiel aus dem Unterricht:
Ein Neuron erhält mehrere Eingaben (z. B. „hohes Einkommen“, „viel Freizeit“, „kurze Entfernung“).  
Erst die Aktivierungsfunktion entscheidet, ob diese Kombination stark genug ist, um z. B. die Entscheidung „ins Kino gehen“ auszulösen.

Typische Funktionen:
* **Sigmoid** – gibt Werte zwischen 0 und 1 zurück (geeignet für Wahrscheinlichkeiten)
* **ReLU** – gibt negative Werte als 0 zurück und lässt positive unverändert, wodurch Training effizienter wird

---

### Forward Propagation & Backpropagation (Schritt für Schritt)
1. **Input**  
   * Rohdaten werden in numerischer Form in den Input Layer gegeben  
2. **Gewichtete Summe**  
   * Jeder Input wird mit einem Gewicht multipliziert und aufsummiert  
3. **Aktivierungsfunktion**  
   * Die Summe wird durch eine Aktivierungsfunktion transformiert  
4. **Weitergabe durch Hidden Layers**  
   * Dieser Prozess wiederholt sich Schicht für Schicht  
5. **Output**  
   * Der Output Layer liefert eine Vorhersage (z. B. Wahrscheinlichkeit zwischen 0 und 1)  
6. **Loss-Berechnung**  
   * Die Vorhersage wird mit dem echten Wert verglichen  
7. **Backpropagation** 
   * Fehler wird rückwärts durch das Netzwerk propagiert  
   * Gewichte werden mithilfe der Kettenregel angepasst  

Das langfristige Ziel ist es, durch wiederholte Anpassung der Gewichte den **Loss zu minimieren**.

---

### Wichtige Einordnung
Neuronale Netze sind **nicht immer die beste Lösung**:
* Für **tabellarische Daten** sind Modelle wie Random Forest oder Gradient Boosting oft besser geeignet  
* Für **Bilder, Text und Audio** sind neuronale Netze meist überlegen  

Sie sind sehr leistungsfähig, aber:
* schwer interpretierbar  
* rechen- und energieintensiv 

---

## __Lexikon__

|Wording|Definition|
|---|---|
|Perceptron|Ein einzelnes künstliches Neuron mit gewichteten Eingaben|
|XOR-Problem|Nicht linear separierbares logisches Problem|
|Hidden Layer|Schicht zwischen Input und Output|
|Dense Layer|Vollständig verbundene Schicht|
|Aktivierungsfunktion|Erzeugt Nicht-Linearität im Netzwerk|
|Forward Propagation|Berechnung der Vorhersage von Input zu Output|
|Backpropagation|Anpassung der Gewichte anhand des Fehlers|




---
## __Links, Zitate, Bilder und GIFs__

* [Playground TensorFlow](https://playground.tensorflow.org/) 
* [TensorFlow guide Keras](https://www.tensorflow.org/guide/keras) 





---
## __Code in Notizen__

Du kannst Codeblöcke in deine Notizen einfügen, indem du den Code mit Backticks (\`) umschließt, sodass \`from x import y\` zu `from x import y` wird

