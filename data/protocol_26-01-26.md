# Tag 06, 26.01.2026

Evaluierungsmetriken

---

## Grundlegender Überblick

- Überwachtes Lernen nutzt gelabelte Daten zur Modellbildung.
- Klassifikation ordnet Eingaben diskreten Klassen zu, Regression sagt kontinuierliche Werte voraus.
- Klassifikationsprobleme können binär, multiklassig oder multilabel sein.
- Die Konfusionsmatrix bildet die Grundlage zur Bewertung von Klassifikationsmodellen.
- Accuracy ist intuitiv, aber bei unausgewogenen Daten oft irreführend.
- Precision und Recall bewerten unterschiedliche Arten von Fehlern.
- Der F1-Score balanciert Precision und Recall.
- Klassifikationsmodelle liefern häufig Wahrscheinlichkeiten statt harter Entscheidungen.
- Der Threshold bestimmt die Klassenzuordnung und ist ein Hyperparameter.
- ROC-Kurve und AUC ermöglichen den Vergleich von Modellen über alle Thresholds hinweg.
- Die Wahl der Metrik hängt immer vom konkreten Anwendungsfall ab.

---

## Zeitplan

| Zeit | Inhalt |
|---:|---|
| 09:00 - 10:15 | Daily Review |
| 10:25 - 11:15 | Evaluierungsmetriken |
| 11:25 - 12:30 | Evaluierungsmetriken |
| 12:30 - 13:30 | Mittagspause |
| 13:30 - 16:00 | Übungen |
| 16:00 - 16:30 | Tägliches Stand-up |
| 16:30 - 18:00 | Übungen |

---

## Erste inhaltliche Notizen

### Evaluierungsmetriken
Es gibt verschiedene Varianten Modelle miteinander zu vergleichen und nicht jede ist bei jedem Modell die Richtige

---

## Lexikon

