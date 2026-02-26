# Tag 25, 20.02.2026

# Einführung Recommender Systems

### __Grundlegender Überblick__

* Was ist ein Recommender-System?
* Inhaltsbasierte Filter vs. Kollaborative Filter
* Ähnlichkeitsmatrixen
* Singulärwertzerlegung
* Evaluation von Recommender-Systemen

---
## Tesco 
Beim Supermarkt Tesco wurden Einkaufsdaten aus dem Clubcard-Programm analysiert, um Kaufmuster zu erkennen. Wenn Kundinnen zum Beispiel plötzlich Folsäure oder bestimmte Pflegeprodukte kauften, konnte ein Algorithmus daraus eine mögliche Schwangerschaft ableiten. Anschließend wurden gezielt Gutscheine oder Werbung für Babyprodukte verschickt.

## Haupt-Takeaway
Empfehlungssysteme personalisieren Inhalte durch zwei grundlegende Ansätze: Inhaltsbasierte Filter (was ähnelt dem, was mir gefällt?) und Kollaborative Filter (was mögen ähnliche Nutzer?). Der entscheidende Durchbruch kam durch Matrixfaktorisierung (SVD), die verborgene Präferenzmuster automatisch aus Bewertungsdaten lernt – ohne dass man eine Merkmalskategorie manuell definieren muss. Die Kosinus-Ähnlichkeit ist dabei das robusteste Maß für hochdimensionale Daten.

*Beispiele: Netflix, YouTube, Amazon, Spotify*

## Arten von Feedback: Implizite vs. explizite Daten
Recommender Systems unterscheiden grundsätzlich zwischen zwei Typen von Nutzerdaten:
- Explizit: Direkt vom Nutzer gegebenes Feedback
- Implizit: Aus dem Nutzerverhalten abgeleitetes Feedback 

| **Arten der Daten** | **Filme** | **Fische** |
|---------------------|-----------|------------|
| Explizit            | Sternenbewertung, Like/Dislike | Bewertung, Lieblingsfisch auswählen |
| Implizit            | Gesehene Filme, Dauer, Pausen, Klicks | Geklickte Fischarten, Kaufhistorie, Produktaufrufe | 

> Hinweis: Implizite Daten sind häufiger verfügbar, aber schwieriger zu interpretieren, da ein Klick nicht zwingend Interesse bedeutet.


## Typen von Recommender Systemen

### Inhaltsbasiertes Filtern
Empfiehlt Elemente, die den Merkmalen eines vom Nutzer bereits gemochten Artikels ähneln.

*Beispiel: Ein Buch aus demselben Genre wie das zuletzt gekaufte.*

### Kollaboratives Filtern (Collaborative Filtering)
Empfiehlt Artikel basierend auf dem **Verhalten ähnlicher Nutzer** – ohne die Inhalte der Artikel selbst zu kennen.

| Typ | Grundidee |
|---|---|
| Benutzerbasiert | Nutzer mit ähnlichem Bewertungsverhalten werden verglichen |
| Elementbasiert | Artikel mit ähnlichen Bewertungsmustern werden verglichen |

## Ähnlichkeitsmatrixen
**Ähnlichkeitsmaße:**
Ähnlichkeitsmaße werden bei beiden Ansätzen eingesetzt.

| Maß | Beschreibung |
|---|---|
| Euklidischer Abstand | Misst die geometrische Distanz zweier Vektoren |
| Pearson-Korrelation | Misst den linearen Zusammenhang zweier Variablen |
| Kosinus-Ähnlichkeit | Misst den Winkel zwischen zwei Vektoren – am häufigsten verwendet |

> Die Kosinusähnlichkeit ist bei hochdimensionalen Daten (viele Items/User) besser geeignet als z.B. euklidische Distanz, weil sie nicht durch die Länge der Vektoren beeinflusst wird — nur durch die Richtung. 

Die **Kosinusähnlichkeit** zwischen zwei Vektoren:

$$
  CosSim(x,y) = \frac{\sum_{i}x_{i}y_{i}}{\sqrt{\sum_{i}x_{i}^2}\sqrt{\sum_{i}y_{i}^2}}
$$

***Interpretation:***
- 0: Keine Ähnlichkeit (orthogonal)
- 1: Sehr ähnliche Vektoren
- -1: Entgegengesetzt (selten im Farbraum)


**Ähnlichkeitsmatrix mit Kosinusähnlichkeiten**

|              | **Fisch 1** | **Fisch 2** | **Fisch 3** | **Fisch 4** |
|--------------|-------------|-------------|-------------|-------------|
| **Fisch 1**  |     1       |    0.57     |     0       |    0.82     |
| **Fisch 2**  |    0.57     |     1       |     0       |    0.71     |
| **Fisch 3**  |     0       |     0       |     1       |     0       |
| **Fisch 4**  |    0.82     |    0.71     |     0       |     1       |

Fisch 3 hat zu allen anderen Fischen eine Ähnlichkeit von 0 – er ist vollständig orthogonal, also in keiner Eigenschaft vergleichbar.

### Singulärwertzerlegung

| Nutzer / Artikel | Fisch 1 | Fisch 2 | Fisch 3 | Fisch 4 | Fisch 5 |
|---|---|---|---|---|---|
| **Marinka** | 5 | 4 | – | 2 | – |
| **Benutzer 2** | – | 3 | 5 | – | 4 |
| **Benutzer 3** | 2 | – | 4 | 5 | – |
| **Benutzer 4** | – | 5 | – | 3 | 1 |

