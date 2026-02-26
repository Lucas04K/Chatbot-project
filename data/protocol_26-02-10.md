# Tag 16, 10.02.2026

### Grundlagen des Deep Learning

---

# Lexikon

| Begriff                            | Definition                                                                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| AdaGrad                            | Optimierungsalgorithmus mit adaptiver Lernrate pro Parameter; besonders geeignet für Sparse-Daten (z. B. NLP).                      |
| Adam (Adaptive Moment Estimation)  | Optimierer, der Momentum und adaptive Lernraten kombiniert; robust und heute weit verbreitet.                                       |
| Aktivierungsfunktion               | Nichtlineare Funktion, die auf die gewichtete Summe eines Neurons angewendet wird (z. B. ReLU, Sigmoid, Tanh, GeLU).                |
| Backpropagation                    | Algorithmus zur Berechnung der Gradienten aller Gewichte mithilfe der Kettenregel; Grundlage des Trainings neuronaler Netze.        |
| Batch                              | Teilmenge der Trainingsdaten, die in einem Optimierungsschritt verarbeitet wird.                                                    |
| Binary Cross Entropy               | Verlustfunktion für binäre Klassifikation; misst die Abweichung zwischen vorhergesagter Wahrscheinlichkeit und tatsächlichem Label. |
| Co-Adaptation                      | Unerwünschte starke Abhängigkeit zwischen Neuronen; reduziert durch Dropout.                                                        |
| CNN (Convolutional Neural Network) | Neuronales Netz mit Faltungsschichten; besonders geeignet für Bild- und Signalverarbeitung.                                         |
| Dense Layer                        | Vollständig verbundene Schicht, in der jedes Neuron mit allen Neuronen der vorherigen Schicht verbunden ist.                        |
| Dropout                            | Regularisierungsmethode, bei der während des Trainings zufällig Neuronen deaktiviert werden, um Overfitting zu reduzieren.          |
| Early Stopping                     | Abbruch des Trainings, wenn der Validierungsfehler steigt; dient der Vermeidung von Overfitting.                                    |
| Epoche                             | Ein vollständiger Durchlauf durch den gesamten Trainingsdatensatz.                                                                  |
| Exploding Gradients                | Problem bei tiefen Netzen, bei dem Gradienten sehr groß werden und das Training instabil machen.                                    |
| Forward Pass                       | Vorwärtsdurchlauf durch das Netzwerk zur Berechnung der Vorhersage.                                                                 |
| GeLU                               | Aktivierungsfunktion auf Basis der Gaußverteilung; häufig in Transformer-Modellen verwendet.                                        |
| Gradient                           | Vektor partieller Ableitungen; gibt Richtung und Stärke der stärksten Zunahme einer Funktion an.                                    |
| Gradient Descent                   | Optimierungsverfahren zur Minimierung einer Funktion durch iterative Anpassung entlang des negativen Gradienten.                    |
| Grid Search                        | Systematische Hyperparameter-Optimierung durch vollständiges Durchprobieren definierter Kombinationen.                              |
| Hidden Layer                       | Zwischenschicht eines neuronalen Netzes zwischen Input- und Output-Layer.                                                           |
| Hochreiter (1991)                  | Beschrieb formal das Vanishing-Gradient-Problem in tiefen neuronalen Netzen.                                                        |
| Hyperparameter                     | Konfigurationsparameter, die nicht gelernt, sondern vor dem Training festgelegt werden (z. B. Lernrate, Batchgröße).                |
| Initialisierung                    | Festlegung der Startwerte der Gewichte; beeinflusst Konvergenz und Stabilität des Trainings.                                        |
| Keras                              | High-Level-API von TensorFlow zur schnellen Implementierung neuronaler Netze.                                                       |
| Kettenregel                        | Mathematische Ableitungsregel für verschachtelte Funktionen; Grundlage der Backpropagation.                                         |
| Lernrate                           | Skalierungsfaktor für den Gradienten beim Gewichtsupdate; einer der wichtigsten Hyperparameter.                                     |
| Loss-Funktion                      | Maß für die Abweichung zwischen Vorhersage und Zielwert (z. B. MSE, Cross Entropy).                                                 |
| Mini-Batch                         | Teilmenge der Trainingsdaten, auf deren Basis ein Update durchgeführt wird.                                                         |
| Momentum                           | Erweiterung von Gradient Descent, die vorherige Updates berücksichtigt, um Plateaus zu überwinden.                                  |
| MSE (Mean Squared Error)           | Mittlerer quadratischer Fehler; typische Verlustfunktion für Regression.                                                            |
| Neuron                             | Grundelement eines neuronalen Netzes; berechnet gewichtete Summe der Eingaben und wendet Aktivierungsfunktion an.                   |
| Neural Network (NN)                | Modell aus verbundenen Neuronen zur Approximation komplexer Funktionen.                                                             |
| Optimizer                          | Algorithmus zur Anpassung der Gewichte basierend auf Gradienten (z. B. SGD, Adam, AdaGrad).                                         |
| Overfitting                        | Modell passt sich zu stark an Trainingsdaten an und generalisiert schlecht auf neue Daten.                                          |
| Perceptron                         | Einfachstes neuronales Modell mit linearer Entscheidungsgrenze; kann XOR nicht lösen.                                               |
| Production                         | Einsatz eines trainierten Modells in realen Anwendungen.                                                                            |
| PyTorch                            | Deep-Learning-Framework mit dynamischem Rechenmodell; besonders beliebt in Forschung und Prototyping.                               |
| Random Search                      | Hyperparameter-Optimierung durch zufällige Kombinationen innerhalb definierter Bereiche.                                            |
| ReLU                               | Aktivierungsfunktion f(x)=max(0,x); Standard in Hidden Layers moderner Netze.                                                       |
| Regularisierung                    | Methoden zur Reduktion von Overfitting (z. B. Dropout, Early Stopping).                                                             |
| Regression                         | Vorhersage kontinuierlicher Zielwerte.                                                                                              |
| RNN (Recurrent Neural Network)     | Netzwerk mit rekurrenten Verbindungen zur Verarbeitung sequenzieller Daten.                                                         |
| Sigmoid                            | Aktivierungsfunktion mit Wertebereich (0,1); häufig im Output-Layer bei binärer Klassifikation.                                     |
| Sparse Daten                       | Daten mit vielen Null- oder selten auftretenden Features (typisch in NLP).                                                          |
| Tanh                               | Aktivierungsfunktion mit Wertebereich (-1,1); nullzentriert, aber anfällig für Vanishing Gradients.                                 |
| TensorFlow                         | Deep-Learning-Framework mit Fokus auf Skalierbarkeit und Produktionsumgebungen.                                                     |
| Transformer                        | Architektur für Sequenzverarbeitung mit Attention-Mechanismus; Standard in modernen NLP-Modellen.                                   |
| Vanishing Gradients                | Problem, bei dem Gradienten sehr klein werden und frühe Netzwerkschichten kaum lernen.                                              |
| Validierungsdaten                  | Datensatz zur Bewertung der Generalisierungsfähigkeit während des Trainings.                                                        |