| Wording | Definition |
|---|---|
| Klassifikation | Ein Verfahren des überwachten Lernens, bei dem ein Modell Eingabedaten einer oder mehreren diskreten Klassen zuordnet, zum Beispiel „Spam“ oder „kein Spam“. |
| Binäre Klassifikation | Sonderform der Klassifikation mit genau zwei möglichen Klassen, häufig kodiert als positiv (1) und negativ (0). |
| Multiklassifikation | Klassifikationsproblem mit mehr als zwei sich gegenseitig ausschließenden Klassen, zum Beispiel die Einordnung eines Objekts in mehrere mögliche Kategorien. |
| Multilabel-Klassifikation | Klassifikationsform, bei der ein einzelner Input mehreren Klassen gleichzeitig zugeordnet werden kann, etwa bei Filmen mit mehreren Genres. |
| Regression | Ein Verfahren des überwachten Lernens, bei dem kontinuierliche numerische Werte vorhergesagt werden, zum Beispiel Temperatur oder Preis. |
| Konfusionsmatrix | Eine tabellarische Darstellung zur Bewertung von Klassifikationsmodellen, die die Anzahl wahrer und falscher positiver sowie negativer Vorhersagen gegenüberstellt. |
| True Positive (TP) | Ein Fall, in dem das Modell die positive Klasse korrekt vorhergesagt hat. |
| False Positive (FP) | Ein Fall, in dem das Modell fälschlicherweise die positive Klasse vorhergesagt hat, obwohl der wahre Wert negativ ist. |
| True Negative (TN) | Ein Fall, in dem das Modell die negative Klasse korrekt vorhergesagt hat. |
| False Negative (FN) | Ein Fall, in dem das Modell die positive Klasse nicht erkannt hat, obwohl sie tatsächlich vorliegt. |
| Accuracy | Der Anteil aller korrekten Vorhersagen an der Gesamtzahl der Vorhersagen; kann bei unausgewogenen Datensätzen irreführend sein. |
| Klassenungleichgewicht | Eine Situation, in der die Klassen im Datensatz stark unterschiedlich häufig vorkommen, was die Bewertung von Modellen erschwert. |
| Positive Klasse | Die Ziel- oder Fokusklasse einer Klassifikation, meist seltener und fachlich besonders relevant. |
| Negative Klasse | Die Gegenklasse zur positiven Klasse, oft häufiger im Datensatz vertreten. |
| Precision | Der Anteil korrekt vorhergesagter positiver Fälle an allen als positiv vorhergesagten Fällen; misst die Zuverlässigkeit positiver Vorhersagen. |
| Recall (Sensitivität) | Der Anteil korrekt erkannter positiver Fälle an allen tatsächlich positiven Fällen; misst, wie vollständig positive Fälle erkannt werden. |
| Specificity | Der Anteil korrekt erkannter negativer Fälle an allen tatsächlich negativen Fällen; Gegenstück zum Recall für die negative Klasse. |
| F1-Score | Das harmonische Mittel aus Precision und Recall; geeignet, wenn ein ausgewogenes Verhältnis zwischen beiden Metriken wichtig ist. |
| Harmonisches Mittel | Eine Mittelwertform, die kleine Werte stärker gewichtet als das arithmetische Mittel und daher empfindlich auf Ungleichgewichte reagiert. |
| Threshold (Schwellenwert) | Ein Grenzwert, ab dem eine vorhergesagte Wahrscheinlichkeit in eine Klassenentscheidung (positiv oder negativ) umgewandelt wird. |
| Hyperparameter | Modellparameter, die nicht aus den Trainingsdaten gelernt werden, sondern vom Anwender festgelegt werden, zum Beispiel der Threshold. |
| Hyperparametertuning | Der systematische Prozess zur Auswahl optimaler Hyperparameter, um die Modellleistung zu verbessern. |
| Sigmoidfunktion | Eine mathematische Funktion, die Werte auf einen Bereich zwischen 0 und 1 abbildet und häufig zur Modellierung von Wahrscheinlichkeiten genutzt wird. |
| ROC-Kurve | Eine Kurve zur Bewertung von Klassifikationsmodellen, die die True Positive Rate gegen die False Positive Rate für verschiedene Thresholds darstellt. |
| True Positive Rate (TPR) | Synonym für Recall; Anteil korrekt erkannter positiver Fälle an allen tatsächlich positiven Fällen. |
| False Positive Rate (FPR) | Anteil fälschlich als positiv klassifizierter negativer Fälle an allen tatsächlich negativen Fällen; definiert als 1 − Specificity. |
| AUC (Area Under the Curve) | Die Fläche unter der ROC-Kurve; misst die Trennschärfe eines Modells unabhängig vom Threshold. |
| Zufallsklassifikator | Ein Modell ohne Lernfähigkeit, dessen ROC-Kurve einer Diagonalen entspricht und eine AUC von 0,5 besitzt. |
| Modellbewertung | Der Prozess der quantitativen Beurteilung der Leistungsfähigkeit eines Modells anhand geeigneter Metriken. |
| Überwachtes Lernen | Ein Lernparadigma, bei dem Modelle anhand gelabelter Daten trainiert werden, das heißt mit bekannten Eingaben und Zielwerten. |
| Heuristik | Eine erfahrungsbasierte Entscheidungsregel, die keine optimale Lösung garantiert, aber in der Praxis oft sinnvoll ist. |

---

## Notizen

### Kleine Geschichte

Die Nichte ist in Schule. Dort erhält Sie Wettersticker als Bewertung. Eine Erklärung, wie das Wetter funktioniert musste also gegeben werden. Als sie wusste, wie das Wetter funktioniert, begann die Nichte das Wetter vorherzusagen. Sie sagt immer es wird regnen. Somit hat die Aussage immer gepasst, wenn es auch geregnet hat. An wie vielen Tagen die Vorhersage aber korrekt waren ist etwas anderes.

### Wann ist meine Vorhersage gut?
Es wird eine Bewertung benötigt, wie gut eine Aussage ist. Um dies zu bewerten muss man zunächst wissen welchen **Fehler** man zulassen kann.
Magie des ML: Modell nicht perfekt
Modell sagt nicht immer alles korrekt vorher
-> Fehler vorhanden
-> Fehler betrachten
-> Fehler verringern
-> Optimierung durch Fehler

