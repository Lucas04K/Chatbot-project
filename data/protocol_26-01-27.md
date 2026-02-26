# Tag 07, 27.10.2023

Logistische Regression

---

## Grundlegender Überblick

- **Überwachtes Lernen**: Nutzt gelabelte Daten zur Modellbildung.
- **Klassifikation vs. Regression**:
  - Klassifikation ordnet Eingaben diskreten Klassen zu (z.B. Spam/kein Spam).
  - Regression sagt kontinuierliche Werte voraus (z.B. Temperatur, Preis).
- **Klassifikationsarten**:
  - Binär: Zwei Klassen (z.B. traurig/glücklich).
  - Multiklassig: Mehr als zwei Klassen (z.B. Katze/Hund/Krokodil).
  - Multilabel: Ein Input kann mehreren Klassen zugeordnet werden (z.B. Filmgenres).
- **Evaluierungsmetriken**:
  - Konfusionsmatrix: True/False Positives/Negatives.
  - Accuracy: Anteil korrekter Vorhersagen (irreführend bei unausgewogenen Daten).
  - Precision: Anteil korrekter positiver Vorhersagen.
  - Recall: Anteil erkannter positiver Fälle.
  - F1-Score: Harmonisches Mittel aus Precision und Recall.
- **Wahrscheinlichkeiten & Threshold**:
  - Klassifikationsmodelle liefern oft Wahrscheinlichkeiten (z.B. Sigmoid-Funktion).
  - Threshold bestimmt die Klassenzuordnung (Hyperparameter).
- **ROC-Kurve & AUC**:
  - ROC-Kurve: True Positive Rate vs. False Positive Rate.
  - AUC: Fläche unter der ROC-Kurve (0,5 = Zufall, 1 = perfekt).
- **Anwendungsabhängige Metriken**:
  - Wahl der Metrik hängt vom Problem ab (z.B. Recall bei Krebsdiagnose).

---

## Erste inhaltliche Notizen
Die logistische Regression ist ein Klassifikationsverfahren, das Wahrscheinlichkeiten für die Zugehörigkeit zu einer Klasse berechnet. Im Gegensatz zur linearen Regression, die kontinuierliche Werte vorhersagt, gibt die logistische Regression diskrete Klassenausgaben (z.B. 0 oder 1). Sie wird häufig für binäre Klassifikationsprobleme eingesetzt, kann aber auch auf Multiklass-Probleme erweitert werden.

---

## Zeitplan

|          Zeit | Inhalt |
|--------------:|---|
| 09:00 - 10:15 | Daily Review |
| 10:15 - 11:00 | Logistische Regression Grundlagen |
| 11:15 - 12:00 | Sigmoid-Funktion und Verlustfunktionen |
| 12:30 - 13:30 | Mittagspause |
| 13:30 - 16:00 | Übungen zur logistischen Regression |
| 16:00 - 16:30 | Tägliches Stand-up |
| 16:30 - 18:00 | Vertiefung und Anwendungsbeispiele |

---

## Lexikon

| Wording | Definition |
|---|---|
| Klassifikation | Ein Verfahren des überwachten Lernens, bei dem ein Modell Eingabedaten einer oder mehreren diskreten Klassen zuordnet, zum Beispiel „Spam“ oder „kein Spam“. |
| Binäre Klassifikation | Sonderform der Klassifikation mit genau zwei möglichen Klassen, häufig kodiert als positiv (1) und negativ (0). |
| Multiklassifikation | Klassifikationsproblem mit mehr als zwei sich gegenseitig ausschließenden Klassen. |
| Multilabel-Klassifikation | Klassifikationsform, bei der ein einzelner Input mehreren Klassen gleichzeitig zugeordnet werden kann. |
| Regression | Ein Verfahren des überwachten Lernens, bei dem kontinuierliche numerische Werte vorhergesagt werden. |
| Sigmoid-Funktion | Mathematische Funktion, die Werte auf einen Bereich zwischen 0 und 1 abbildet. |
| Logistische Regression | Klassifikationsmodell, das die Sigmoid-Funktion zur Berechnung von Wahrscheinlichkeiten verwendet. |
| Verlustfunktion | Mathematische Funktion, die die Abweichung zwischen Vorhersagen und tatsächlichen Werten misst. |
| Gradient Descent | Optimierungsverfahren zur Minimierung der Verlustfunktion durch iterative Anpassung der Modellparameter. |
| Threshold | Grenzwert, ab dem eine vorhergesagte Wahrscheinlichkeit in eine Klassenentscheidung umgewandelt wird. |
| ROC-Kurve | Grafische Darstellung der True Positive Rate gegen die False Positive Rate für verschiedene Thresholds. |
| AUC | Fläche unter der ROC-Kurve, misst die Trennschärfe eines Modells. |

