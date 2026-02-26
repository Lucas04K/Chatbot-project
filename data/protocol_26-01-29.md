# Tag 9, 29.01.2026

Entscheidungsbäume (Decision Trees)

---

## Grundlegender Überblick/ Hauptthemen

- Überwachtes Lernen - Klassifikation und Regression
- Grundprinzip von Entscheidungsbäumen
- Binäre Entscheidungen (ja/nein-Fragen)
- CART-Methode (Classification and Regression Trees)
- Gini Impurity zur Bewertunng von Splits
- Wurzelknoten (root node), Kinderknoten (child node) und Blätter (leafs)
- Overfitting-Problematik bei Entscheidungsbäumen
- "Zurechtstutzen" der Bäume
- Hyperparameter: Max Depth, Max Leaf Nodes, Max Splits, Max Features
- Hyperparameter-Optimierung
- Whitebox vs. Blackbox Algorithmen
- Greedy Algorithmus

---

## Zeitplan

|          Zeit | Inhalt |
|--------------:|--------|
| 09:00 - 10:00 | Daily Review |
| 10:00 - 12:00 | Decision Trees Theorie |
| 12:00 - 13:00 | Mittagspause |
| 13:00 - 16:00 | Notebooks zu Decision Trees |
| 16:00 - 16:30 | Tägliches Stand-up |
| 16:30 - 18:00 | Vertiefung |

---

## Haupt Take-Away

Entscheidungsbäume sind überwachte Lern Algorithmen, die durch binäre Ja/Nein-Fragen Daten klassifizieren. Sie funktionieren zB wie das Spiel "Wer bin ich?" - durch systematisches Ausschlussverfahren. Der CART-Algorithmus nutzt "Gini Impurity", um optimale Splits zu finden. 

---

## Lexikon

| Wording | Definition |
|---------|------------|
| Decision Tree | Überwachter Lernalgorithmus, der durch binäre Entscheidungen Daten hierarchisch in Klassen einteilt. |
| CART | Classification and Regression Trees - Standardmethode zum Bau von Entscheidungsbäumen aus den 1980ern. |
| Gini Impurity | Maß für die Unreinheit eines Blattes. Berechnet, wie gut ein Split die Daten trennt. Wert zwischen 0 (perfekt rein) und 0,5 (maximal unrein). |
| Root Node / Wurzelknoten | Oberster Knoten des Baums, enthält alle Daten und trifft erste Entscheidung. |
| Child Nodes / Kinderknoten | Entstehen durch Splits und enthalten Teilmengen der Daten. |
| Leafs / Blätter | Endknoten ohne weitere Splits. Enthält finale Klassenzuordnung. |
| Split / Schnitt | Aufteilung eines Knotens anhand eines Features und Schwellenwerts in zwei Kinderknoten. |
| Purity / Reinheit | Maß dafür, wie homogen die Klassen in einem Knoten verteilt sind. |
| Overfitting | Modell passt sich zu stark an Trainingsdaten an. Bei Decision Trees durch zu viele Splits. |
| Regularisierung | Begrenzung des Baumwachstums durch Hyperparameter zur Vermeidung von Overfitting. |
| Greedy Algorithm | Algorithmus, der an jedem Punkt die lokal optimale Entscheidung trifft, ohne globale Konsequenzen zu berücksichtigen. |
| Whitebox Model | Modell, dessen Entscheidungen nachvollziehbar und erklärbar sind. Gegenteil von Blackbox. |
| Hyperparameter | Parameter, die vor dem Training festgelegt werden und nicht vom Modell gelernt werden können. |

---

## Notizen

### Grundprinzip: "Wer bin ich?"-Spiel

Systematisches Ausschlussverfahren durch binäre Ja/Nein-Fragen. Ziel: Optimale Features finden, die Daten am besten teilen (trifft zu / trifft nicht zu).

### Überwachtes Lernen - Klassifikation

Daten enthalten Zielvariable. Klassifikation weist Klassenlabel zu ↔ Regression sagt numerische Werte vorher.

### Whitebox vs. Blackbox