### Einordnung und Lernkontext
Wir befinden uns weiterhin im Kontext des überwachten Lernens. Am Ende der Woche wurde die lineare Regression behandelt; heute liegt der Fokus auf Klassifikation. Ziel ist es zu verstehen, wie gut ein Modell funktioniert und wie wir diese Leistung systematisch bewerten können. Gerade bei Klassifikationsmodellen kann die Evaluation schnell zur Verzweiflung führen, obwohl die Grundidee intuitiv einfach ist.


### Klassifikation vs. Regression
Bei der Klassifikation ordnet ein Modell einem Input eine **diskrete Klasse** zu. Beispiele aus dem Alltag sind „gut gelaunt / nicht gut gelaunt“, „Tasse / Trinkflasche“ oder „Spam / kein Spam“. Es gibt binäre Klassifikation (zwei Klassen) und Multiklassifikation (mehr als zwei Klassen). Zudem können einem Input auch mehrere Klassen gleichzeitig zugeordnet werden, etwa bei Filmen oder Musikstücken mit mehreren Genres (Multilabel-Klassifikation).


Im Gegensatz dazu sagt die Regression einen **kontinuierlichen Wert** voraus, zum Beispiel die exakte Temperatur. Klassifikation wäre hier eine grobe Einteilung wie „warm“ oder „kalt“. Wenn jemand fragt: „Wie wird das Wetter?“, reicht oft die Klassifikation „warm“, auch wenn diese im Einzelfall falsch oder richtig sein kann.


### Die Konfusionsmatrix
Zur Bewertung von Klassifikationsmodellen wird häufig die Konfusionsmatrix (auch Verwirrungs- oder Fehlermatrix) verwendet. Ihr Ursprung liegt in der Psychologie der 1960er Jahre, wo untersucht wurde, wie Menschen unter Stress Klassifikationsfehler machen. Die Matrix hilft insbesondere bei binären Klassifikationen, Vorhersagen systematisch zu analysieren.
![Konfusionsmatrix](images/Konfusionsmatrix.png)


Man unterscheidet dabei eine **positive Klasse** (meist die seltenere oder besonders relevante, kodiert als 1) und eine **negative Klasse** (kodiert als 0).


### Accuracy und ihre Grenzen
Ein intuitives Maß ist die **Accuracy** (Trefferquote), definiert als:
> Anzahl korrekter Vorhersagen / Anzahl aller Vorhersagen.


Problematisch wird Accuracy bei **unausgewogenen Datensätzen**. Wenn z. B. Betrug sehr selten ist, kann ein Modell, das immer „kein Betrug“ vorhersagt, eine sehr hohe Accuracy haben, obwohl es praktisch nutzlos ist. Daher kann Accuracy stark irreführend sein.


### Precision und Recall
Um diese Schwächen auszugleichen, betrachtet man weitere Metriken:


- **Precision** misst den Anteil korrekter positiver Vorhersagen an allen als positiv vorhergesagten Fällen. Sie beantwortet die Frage: *Wie viele der vorhergesagten positiven Fälle waren tatsächlich positiv?*
Beispiel: „Ich habe oft Regen vorhergesagt – wie oft hat es wirklich geregnet?“


- **Recall** misst den Anteil korrekt erkannter positiver Fälle an allen tatsächlich positiven Fällen. Sie beantwortet die Frage: *Wie viele der tatsächlichen positiven Fälle habe ich erkannt?*
Beispiel: „Ich habe alle Regentage erwischt.“


In sensiblen Anwendungsfällen wie der Krebsdiagnose ist ein hoher Recall besonders wichtig, da übersehene positive Fälle gravierende Folgen haben können.


### F1-Score
Der **F1-Score** ist das harmonische Mittel aus Precision und Recall. Er ist besonders geeignet, wenn eine Balance zwischen beiden wichtig ist und weder zu viele falsche Positive noch zu viele falsche Negative akzeptabel sind. Da es sich um ein harmonisches und nicht um ein arithmetisches Mittel handelt, reagiert der F1-Score sehr sensibel auf Ungleichgewichte zwischen Precision und Recall.