---

## **Grundlegender Überblick**

- Backpropagation basiert auf der **Kettenregel**
- Aktivierungsfunktion beeinflusst Gradientendynamik
- Vanishing/Exploding Gradients sind zentrale Probleme
- Hyperparameter bestimmen Trainingsverhalten stark
- Adam ist Standardoptimierer
- Dropout zentrale Regularisierungsmethode
- TensorFlow & PyTorch beide relevant
- Trend geht zu vortrainierten Modellen

---

## 1. PyTorch vs. TensorFlow

### TensorFlow

- Häufig in **Production-Umgebungen**
- Stark skalierbar (Google Cloud, Browser, Mobile)
- Mit **Keras** sehr schnell Prototypen entwickelbar
- High-Level-API für schnelles Testen

### PyTorch

- Sehr beliebt in **Forschung und experimentellen Anwendungen**
- Python-nahe, intuitive Syntax
- Häufig in NLP-Projekten (z. B. Hugging Face)
- Flexibler im Prototyping

### Fazit

Beide Frameworks sind relevant.

- **TensorFlow** → häufiger in Produktion
- **PyTorch** → stärker in Forschung & Prototyping
  Kenntnisse in beiden sind vorteilhaft.

Trend: **Vortrainierte Modelle** (z. B. Hugging Face).
Viele Modelle lösen Aufgaben, auf die sie nicht explizit trainiert wurden.

---

# 2. Historischer Kontext: Perceptron & Backpropagation

## XOR-Problem & KI-Winter

- Das **Perceptron** kann das XOR-Problem nicht lösen.
- Dies führte zum ersten **KI-Winter**.
- Kurz nach Veröffentlichung:
  - Ein finnischer Forscher beschreibt in seiner Masterarbeit die Kombination von Perceptrons mit **Backpropagation**.
  - Arbeit war auf Finnisch → kaum beachtet.
  - Später erneut publiziert, aber schlecht platziert.
  - **16 Jahre später** Veröffentlichung in _Nature_ → große Aufmerksamkeit.

### Zentrale Frage:

Warum wurde die kombinierte Lösung nicht früher erkannt?

---

# 3. Backpropagation – Einfaches Beispiel

## Vorhersage

Gegeben:

- Input: ( i = 1,5 )
- Gewicht: ( w_0 = 0,8 )
- Output:

$$
a = i \cdot w_0
$$

$$
a = 1{,}5 \cdot 0{,}8 = 1{,}2
$$

## Tatsächlicher Wert

$$
y = 0{,}5
$$

## Fehlerfunktion (MSE)

$$
C = (a - y)^2
$$

Ziel:

$$
C \rightarrow \min
$$

