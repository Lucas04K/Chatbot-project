# Tag 03, 21.01.2026

Explorative Datenanalyse (kurz EDA)

---
## __Grundlegender Überblick__

* Grundlegende Begrifflichkeiten in der EDA
* Was ist EDA und warum machen wir das?
* Arten von EDA
* Schätzungen
* Datentypen
* Univariate EDA - Berechnungen von Mittelwert, Median und Modus
* Streuung von Daten

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|10:00 - 11:08|Erste theoretische Inputs|
|11:16 - 12:10|Weitere theoretische Inputs|
|12:10 - 13:30|Mittagspause| 
|13:30 - 16:00|Praktische Übungen|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|


---
## __Erste inhaltliche Notizen__

# Lexikon #
|Wording|Definition|
|---|---|
|univariat|Univariat bedeutet, dass sich etwas auf nur eine einzige Variable bezieht, was in der Statistik und Mathematik verwendet wird, um Daten oder Funktionen zu beschreiben, die sich nur mit einem Merkmal oder einer Unbekannten beschäftigen.|
|bivariat|Bivariat (von lat. bis = zwei und variatus = verschieden) beschreibt in der Statistik und Mathematik die Untersuchung des Zusammenhangs zwischen genau zwei Variablen (Merkmalen), um deren gegenseitige Abhängigkeit zu analysieren, beispielsweise durch Korrelation oder Regression, was über die getrennte Betrachtung einzelner Variablen (univariat) hinausgeht.|
|multivariat|Mit Hilfe von multivariaten Verfahren (auch multivariate Analysemethoden) werden in der multivariaten Statistik mehrere statistische Variablen oder Zufallsvariablen zugleich untersucht.| 
|Sample sizes|Schätzungen - Stichproben, aus der Grundgesamtheit entommene Daten.|
|Konfidenz|In der Statistik: Ein Maß für die Zuverlässigkeit einer Schätzung. |
|Mittelwert|Alle Werte zusammenrechnen und durch die Anzahl der zusammengerechneten Werte teilen|
|Median|Daten werden nach Größe geordnet und der mittlere Wert gesucht, sodass auf beiden Seiten 50% liegen. Aufwendiger durch vorherige Sortierung|
|Modus|Nicht unbedingt eindeutige, meist für kategorische Daten verwendeter häufigste Wert.|
|Kategorische Typen|Zwischen Kategorien besteht keine numerische Ordnung (Beispiel Namen, Städte, Länder)|
|Numerische Typen|Sind numerisch geordnet (Beispiel Kleidergroeßen, S/M/L)|
|Quantile|Sortierte Daten in Teile einteilen|
|Quartile|4 Teile|
|Dezile|10 Teile|
|Perzentile|100 Teile|

#### Hypothesengenerierung

Was ist eine Hypothese? Wie stellt man diese?

Warum suchen wir erst Hypothesen und betrachten dann die Daten?
Weil es die Sicht für Korrelationen zwischen Daten erleichtert.

#### Besprochen Data Science Lifecycle (siehe Folie)

Was ist EDA und warum machen wir das?
Um einen Eindruck der Daten zu bekommen und Einsichten zu gewinnen. Unvorhergesehene Situationen vorhersehen.

### Arten von EDA
#### Datentypen
* Kategorische Typen
* Numerische Typen

#### Univariate :
##### Mittelwert berechnen:
Alle Werte zusammenrechnen und durch die Anzahl der zusammengerechneten Werte teilen
Beispiel: Im Mittelalter sind Menschen im Durchschnitt nur 30 Jahre alt geworden. Liegt daran, dass Babys sehr oft verstorben sind.

##### Median:
Daten werden nach Größe geordnet und der mittlere Wert gesucht, sodass auf beiden Seiten 50% liegen. Aufwendiger durch vorherige Sortierung

##### Modus:
Nicht unbedingt eindeutige, meist für kategorische Daten verwendeter häufigste Wert.

#### Streuung von Daten:
##### Spannweite:
Differenz zwischen kleinstem und größtem Wert (Beispiel: Alter, Range)

##### Quantile:
Sortierte Daten in Teile einteilen.
Gut gegen Ausreißer (Beispiel: Ladezeiten von Websites)

##### Interquartilsabstand (IQR):
Mittlere 50%
Zwischen 25% und 75%

##### Ausreißer:
Gegenüber einer Menge von üblichen Daten weit außerhalb des Bereichs. 
Können situationsbedingt gut oder schlecht sein. 
Eventuell verwertbar.

##### Boxplots:
Sind sehr informationsreich. Werden oft von Statistikern genutzt, dafür 

#### Varianzen und Standardabweichungen:
##### Varianz:
Durchschnittliche quadrierte Differenz der Werte vom Mittelwert.
Wie weit ist der Datenpunkt vom Mittelwert entfernt?

##### Standardabweichungen:
Quadratwurzel der Varianz
Differenz zwischen jedem Datenpunkt und dem Mittelwert

##### Schiefe:
Grad der Asymmetrie der Datenverteilung

Kurtosis:
Wölbung / Exzess
Grad der Spitzigkeit im Vergleich zu einer Normalverteilung

Histogramm

##### Modalitäten:
Anzahl der Gipfel (Modi) in der Verteilung eines Datensatzes

##### Streudiagramm/Korrelationsdiagramm
Verwendung um Beziehung zwischen zwei numerischen Variablen zu visualisieren

Pearson-Korrelationskoeffizient / Pearson's r:
Lineare Beziehung beschreiben

Spearman-Rangkorrelationskoeffizient - Spearman's p

Techniken
