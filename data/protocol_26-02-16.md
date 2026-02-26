# Tag 21, 16.02.2026

Zeitreihenanalyse

---

## Haupt Take-Away

Zeitreihenanalyse versucht, aus zeitlich geordneten Daten systematische Muster (Trend, Saisonalität/Zyklen, Autokorrelation) herauszuarbeiten, damit Forecasts sinnvoll möglich sind. Zentral sind regelmäßige Daten, ein korrekter zeitlicher Train-Test-Split (keine Zukunft im Training), sowie die Frage nach Stationarität (oder passenden Transformationen). In der Modellierung startet man mit einfachen Baselines und klassischen Verfahren (AR/MA/ARMA/ARIMA) und erweitert bei Bedarf über Feature Engineering (Lag/Rolling) hin zu ML- und Deep-Learning-Ansätzen, abhängig von Datengröße, Komplexität, Interpretierbarkeit und Ressourcen.

---

## Lexikon

| Wording | Definition |
|---------|------------|
| Zeitreihe | Sequenz von Datenpunkten mit Zeitindex; Reihenfolge ist relevant und Abstände sind idealerweise regelmäßig. |
| Historische Daten | Vergangenheitswerte einer Zeitreihe. |
| Signal | Nicht-zufällige, regelmäßige Struktur in der Zeitreihe, aus der man etwas ableiten kann. |
| Forecast | Vorhersage im Zeitreihen-Kontext (statt „Prediction“). |
| Autokorrelation | Zusammenhang des Werts zu Zeitpunkt \(t\) mit früheren Zeitpunkten \(t-1, t-2, ...\). |
| Trend | Langfristige (niederfrequente) Tendenz der Reihe, z.B. systematischer Anstieg/Abstieg. |
| Saisonalität | Wiederkehrende Muster mit fester Periode (z.B. wöchentlich, jährlich). |
| Zyklus | Wiederkehrende Muster ohne feste Periode/Dauer (z.B. Konjunktur). |
| Rauschen (Noise) | Zufällige Schwankungen; idealerweise ohne Muster. |
| Stationarität | Annahme: Mittelwert und Varianz sind über die Zeit (annähernd) konstant. |
| Moving Average (Glättung) | Rollender Durchschnitt über Fenster \(k\). |
| Exponentielle Glättung | Gewichte fallen exponentiell ab; neuere Werte dominieren stärker. |
| Drift | Einfache Prognose durch lineare Fortschreibung aus der Historie. |
| ARMA | Kombination aus AR(p) und MA(q) für stationäre Reihen. |
| ARIMA | ARMA mit vorgelagertem Differencing (d), um Reihen stationärer zu machen. |
| SARIMA | ARIMA mit zusätzlichen saisonalen Komponenten. |
| Leakage | Unsaubere Evaluation, wenn Zukunftsinformation in die Trainingsdaten gelangt (z.B. durch zufälligen Split). |

## Notizen 

### Motivation: Random Walk → „Sinn in der Zeit“
- Photon-Beispiel: Sonne→Erde ~8 Min, Sonne Kern→Sonne Oberfläche 10.000–1.000.000 Jahre wegen Random Walk (ständige Ablenkung/"Schocks").
- Brücke: Zeitreihen wirken oft „schockartig“; Ziel ist, **statistische Struktur** in der Zeit zu finden, um Forecasts zu verbessern.

### Was ist eine Zeitreihe – wann lohnt sich Analyse?
- Zeitreihe = zeitlich geordnete Messpunkte (regelmäßige Abstände ideal).
- Zeit kann relevant sein oder nicht: sinnvoll, wenn zeitliche Ordnung zusätzliche Information trägt (Trend, Saisonalität/Zyklen, Autokorrelation). Unsinnig, wenn formal Zeit, aber kaum Muster/Erkenntnis (Museum-Beispiel).

### Typische Merkmale
- Abhängigkeiten: aktueller Wert hängt von früheren ab (Trägheit; Wetter).
- Schocks/Fehler können nachwirken (z. B. Markt).
- Ziel: Systematik herausarbeiten, Restrauschen möglichst „musterlos“.

### Stationarität
- Viele klassische Modelle setzen konstantes Niveau/Varianz voraus.
- ADF-Test: p < 0,05 → eher stationär; p ≥ 0,05 → eher nicht.
- Bei Nicht-Stationarität: Differencing/Detrending, ggf. Log-Transformation.

### Zerlegung („Schichten“)
- Zeitreihe ≈ Trend (niederfrequent) + Saisonalität/Zyklen (mittelfrequent) + Rauschen (hochfrequent).
- Trend kann Muster maskieren; Modelle lernen sonst primär den Trend.

### Fehlende Werte (Lücken)
- Strategien: ffill/bfill, Mittelwert/Interpolation, Resampling, modellbasiertes Auffüllen.
- Warnung: zu einfache Füllungen können Aussagekraft verzerren.

### Train-Test-Split ohne Leakage
- Kein Random Split. Stattdessen zeitlich schneiden: Vergangenheit trainieren, Zukunft testen.
- Random Split ⇒ Leakage und unrealistisch gute Performance.

### Glättung
- Moving Average (Fenster k): Rauschen reduzieren; Trade-off groß=glatt/Detailverlust, klein=mehr Details.
- Weighted/Exponential Smoothing: neuere Beobachtungen stärker gewichtet.

### Baseline-Forecasts
- Naiv: nächster Wert = letzter Wert.
- Saisonal naiv: Wert aus letzter Saison.
- Drift: lineare Fortschreibung. Dient als Benchmark für komplexere Modelle.

### Klassische Modelle: AR, MA, ARMA, ARIMA (und saisonal SARIMA)
- AR: Vorhersage aus vergangenen Werten; Ordnung \(p\) = wie viele Lags genutzt werden.
- MA: Vorhersage aus vergangenen Fehlern; Ordnung \(q\) = wie viele Fehler-Lags genutzt werden.
- ARMA: Kombination aus AR(p) und MA(q); setzt stationäre Reihen voraus.
- ARIMA: stationär machen durch Differencing, dann ARMA; saisonale Erweiterung wird als Idee erwähnt.

### ML über Feature Engineering
- Zeitreihen-Features machen Muster sichtbar: Lag-Features, Rolling-Features.
- Starker Trend kann dominieren → ggf. vorher behandeln.

### Deep Learning Ansätze
- Für nichtlineare/multivariate Reihen:
  - Prophet (siehe Skript als CNN/Conv-Idee für lokale Muster),
  - RNN/LSTM für längere Abhängigkeiten (rechenintensiv),
  - Transformer für lange Abhängigkeiten (daten-/rechenintensiv).
- Abwägung: Interpretierbarkeit, Ressourcen, Datengröße, Komplexität.

