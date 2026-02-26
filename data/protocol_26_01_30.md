# Tag 10, 30.01.2026

Lineare Regression (Linear Regression)

---
## __Grundlegender Überblick__

* Einsatz in der Biomechanik
* Regressionsmodell trainieren
* Lineare Gleichung
* Lineare Regression
* Woran erkennt man wie gut eine Gerade ist?
* Kleinste-Quadrate-Kriterium
* Kleinste-Quadrate-Regression
* Modelleistung
* Varianzanalyse
* Wurzel der mittleren quadratischen Abweichung (RMSE)
* Multiple Lineare Regression

---
##  __Zeitplan__

|          Zeit | Inhalt |
|--------------:|--------|
| 09:00 - 10:00 | Daily Review |
| 10:00 - 12:00 | Linear Regression Theorie |
| 12:00 - 13:00 | Mittagspause |
| 13:00 - 16:00 | Notebooks zu Linear Regression |
| 16:00 - 16:30 | Tägliches Stand-up |
| 16:30 - 18:00 | Vertiefung |


---
## __Erste inhaltliche Notizen__


### Haupt Take-Away ###
Lineare Regression modelliert den Zusammenhang zwischen einer abhängigen Variable und einer oder mehreren unabhängigen Variablen durch eine lineare Funktion. Die Modellparameter werden so geschätzt (meist mittels Methode der kleinsten Quadrate), dass die Summe der quadrierten Abweichungen zwischen beobachteten und vorhergesagten Werten minimal ist. Ziel ist es, Trends zu erklären und Vorhersagen für neue Datenpunkte zu treffen.



# Lexikon #
|Wording|Definition|
|---|---|
|Korrelation|Ein statistisches Maß für die Stärke und Richtung eines Zusammenhangs zwischen zwei Variablen.|
|Kausalität|Ein Ursache-Wirkungs-Zusammenhang, bei dem eine Variable eine andere direkt beeinflusst.|
|Merkmal|Eine messbare Eigenschaft oder Variable, die bei Beobachtungen erhoben wird.|
|Residuum|Die Differenz zwischen einem beobachteten Wert und dem vom Modell vorhergesagten Wert.|
|Gewicht|Ein Faktor, der angibt, wie stark eine Beobachtung in eine Berechnung oder Schätzung eingeht.|
|fitten|Das Anpassen eines Modells an Daten durch Schätzung seiner Parameter.|

---
## Notizen

### Einsatz in der Biomechanik
Untersuchung des Zusammenhangs zwischen Muskelkraft und Gelenkwinkel. Erstellung von Vorhersagen über die Belastung von Knochen basierend auf Bewegungsdaten.

### Regressionsmodell trainieren
- Zeigt Korrelationen auf
- Kann keine Kausalitäten darstellen!

### Lineare Gleichung
- $ y=b_{0}+b_{1}\cdot x$
- 2 Datenpunkte ergeben eine Gerade

### Lineare Regression
- mehr als 2 Punkte => Wie kann die bestmögliche Gerade gefunden werden?
- Korrelation der Variablen finden (r=0,9)
- es gibt immer Abweichungen (Fehler), daher wird +e in der Funktion addiert
- $ y=b_{0}+b_{1}\cdot x + e$

### Woran erkennt man wie gut eine Gerade ist?
- absolute Distanz zu Gerade von allen Punkten addieren
- Residuum / Fehlerterm: $e_i = y_i - \hat{y}_i$  
- Aufsummieren von Beträgen der Fehler möglich, aber besser:

### Kleinste-Quadrate-Kriterium
 $$ J(b_{0},b_{1})\,=\,\sum_i^n e_{i}^{2}\,=\,\sum_i^n(y_{i}\,-\,\hat{y}_{i})^{2}\,=\,\sum_i^n(y_{i}\,-\,(b_{0}\,+\,b_{1}x_{i}))^{2}$$
 $$n \text{ ist die Anzahl der Beobachtungen}$$