---

## Notizen

### Zusammenfassung der heutigen Inhalte
Die Vorlesung behandelte die logistische Regression als Methode für binäre Klassifikation, insbesondere im Kontext von Sentiment-Analyse. Es wurden die Herausforderungen der linearen Regression für Klassifikationsprobleme aufgezeigt und die Sigmoid-Funktion als Lösung eingeführt. Zudem wurde die historische Bedeutung der logistischen Regression in der medizinischen Statistik (Herzinfarkt-Risiko) betont.

### Detaillierte Notizen

#### Klassifikation vs. Regression
- **Klassifikation**: Zuordnung von Eingaben zu diskreten Klassen (z.B. Spam/kein Spam, traurig/glücklich).
- **Regression**: Vorhersage kontinuierlicher Werte (z.B. Temperatur, Preis).
- Beispiel: Sentimentanalyse basierend auf negativen Wörtern und Smileys.

#### Lineare Regression für Klassifikation
- Problem: Lineare Regression liefert kontinuierliche Werte, nicht binäre Klassen.
- Beispiel mit negativen Wörtern:
  - Lineare Regression könnte Vorhersagen wie 0,3 oder 1,2 liefern.
  - Threshold bei 0,5: Werte >0,5 als "negativ" klassifiziert.
- Herausforderung: Ausreißer (z.B. 30 negative Wörter) verschieben die Entscheidungsgrenze drastisch.

#### Sigmoid-Funktion als Lösung
- **Sigmoid-Funktion**: Wandelt beliebige Werte in Wahrscheinlichkeiten zwischen 0 und 1 um.
- Eigenschaften:
  - Asymptotisch gegen 0 und 1 bei ±∞.
  - Stabiler gegenüber Ausreißern als lineare Regression.

#### Mathematische Grundlagen
- **Logistische Regression**:
  $ P(y=1|x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}} $
- **Verlustfunktion (binäre Kreuzentropie)**:
  $ L = -\frac{1}{N} \sum_{i=1}^N [y_i \log(p_i) + (1-y_i) \log(1-p_i)] $
- **Gradient Descent**: Iterative Anpassung der Parameter $\beta_0, \beta_1$ zur Minimierung des Verlusts.

#### Beispiel: Sentimentanalyse
- Features:
  - Anzahl negativer Wörter ($x_1$).
  - Anzahl trauriger Smileys ($x_2$).
- Entscheidungsgrenze:
  $ \beta_0 + \beta_1 x_1 + \beta_2 x_2 = 0 $
- Beispiel: Bei $x_1 + x_2 \geq 3$ wird der Text als "traurig" klassifiziert.

### Fazit
Die logistische Regression ist ein mächtiges Werkzeug für Klassifikationsprobleme, insbesondere wenn es um die Vorhersage von Wahrscheinlichkeiten geht. Im Vergleich zur linearen Regression bietet sie den Vorteil, dass sie direkt diskrete Klassenausgaben liefert und stabiler gegenüber Ausreißern ist. Die Sigmoid-Funktion spielt dabei eine zentrale Rolle, indem sie beliebige Werte in Wahrscheinlichkeiten zwischen 0 und 1 umwandelt. Die Verlustfunktion (binäre Kreuzentropie) und der Gradient Descent sind essentiell für das Training des Modells. In der Praxis ist es wichtig, den richtigen Threshold zu wählen und die Modellleistung mit Metriken wie Precision, Recall und F1-Score zu bewerten.