Decision Trees = Whitebox: Entscheidungen nachvollziehbar und erklärbar. Wichtig bei kritischen Entscheidungen. Biases und Fehler identifizierbar ↔ neuronale Netzwerke, LLMs = Blackbox. Decision Trees sind Bausteine für komplexere Modelle (Random Forest etc.).

### Baumstruktur

**Binär**: Zwei Ausgänge pro Knoten. **Wurzelknoten** (Root Node): Erste Einteilung mit allen Daten. **Kinderknoten** (Child Nodes): Teilmengen nach Split. **Blätter** (Leafs): Endknoten mit finaler Klassenzuordnung. Sample-Größe wird nach unten kleiner.

### CART-Methode (Classification and Regression Trees)

Standard seit 1980ern, ursprünglich für medizinische Diagnose. Greedy Algorithm: Trifft zu jedem Zeitpunkt lokal optimale Entscheidung ohne globale Berücksichtigung.

### Gini Impurity - Kernkonzept

Wertebereich: 0 (perfekt rein, alle gleiche Klasse) bis 0,5 (maximal unrein, 50/50 Split). Je niedriger, desto besser der Split.

**Beispiel "Kennt Travis Kelce"** (Taylor Swift Fan Vorhersage):
- Trevor Kelce =NFL-Spieler + Partner v. Taylor Swift
- Kennt ihn nicht: 7 Personen, 0 Fans → Gini = 0
- Kennt ihn: 4 Personen, 4 Fans → Gini = 0
- Gesamt-Gini = 0 → perfekter Split, wird Root Node

**Beispiel "Hat Katze"**:
- Hat Katze: 4 Personen (1 Fan, 3 keine) → Gini = 0,375
- Keine Katze: 7 Personen (3 Fans, 4 keine) → Gini = 0,489
- Gewichtet: 0,448

CART berechnet Gini für alle Features und Schwellenwerte, wählt niedrigsten Wert.

### Iterativer Prozess

Nach Split: Nur Teilmenge im jeweiligen Ast betrachten. Bei unreinem Blatt: Prozess wiederholen bis Stoppbedingung (Gini = 0, keine Verbesserung mehr, oder nur eine Instanz).

### Overfitting-Problem

Ohne Regularisierung: CART zerteilt unbegrenzt weiter. Worst Case: Ein Split pro Datenpunkt. Modell lernt Trainingsdaten inkl. Rauschen auswendig. Entscheidungsgrenzen zu komplex und spezifisch. Schlechte Performance auf neuen Daten.

### Hyperparameter zur Regularisierung

**Max Leaf **: Maximale Anzahl Blätter  
**Max Depth**: Maximale Tiefe/Ebenen  
**Max Splits**: Maximale Aufteilungen  
**Max Features**: Maximale Features für Baumaufbau

Vor Training festlegen, nicht vom Modell lernbar.

### Hyperparameter-Tuning

**Domain Knowledge anwenden**: Sinnvolle Grenzen basierend auf Problemverständnis (Bsp. Pilzbestimmung).

**Durchrastern**: Systematisches Durchprobieren von Parameterwerten, beste Kombination nach Evaluierung wählen.

---

## Zusammenfassung 

- Entscheidungsbäume teilen Merkmal in binären Bäumen auf (ist der Fall / ist nicht der Fall)
- Schauen wie diese in Bezug auf Zielvariable performen
- Meistens CART verwendet zum Bauen von Entscheidungsbäumen
- CART schaut wie gut jeweiliger Schnitt funktioniert durch Berechnung der Gini Impurity
- CART setzt Schnitt, teilt Instanzen nach Schnitt ein
- Schaut sich Daten wieder an, sucht besten Schnitt für diese Daten usw. bis Stoppbedingung erfüllt
- Stoppbedingung zB Leaf so pure dass man nicht mehr verbessern kann (Travis Kelce Beispiel)
- Grundsätzlich zerteilt CART immer weiter: daher stoppen meist notwendig
- Stoppen durch Regulierung der Bäume: max Anzahl Blätter bzw Splits bzw Features
