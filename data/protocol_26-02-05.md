# Tag 14, 05.02.2026

Ensemble-Methoden 

---
## __Grundlegender Überblick__

* Esemble-Methoden generell
* CART - Vor und Nachteile
* Ensemble-Lernen, Theorie und Voting

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:20|Daily Review|
|10:00 - 11:00|Erste theoretische Inputs|
|11:10 - 12:10|Weitere theoretische Inputs|
|12:20 - 13:30|Mittagspause| 
|13:30 - 16:00|Praktische Übungen|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|


---
## __Erste inhaltliche Notizen__


### Title
Ensemble-Methoden

### Anekdote
Das Beispiel mit den Wettermodellen für Süd-England.

## __Lexikon__
|Wording|Definition|
|---|---|

#### CART
##### Regularisierung
Pruning um overfitting zu vermeiden.
Bäume neigen zum Overfitting.

##### CART - Vor- und Nachteile
|Vorteile|Nachteile|
|---|---|
|White-Box-Modell - einfach zu interpretieren|nicht sehr genau|
|kann gemischte Daten verarbeiten, diskret und kontinuierlich|gierige Natur der Konstruktion|
|unempfindlich gegenüber Datentransformationen... Aufteilungspunkte basieren auf Ranking|Bäume sind instabil, kleine Änderungen im Input können zu großen Änderungen in der Baumstruktur führen. Beispiel: Wenn sich oben leicht was verändert, kann der komplette Baum anders aussehen|
|relativ robust gegenüber Ausreißern|neigen zu Overfitting (d.h. Schätzer mit hoher Varianz)|

#### Bäume sind instabil
##### Beispiel: 
Man geht in ein Restaurant und probiert alles einmal und wählt am Ende, was man essen möchte.
Man könnte auch Freunde fragen auch zu probieren, oder man fragt jemanden, ob er schon mal da war. 

##### Beispiel:
Wer wird Millionär
Fehler: Man spricht vorerst über seine Annahme und beeinflusst damit den Publikumsjoker.

Brücke zu Ensemble:
Ensemble = Erfragen von sehr vielen verschiedenen Meinungen

#### Theorie der Weisheit der Vielen (Wisdom of the crowds)
Auch bekannt unter Schwarmintelligenz

#### Ensemble-Lernen
* Bagging (glecihes Modell auf verschiedenen Teilen der Daten)
* Boosting (sequenziell angepasst an der Wcihtigkeit der Beobachtungen)
* Stacking/Blending (paralleles Training und Kombination)
Ist weniger anfällig für Overfitting

#### Mehrheitsentscheidung
* Hard Voting (nimmt di3e Mehrheitsklasse)
* Soft Voting (Durchschnitt der summierten Wahrscheinlichkeitsvektoren / Soft voting übertrifft Hard Voting in der Regel)

### Stacking
#### Beispiel schwache Lerner
Als Beispiel sind hier 1000 schwache Lerner (m) zu einer Quote der wahren Vorhersagen (p) mit einem Ergebnis von 0.27% Fehlerquote in der Vorhersage<br />
m = 1000, p= 0.51 = 0.27% Fehlerquote<br />
Diese ändert sich, wenn man die Quote der wahren Vorhersagen um nur 0.04% erhöht auf 0.08% Fehlerquote<br />
m = 1000, p= 0.55 = 0.08% Fehlerquote<br />

### Bagging (Bootstrap aggregating)

Formel: f(x)=1m∑fm(x)<br />

Man zieht zufällig eine bestimmte Menge Daten aus dem Trainingsdatenset heraus und füttern das Modell damit.<br />
<small>Um die Unabhängigkeit zu bewahren, muss diese bestimmte Menge Daten wieder zurück ins Gesamtdatenset (Keine Abhängigkeit der zuvor gezogenen Daten, welche die Gesamtdatenmenge verkleinert hätten).</small>


#### Random Forest
Versuch Prädiktoren zu dekorrelieren
Zufällige Features (Teilmenge von Eingabevariablen)
Zufällige Beobachtungen (Teilmenge von Datenfällen)

Nachteil: Random Forest gewinnt an Leistung, aber verliert an Interpretierbarkeit

#### Random Patches und Subspaces
* Random Patches: Sampling von sowohl Features als auch Instanzen
* Random Subspaces: Sampling nur von Features
* Kann zur Ermittlung der Feature-Wichtigkeit verwendet werden

#### Extra-Trees - Extremeley Randomized Trees
* Alle Daten für Splits verwenden
* Zufällig Auswahl spart Rechenleistung

#### Genauigkeit vs. Varianz
Genauigkeit:
* Random Forest und Extra Trees übertreffen Entscheidungsbäume

Varianz:
* Entscheidungsbäume → hoch
* Random Forest → mittel
* Extra Trees → niedrig


### Boosting
* anpassen adaptiver Basisfunktion
* gierig

Die Formel: f(x)=b0  +∑bmϕm(x)

Wobei:
* ϕm werden von einem schwachen Lerner generiert
* der schwache Lerner wird sequenziell auf gewichtete Versionen der Daten angewendet
* mehr Gewicht wird Beispielen gegeben, die in früheren Runden falsch klassifiziert wurden
* der schwache Lerner kann jeder Regressor oder Klassifikator sein, aber es ist üblich, CART → Entscheidungsbaum zu verwenden 

INIT
* Jede Instanz hat das gleiche Gewicht

LOOP
* (Gewichte von falsch vorhergesagten Instanzen werden erhöht.)
* Modell wird trainiert
* Alle Modelle sagen vorher
* Die Vorhersagen werden nach ihrer Genauigkeit gewichtet und addiert


#### Boosting-Algorithmus
##### Beispiele
* AdaBoost
* LogitBoost
* Gradient Boost
* Stochastic Gradient Boost
* XGBoost (eXtreme Gradient Boost, sollten wir kennen, populär)

## Interpretierbarkeit
### Partial-Dependence-Plots - Vorteile
* Intuitiv
* kausale Interpretations (für das Modell)

### Permutation-Feature-Wichtigikeit - Vorteile
* Schöne Interpretation: der Verlust, wenn ein Feature entfernt wird
* berücksichtigt die Interaktionen mit anderen Features
* erfordert kein erneutes Training

---
## __Referenzen__

* [Zu den Folien](https://literate-adventure-1e3gl8r.pages.github.io/sessions/Ensemble_Methods_DE_FINAL.html#)