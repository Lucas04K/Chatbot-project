# Tag 11, 02.02.2026 – Bias-Varianz-Kompromiss & Regularisierung

---

## **Grundlegender Überblick**

* Zusammenhang zwischen Modellkomplexität und Generalisierung
* Bias–Varianz-Kompromiss als zentrales Diagnosewerkzeug
* Underfitting vs. Overfitting
* Rolle von Trainings- und Testfehlern
* Regularisierung als Methode zur Kontrolle der Modellkomplexität
* L1- und L2-Regularisierung (Lasso & Ridge)
* Einfluss des Regularisierungsparameters

---

## **Zeitplan**

|          Zeit | Inhalt                                        |
| ------------: | --------------------------------------------- |
| 09:00 – 10:00 | Daily Review                                  |
| 10:00 – 12:00 | Bias–Varianz-Kompromiss (Theorie & Intuition) |
| 12:00 – 13:00 | Mittagspause                                  |
| 13:00 – 16:00 | Regularisierung (Notebooks & Beispiele)       |
| 16:00 – 16:30 | Tägliches Stand-up                            |
| 16:30 – 18:00 | Vertiefung                                    |

---

## **Haupt Take-Away**

Gute Machine-Learning-Modelle entstehen aus einem **Kompromiss zwischen Bias und Varianz**. Zu einfache Modelle können die Datenstruktur nicht erfassen (Underfitting), zu komplexe Modelle passen sich zu stark an die Trainingsdaten an (Overfitting). Regularisierung ist ein zentrales Werkzeug, um diesen Kompromiss gezielt zu steuern, indem Modellkomplexität kontrolliert und Generalisierungsfähigkeit verbessert wird.

---

## **Notizen**

### Bias–Varianz-Kompromiss

**Bias (Verzerrung):**

* Fehler durch zu starke Vereinfachung des Modells
* Modell ist nicht flexibel genug
* Typisch für **Underfitting**

**Varianz:**

* Fehler durch starke Abhängigkeit vom Trainingsdatensatz
* Modell reagiert empfindlich auf kleine Datenänderungen
* Typisch für **Overfitting**

**Zentrale Erkenntnis:**

* Steigende Modellkomplexität ↓ Bias, aber ↑ Varianz
* Sinkende Modellkomplexität ↑ Bias, aber ↓ Varianz
* Ziel ist ein Bereich minimalen Testfehlers

**Trainings- vs. Testfehler:**

* Trainingsfehler sinkt meist monoton mit steigender Komplexität
* Testfehler zeigt typischerweise eine U-Form
* Minimum des Testfehlers entspricht dem optimalen Kompromiss

---

### Underfitting vs. Overfitting

**Underfitting:**

* Modell zu einfach
* Hoher Trainings- und Testfehler
* Relevante Muster werden nicht gelernt

**Overfitting:**

* Modell zu komplex
* Sehr niedriger Trainingsfehler
* Hoher Testfehler
* Modell lernt Rauschen statt Struktur

---

### Regularisierung

**Motivation:**

* Reduktion der effektiven Modellkomplexität
* Verbesserung der Generalisierungsfähigkeit

**Prinzip:**

* Erweiterung der Verlustfunktion um einen Strafterm
* Große Gewichte werden bestraft

**L2-Regularisierung (Ridge):**

* Bestraft die quadrierte Größe der Gewichte
* Führt zu kleinen, stabilen Gewichten
* Reduziert Varianz ohne vollständige Feature-Elimination

**L1-Regularisierung (Lasso):**

* Bestraft die absolute Größe der Gewichte
* Führt zu sparsamen Modellen
* Kann Gewichte exakt auf 0 setzen (implizite Feature Selection)

**Regularisierungsparameter α:**

* Kontrolliert Stärke der Regularisierung
* Kleines α → hohe Modellkomplexität
* Großes α → stark vereinfachtes Modell

---

### Zusammenhang Bias–Varianz & Regularisierung

* Regularisierung erhöht bewusst den Bias
* Gleichzeitig wird die Varianz reduziert
* Ziel: Senkung des Testfehlers durch besseren Kompromiss

---

## **Praktische Hinweise**

### Kombination: Polynomiale Features + Regularisierung

Polynomiale Features und Regularisierung lassen sich sinnvoll kombinieren:

| Technik              | Effekt                                         |
| -------------------- | ---------------------------------------------- |
| Polynomiale Features | Erhöht Modellflexibilität (Overfitting-Risiko) |
| Ridge / Lasso        | Reduziert effektive Komplexität                |

**Vorteile der Kombination:**

* Flexibilität für nicht-lineare Zusammenhänge
* Schutz vor Overfitting durch Regularisierung
* Lasso kann unnötige Polynomterme automatisch eliminieren

**Typische Pipeline:**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge

model = Pipeline([
    ('poly', PolynomialFeatures(degree=3)),
    ('ridge', Ridge(alpha=1.0))
])
```

---

### Skalierung vor Regularisierung

**Wichtig:** Ridge und Lasso skalieren Features **nicht** automatisch.

**Problem ohne Skalierung:**

* Features mit unterschiedlichen Skalen erhalten unterschiedlich große Koeffizienten
* Regularisierung bestraft alle Koeffizienten gleich → unfaire Bestrafung
* Koeffizientengröße spiegelt nicht die tatsächliche Feature-Wichtigkeit wider

**Lösung:** Immer vor Regularisierung skalieren

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

model = Pipeline([
    ('scaler', StandardScaler()),
    ('ridge', Ridge(alpha=1.0))
])
```

**Nach Skalierung:**

* Alle Features haben Mittelwert = 0 und Standardabweichung = 1
* Koeffizienten werden vergleichbar
* Regularisierung wirkt fair auf alle Features

---

## **Lexikon**

| Begriff                 | Definition                                              |
| ----------------------- | ------------------------------------------------------- |
| Bias                    | Fehler durch zu einfache Modellannahmen                 |
| Varianz                 | Fehler durch hohe Sensitivität gegenüber Trainingsdaten |
| Bias–Varianz-Kompromiss | Zielkonflikt zwischen Einfachheit und Flexibilität      |
| Underfitting            | Modell ist zu einfach                                   |
| Overfitting             | Modell ist zu komplex                                   |
| Regularisierung         | Kontrolle der Modellkomplexität                         |
| L1-Regularisierung      | Fördert sparsame Modelle                                |
| L2-Regularisierung      | Schrumpft Gewichte und stabilisiert Modelle             |
| Trainingsfehler         | Fehler auf den Trainingsdaten                           |
| Testfehler              | Fehler auf unbekannten Daten                            |
| StandardScaler          | Transformiert Features auf Mittelwert=0, Std=1          |

---