Typische Anwendungsfälle sind Fraud Detection oder die Erkennung von Fake News, bei denen sowohl das Übersehen von Fehlern als auch falsche Anschuldigungen problematisch sind.


### Positive und negative Sichtweisen
Bisher wurde meist die positive Klasse betrachtet. In manchen Anwendungen ist jedoch auch die negative Perspektive entscheidend. Bei der Spam-Erkennung ist es zum Beispiel besonders kritisch, legitime E-Mails fälschlich als Spam zu klassifizieren. Welche Metrik sinnvoll ist, hängt daher stark vom Anwendungsfall ab.


### Entscheidungsgrenzen und Wahrscheinlichkeiten
Klassifikationsmodelle liefern häufig Wahrscheinlichkeiten statt harter Entscheidungen. Beispiel: Die Anzahl an Kaffeetassen pro Tag wird genutzt, um Schlaflosigkeit vorherzusagen. Bei weniger als einer Tasse ist die Wahrscheinlichkeit gering, bei 2,5 Tassen etwa 50 %, und ab fünf Tassen sehr hoch. Diese Beziehung wird oft durch eine Sigmoidfunktion modelliert.
![Sigmoidfunktion](images/Sigmoidfunktion.png)


Die eigentliche Klassifikation entsteht durch einen **Threshold**, ab dem eine Wahrscheinlichkeit als „positiv“ gilt. Dieser Schwellenwert kann verschoben werden und beeinflusst das Ergebnis stark.


### Threshold als Hyperparameter
Der Threshold ist ein **Hyperparameter**. Er wird nicht vom Modell gelernt, sondern von uns festgelegt – abhängig davon, wie risikofreudig oder vorsichtig wir sein möchten. Ein niedriger Threshold führt zu mehr Treffern, aber auch zu mehr Fehlalarmen; ein hoher Threshold reduziert Fehlalarme, verpasst aber möglicherweise relevante Fälle. Das bewusste Anpassen solcher Hyperparameter wird später im Kontext des Hyperparametertunings vertieft.


### ROC-Kurve und AUC
Die **ROC-Kurve** (Receiver Operating Characteristic) dient zum Vergleich von Klassifikationsmodellen über alle möglichen Thresholds hinweg. Sie stellt die True Positive Rate (Recall) gegen die False Positive Rate (1 − Specificity) dar.
![alt text](images/ROC.png)


Ein zufälliger Klassifikator entspricht der Diagonalen mit einer AUC (Area Under the Curve) von 0,5. Ein perfektes Modell erreicht eine AUC von 1. Reale Modelle liegen typischerweise zwischen 0,5 und 1. Die ROC-Kurve eignet sich gut zum Modellvergleich, zeigt aber nicht immer das ganze Bild.


### Einschränkungen der ROC-Kurve
Bei stark unausgewogenen Klassen kann die ROC-Kurve irreführend sein. In solchen Fällen ist eine Precision-Recall-Kurve oft aussagekräftiger. Generell gilt: Keine einzelne Metrik ist universell optimal.


### Auswahl der richtigen Metrik
Welche Metrik sinnvoll ist, hängt vom konkreten Problem ab. Zentrale Fragen sind:
- Welcher Fehler ist akzeptabel?
- Welche Klasse ist besonders wichtig?
- Was soll bestätigt oder vermieden werden?


Es gibt keine algorithmisch eindeutige Antwort, sondern nur heuristische Entscheidungen.


### Anwendungsbeispiele
Bei selbstfahrenden Autos ist ein hoher Recall für relevante Objekte entscheidend, um Sicherheitsabstände einzuhalten. In Dating-Apps geht es darum, Fehlmatches zu reduzieren, ohne potenziell gute Matches zu verlieren. Diese Beispiele zeigen, dass man das Problem verstehen muss, bevor man die Modellleistung sinnvoll bewerten kann.


### Fazit
Die Bewertung von Klassifikationsmodellen erfordert ein tiefes Verständnis des Anwendungsfalls. Accuracy allein reicht selten aus. Stattdessen sollten mehrere Metriken betrachtet und gegeneinander abgewogen werden, um fundierte Entscheidungen über die Modellqualität zu treffen.