> Die meisten Einträge fehlen (–) – das ist typisch für reale Daten. Kein Nutzer bewertet alle Artikel.

**Singulärwertzerlegung (SVD):**
Die Grundidee: Eine große Nutzer-Artikel-Bewertungsmatrix wird in kleinere Matrizen zerlegt, die **latente (verborgene) Faktoren** repräsentieren.

$$
R \approx U \cdot \Sigma \cdot V^T
$$

- **R** - Rating-Matrix
- **U** – Nutzer-Merkmalsmatrix
- **Σ** – Singulärwerte (Gewichtung der Faktoren)
- **V^T** – Artikel-Merkmalsmatrix

> Was sind latente Faktoren? Das Modell lernt automatisch Muster wie z.B. „Nutzer, die Fisch 2 mögen, mögen auch Fisch 3" – ohne dass wir ihm sagen, *warum*. Das Modell arbeitet nicht mit Labels, sondern mit Zahlen.

**Funk-SVD** (auch Matrix Factorization genannt, entwickelt von Simon Funk beim Netflix Prize 2006)   

In der Praxis wird statt klassischer SVD meist **Funk-SVD** verwendet, da sie direkt mit fehlenden Werten umgehen kann. Statt die Matrix exakt zu zerlegen, lernt man U und V direkt durch SGD (Stochastic Gradient Descent) – und zwar nur auf den bekannten Einträgen. Fehlende Werte werden ignoriert, nicht ersetzt. Das Ergebnis ist keine exakte Zerlegung, sondern eine Approximation, die aber deutlich besser mit realen, spärlichen Daten umgeht.

$$R \approx U \cdot V^T$$

- **R** - Rating-Matrix
- **U** – Nutzer-Faktormatrix
- **V^T** – Artikel-Faktormatrix
> Die gelernten Faktoren haben keine interpretierbaren Labels – das Modell lernt nur Zahlen.

**Minimales Code-Beispiel:**

```python
from surprise import SVD, Dataset
from surprise.model_selection import cross_validate

# MovieLens-Datensatz laden
data = Dataset.load_builtin('ml-100k')

# Modell definieren und evaluieren
model = SVD()
cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5)
```

---

## Wie bewertet man Recommender?
**Bewertungsgenauigkeit:**
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

**Rangfolgequalität:**
- Precision & Recall
- MAP (Mean Average Precision)

**Weitere Dimensionen:** Diversität, Neuheit

### Online-Evaluation (im Live-Betrieb)

- A/B-Tests
- Relevante Metriken: CTR (Klickrate), Konversionsrate, Engagement-Zeit, Retention vs. Churn

## Nachteile & Ethik

### Nachteile

- Kaltstart-Problem: Neue Nutzer oder Artikel haben keine Bewertungshistorie
- Sparsität: Die meisten Nutzer bewerten nur einen Bruchteil aller Artikel
- Skalierbarkeit: Ähnlichkeitsberechnungen werden bei großen Datenmengen teuer
- Popularitätsbias: Beliebte Artikel werden überproportional oft empfohlen

### Ethische Aspekte

Recommender Systems haben erhebliche gesellschaftliche Wirkung – sie beeinflussen:
- Meinungsbildung (Filterblasen)
- Konsumverhalten (gezielte Kaufanreize)
- Informationszugang (welche Inhalte werden sichtbar, welche nicht?)

> Der Algorithmus entscheidet nicht nur „was gefällt dem Nutzer?" – sondern auch, was er nie zu sehen bekommt.

## Lexikon

| Begriff | Erklärung |
|---|---|
| Surprise | Python-Bibliothek für Recommender Systems mit Algorithmen wie KNN, SVD und NMF |
| Singulärwertzerlegung (SVD) | Matrixfaktorisierungsmethode zur Zerlegung einer Ratingmatrix in latente Faktormatrizen |
| Latente Faktoren | Verborgene Merkmale (z. B. „Actionlastigkeit"), die das Modell automatisch aus Daten lernt |
| Kollaboratives Filtern | Empfehlung auf Basis des Verhaltens ähnlicher Nutzer oder ähnlicher Artikel |
| Inhaltbasiertes Filtern | Empfehlung auf Basis der Merkmale des Artikels selbst |
| Explizite Daten | Direkt gegebenes Feedback (Bewertungen, Likes) |
| Implizite Daten | Aus Verhalten abgeleitetes Feedback (Klicks, Verweildauer) |
| Kosinus-Ähnlichkeit | Ähnlichkeitsmaß zwischen zwei Vektoren basierend auf dem Winkel, nicht der Länge |
| Cold-Start-Problem | Fehlende Empfehlungsgrundlage für neue Nutzer oder Artikel ohne Bewertungshistorie |
| RMSE / MAE | Metriken zur Messung der Vorhersagegenauigkeit eines Recommenders |

---


## Referenzen
- [Datensatz MovieLens – Wikipedia](https://en.wikipedia.org/wiki/MovieLens)
- [Funk SVD Recommender](https://temugeb.github.io/tensorflow/python/svd/2021/02/04/Funk-SVD-recommender-p1.html)
- [Matrix Factorization Techniques](https://medium.com/@himasharandil/matrix-factorization-techniques-ab01539c2906)
- [Recommender System – Wikipedia](https://en.wikipedia.org/wiki/Recommender_system)
- [Tutorial Tensorflow Recommender](https://www.tensorflow.org/recommenders)