- Abweichungen werden quadriert (Konvexe Funktion) lässt sich einfacher fitten
- Gesamtfehler ist Summe der Quadrat-Fehler => große Abweichungen werden bestraft
- Wie kann aus allen möglichen Geraden, die richtige gefunden werden?
- Mittelwert von x und Mittelwert von Y als Ursprung für Geradenschar wählen
- Gesamtfehler von mehreren Geraden plotten, Funktion über Ergebnis legen und Minimum finden
- Ergebnisfunktion ergibt immer Parabel (bei Linearer Regression)

### Kleinste-Quadrate-Regression
$$ \mathrm{min}\ J(b_{0},b_{1})\ =\ \sum(y_{i}\ -\ b_{0}\ -\ b_{1}x_{i})^{2}$$


$$\begin{align}
\frac{\partial J}{\partial b_{0}}&=\mathrm{-2\,}\Sigma(y_{i}-b_{0}-b_{1}x_{i})\nonumber\,=\,0 \\
\frac{\partial J}{\partial b_{1}}&=\mathrm{-2\,}\Sigma x_i(y_{i}-b_{0}-b_{1}x_{i})\nonumber\,=\,0
\end{align}$$


$$\Rightarrow\ b_{0}=\bar{y}-b_{1}\bar{x}\qquad\text{und}\qquad b_{1}=\frac{\sum(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sum(x_{i}-\bar{x})^{2}}$$

- Minimum kann mathematisch über Ableitung ermittelt werden (Steigung = 0)
- Damit kann Abhängigkeit der Funktion von $b_{0}$ und $b_{1}$ bestimmt werden (analytische Berechnung)
- Tatsächlich: Numerische bestimmung, da weniger Aufwand

## Modelleistung

### Mittelwert $\bar{y}=\frac{1}{n} \sum\limits_{i=1}^{n}y_{i}$  
### Varianz $\sigma^2 = \frac{1}{n-1}\sum_i{(y_i-\bar{y})^2}$

### Varianzanalyse
SST = totale Quadratsumme,
SSE = erklärte Quadratsumme,
SSR = verbleibende Quadratsumme
- Mittelwert als Modell nehmen
- Lineares Regressionsmodell "erklärt" einen Teil der Quadratsumme
- Verbleibende Quadratusmme => Enstpricht Varianz
- R^2 gibt uns an, wie gut das Modell in der Lage ist, die Situation zu beschreiben

### Wurzel der mittleren quadratischen Abweichung (RMSE)
$$ R M S E=~{\sqrt{{\frac{1}{n}}\sum_{i=1}^{n}\left(y_{i}-{\hat{y}}_{i}\right)^{2}}} $$
Kann auch bei andern Modellen als Lineare Regression zum bewerten der Modellqualität verwendet werden

### Multiple Lineare Regression
- Mehr als ein Merkmal zur Vorhersage verwenden
- Jede Beobachtung hat eine Geradengleichung
- Für allgemeine Betrachtung wird Matrixmultiplikation verwendet $ y=X b+e $
- y, b und e sind Vektoren, X ist eine Matrix
- Mit Normalengleichung können alle B-Werte auf einmal berechnet werden

### Bewertungsmetriken
#### Bestimmtheitsmaß: R^2 $$ R^2 = 1 - \frac{SSR}{SST} = \frac{SSE}{SST}$$
#### MSE mittlere quadratische Abweichung
#### RMSE $$ R M S E=~{\sqrt{{\frac{1}{n}}\sum_{i=1}^{n}\left(y_{i}-{\hat{y}}_{i}\right)^{2}}} $$
#### Angepasstes R^2 $$\text{adj. }R^2=1-\frac{n-1}{n-m-1}\cdot(1-R^2)$$
    => Verwendung von zu vielen Merkmalen (m) verglichen mit Anzahl Datensätzen (n) wird bestraft