---

## Ableitungen

### 1. Ableitung nach (a)

$$
\frac{\partial C}{\partial a} = 2(a - y)
$$

### 2. Kettenregel

$$
\frac{\partial C}{\partial w} =
\frac{\partial a}{\partial w} \cdot
\frac{\partial C}{\partial a}
$$

Da:

$$
a = i w
\Rightarrow
\frac{\partial a}{\partial w} = i
$$

Also:

$$
\frac{\partial C}{\partial w} = i \cdot 2(iw - y)
$$

Einsetzen:

$$
1{,}5 \cdot (2(1{,}5w) - 1)
$$

$$
= 4{,}5w - 1{,}5
$$

---

## Update-Regel (Gradient Descent)

Lernrate:

$$
\eta = 0{,}1
$$

$$
w_{neu} = w_{alt} - \eta \cdot \frac{\partial C}{\partial w}
$$

| w₀    | w₁     |
| ----- | ------ |
| 0,8   | 0,59   |
| 0,59  | 0,474  |
| 0,474 | 0,41   |
| ...   | 0,3333 |

→ Konvergenz gegen optimales Gewicht.

**Hinweis:**

- Lernrate moderat wählen
- Anpassung durch Optimizer (nicht manuell)

---

# 4. Aktivierungsfunktionen

![Aktivierungsfunktionen](https://ml-explained.com/articles/activation-functions-explained/Activation_Functions.png)

## Sigmoid

$$
a = \frac{1}{1 + e^{-iw}}
$$

- Wertebereich: (0,1)
- Problem: **Vanishing Gradients**
- Meist nur im **Output-Layer** bei Klassifikation

---

## ReLU (Standard in Hidden Layers)

$$
f(x) =
\begin{cases}
x & x > 0 \\
0 & x \le 0
\end{cases}
$$

- Kein Vanishing bei positiven Werten
- Problem: „Dead Neurons“

---

## Tanh

- Nullzentriert
- Ebenfalls Vanishing-Problem
- Training oft stabiler als Sigmoid

---

## GeLU

- Verwendet in **Transformern**
- Gauß-basierte Aktivierung

---

## Regression

- Meist **keine Output-Aktivierung**

---

# 5. Vanishing & Exploding Gradients

Problem:

- Gradienten verschwinden oder explodieren
- Besonders bei tiefen Netzwerken

Formalisiert durch:
**Hochreiter (1991)**

Ursache:

- Multiplikation vieler kleiner oder großer Werte
- Abhängig von Initialisierung und Aktivierungsfunktion

---

# 6. Architekturtypen

- **Dense NN** → Vollständig verbunden
- **CNN** → Feste Faltungsstruktur
- **RNN** → Rekurrente Struktur

Teilweise fixe Struktur, teilweise frei konfigurierbar.

---

# 7. Hyperparameter

Definition:
Parameter, die **nicht gelernt**, sondern vom Nutzer festgelegt werden.

## Wichtige Hyperparameter

- **Lernrate** (sehr wichtig)
- **Anzahl Schichten**
- **Neuronen pro Schicht**
- **Feature-Anzahl**
- **Mini-Batch-Größe**
  - Eine Epoche = alle Batches einmal durchlaufen

- **Optimierungsalgorithmus**

---

## Optimierer

### Adam (Adaptive Moment Estimation)

- Sehr populär
- Adaptive Lernrate pro Parameter
- Momentum-Effekt (Plateaus überwinden)

### AdaGrad

- Gut für NLP / Sparse Daten
- Häufig aktualisierte Parameter → größere Lernraten

---

# 8. Hyperparameter-Optimierung

## Grid Search

- Systematisches Durchprobieren
- Nachvollziehbar
- Sehr rechenintensiv
- Beispiel: 4 Parameter × 3 Werte → 81 Kombinationen

## Random Search

- Zufällige Auswahl in definierten Bereichen
- Oft effizienter
- Kein Lernen aus vorherigen Versuchen
- Weniger reproduzierbar

### Praxis:

- Grobe → feine Suche
- Oft zuerst Lernrate optimieren

Gradient Descent nicht direkt anwendbar, da kein kontinuierlicher Zusammenhang.

---

# 9. Regularisierung

Ziel:

- **Overfitting vermeiden**
- Keine Co-Adaptation von Neuronen

## Dropout

- Zufälliges Deaktivieren von Neuronen während Training
- Erhöht Robustheit
- Verhindert Abhängigkeiten

Beispiel:

- Ein Neuron erkennt Schnurrhaare
- Ein anderes Ohren
- Modell soll Katze auch ohne Schnurrhaare erkennen

Dropout meist wichtiger als Early Stopping.

---

## Early Stopping

Beobachtung:

- Trainingsverlust sinkt
- Validierungsverlust steigt

→ Modell overfitted

Training wird gestoppt.

Wirkt sowohl als Regularisierung als auch Optimierungskontrolle.
