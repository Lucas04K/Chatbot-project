# Tag 24, 19.02.2026

# Dimensionalitätsreduktion

## Haupt Take-Away
Dimensionalitätsreduktion versucht hochdimensionale Datensätze auf eine geringere Anzahl von Dimensionen (Merkmalen) zu reduzieren.   
Dabei wird darauf geachtet, die höchste Varianz und damit die meiste Information und Eigenschaften der Originaldaten beizubehalten.   
Dazu gibt es verschiedene Verfahren: die deterministische Hauptkomponentenanalyse (Principal Component Analysis, PCA), t-SNE, UMAP und Autoencoder, die auf neuronalen Netzen basieren.

## Notizen 

### Motivation: "Fluch der Dimensionalität“
Die Nichte hat versucht in der Schule durch ein Blatt Papier auf einer Münze selbige mit einem Bleistift abzubilden. Dann fehlte ihr aber die Rückseite und zusätzlich auch der Rand. Dies wurde dann in weiteren Zeichnungen ergänzt, so dass für jede Dimension der Münze eine Zeichnung entstand.

### Analogie
Kurze, selbsterstellte Zusammenfassungen von Büchern ergibt eine Reduktion der gesamten Datenmenge, Kernaussagen und Maximum an Info bleiben erhalten.

### Einordnung
Unlabeled, unsupervised Learning: Dimensionality Reduction

### Der Fluch der Dimensionalität bei Graphiken
Zweidimensional: Flächen kennzeichnen und Zugehörigkeit zu Klassen. Das lässt sich noch problemlos darstellen.     
Was ist aber bei mehr Dimensionen?  
Eine bestimmte Vergrößerung der Dimension lässt sich oft noch durch grafische 'Tricks' erreichen (Farbe, 3-D-Diagramm).   
Aber was macht man bei noch mehr Dimensionen? Je mehr Dimensionen, desto schwieriger wird die grafische Darstellung.

### Beispiel für Dimensionsreduktion
Eine dreidimensionale Skulptur wird auf einem Foto auf zwei Dimensionen reduziert.   
Ähnlich funktioniert Dimensionsreduktion.

### Ziel
Varianz und damit möglichst viel Information soll erhalten bleiben.
Vorteile
- ggf. grafische Darstellung möglich
- Erhöhung der Effizienz
- Verringern von Rauschen
- Ggf. Vermeidung von Overfitting

Warum ist das nötig?
Fluch der Dimensionalität: mit jeder Dimension erhöht sich die Potenz, Datenmenge wird mit zunehmenden Dimensionen auch sehr dünn. Das Datenset wird 'sparse'. Je höher die Dimensionen, desto schwieriger wird es, die wichtigen Informationen zu finden.   
Distanzproblem: alle Punkte sind weiter voneinander entfernt. (vgl. Länge der Diagonalen in Quadrat, Würfel, Hyperwürfel)

Dazu gab es noch das Beispiel mit dem Volumenproblem: alle Datenpunkte liegen auf der äußeren Schale der Kugel in einer dünnen Schicht verteilt. Mit höheren Dimensionen wird die Schale dünner und die Punkte verteilen sich immer weiter entfernt von der Mitte und voneinander. Je mehr Dimensionen, desto dünner wird die Datenschicht.

### Idee
Durch Weglassen von Dimensionen sollen möglichst die relevanten Informationen erhalten bleiben. Wir brauchen dann nicht mehr alle Originalfeatures.

### konkrete praktische Ziele
- Datenkompression
- Visualisierung
- Rauschreduktion   
- Merkmalextraktion
- Effiziente Berechnung   

### Methoden
- Lineare Methoden: PCA, LDA (nicht besprochen)
- Nicht-lineare Methoden t-SNE, UMAP, Autoencoder

### Wann verwenden?
- hochdimensionale Daten, die möglicherweise sparse sind
- Visualisierung
- Recheneffizienz steigern
- Viele korrelierte Features. Die tragen die gleiche Information

### nicht verwenden bei
- wenigen Features <10-20

----
## Hauptkomponentenanalyse, Principal Component Analysis, PCA
Finde neue Achsen nach folgender Idee:
- finde Richtungen maximaler Varianz
- projiziere Daten auf diese Richtungen
- erste Komponente: höchste Varianz
- zweite Komponente: steht orthogonal auf der ersten und ist unabhängig von der ersten.

Mathematisch:
- Mittelwert auf 0 transformieren
- Eigenvektoren der Kovarianzmatrix ergibt Richtungen für Hauptkomponenten
- Sortierung nach Eigenwerten (Varianz) ergibt die Wichtigkeit der Achsen (wichtigste Komponente=höchste Varianz)

Vorteile
- einfach und schnell
- gut verstanden
- deterministisch
- bewahrt globale Struktur
- kann für Rekonstruktion verwendet werden (ist umkehrbar)

Nachteile
- nur lineare Beziehungen
- empfindlich gegenüber Skalierung (Standardisierung nötig!)
- schwer interpretierbar bei vielen Features
- Annahme: Varianz = Wichtigkeit

Beispiel:
Bild mit handgeschriebenen Zahlen 784 Features (aus Bildgröße)   
Bildkompression erhält 95% der Varianz, reduziert auf 154 Hauptkomponenten, 20% Bildgröße
   
Alternative Methode der Gesichtserkennung   
Eigengesichter 47*62 Pixel = 2914 Features, kann auf 154 Hauptkomponenten reduziert werden.   
Bei Bildern werden die zentralen Merkmale (Principal Components) hervorgehoben.   

Anwendungsfälle
- wenn Berechnung vieler Dimensionen teuer ist, durch PCA kann das Trainieren günstiger werden
- Anomalieerkennung bei Zeitreihen
- Vorverarbeitung bei Bildern, Rauschunterdrückung
- Visualisierung
- PCA-Plots (mit Vorsicht zu genießen, PC1 bildet die meiste Varianz ab, dadurch kann PC2 schon ggf. sehr wenig Bedeutung haben.)
- Merkmalsextraktion
---- 
## t-SNE - t-distributed Stochastic Neighbor Embedding
Hauptidee:
- ähnliche Punkte bleiben nah beieinander, unähnliche gehen auseinander
- verwendet t-Verteilung

Anwendungsfälle
- vor allem für Visualisierungen
- nicht-lineare Dimensionalitätsreduzierung
- erhält Nachbarschaften, d.h. lokale Struktur
- konvertiert Distanzen von Wahrscheinlichkeiten

t-SNE Algorithmus
- paarweise Distanzen berechnen und zu Wahrscheinlichkeiten konvertieren ("Wie wahrscheinlich ist es, das jemand in der Nähe auftaucht?")
- niedigdimensionale Initialisierung: zufällige Positionen in niedrigeren Dimensionen
- Verschiebung der Punkte, so dass die Wahrscheinlichkeiten in der niedrigeren Dimension abgebildet werden, Berechnung mit t-Verteilung

t-SNE Parameter
- Perplexität (5-50): Balance zwischen lokaler/globaler Struktur, typisch 30-50 (lokale Nachbarschaften vs. globale Strukur)
- Lernrate
- Iterationen

Nachteile
- langsam wegen vielen Berechnungen
- globale Abstände werden nicht gut dargestellt.

## UMAP - Uniform Manifold Approximation and Projection 
moderne Variante zu t-SNE   
versucht Balance zwischen lokalen und globalen Strukturen besser zu behalten   

Vorteile gegenüber t-SNE   
- skaliert besser
- Distanzen sind bedeutungsvoller
- kann neue Punkte transformieren

Parameter
n_neighbors (5-50): lokale vs. globale Struktur

(Zur Erläuterung von 'lokal' und 'global': Analog zur Erde: Fläche (lokal) vs. Kugel(global))
   
Idee von UMAP:   
kann man die Mannigfaltigkeit auswickeln?

Vorteil
- schneller als t-SNE

## Vergleich PCA vs. t-SNE vs UMAP
Empfehlung:   
Visualisierung: UMAP > t-SNE > PCA   
Feature Reduction: PCA > UMAP   
Geschwindigkeit: PCA >> UMAP > t-SNE   

## Autoencoder (funktionieren über neuronale Netze, Deeplearning)
weiterer Typ von Algorithmen zur Dimensionalitätsreduktion  
mit den Layern werden die Daten komprimiert  
4 Varianten: Vanilla, Denoising, Sparse, Variational  
   
## Zusammenfassung
- Dimensionalitätsreduktion: essenziell für hochdimensionale Daten: Datenpunkte oft weit auseinander, korrelierte Daten sind oft unnötig und können reduziert werden
- Visualisierung
- viele verschiedene Methoden verfügbar

Methoden  
- PCA: Achsen finden in Richtung größter Varianz  
- t-SNE  
- UMAP  
- Autoencoder  
  
Best Practices:
- immer Daten standardisieren
- mehrere Methoden ausprobieren, ggf. auch mehrere Methoden kombinieren
- Parameter tunen (besonders Perplexität/n_neighbors)
- PCA vor t-SNE für große Datensätze
- Fachwissen einfließen lassen

Analogie zur Karte:  
Karte zeigt Landschaft,  
man kann die Landschaft von der Karte rekonstruieren (Rekonstruktion)


## Lexikon

| Wording | Definition |
|---------|------------|
| Autoencoder | ein neuronales Netz für unüberwachtes Lernen, das Eingabedaten komprimiert (Encoder) und wieder rekonstruiert (Decoder), um wesentliche Merkmale zu lernen |
| LDA | Linear Discriminant Analysis - supervised Methode zur Dimensionalitätsreduktion |
| PCA | Principal Component Analysis. Deterministisches Verfahren zur Dimensionalitätsreduktion |
| sparse | dünne Verteilung der Datensätze mit viel Zwischenraum |
| Support Vector Machine (SVM) | Supervised Learning Algorithmus, der hauptsächlich zur Klassifizierung und Regressionsanalyse eingesetzt wird |
| t-SNE | t-distributed Stochastic Neighbor Embedding ist ein nichtlineares Verfahren des maschinellen Lernens, hauptsächlich zur Visualisierung hochdimensionaler Daten|
| t-Verteilung | Verteilung ähnlich der Standardnormalverteilung, setzt allerdings nicht voraus, dass die Standardabweichung der Population bekannt ist |
| UMAP | Uniform Manifold Approximation and Projection - schneller Algorithmus zur Dimensionalitätsreduktion, der lokale und globale Strukturen erhält|


## Hinweis: 
Das dritte Notebook der [heutigen Übungen](https://github.com/neuefische/ds-dimensionality-reduction.git) [(DE)](https://github.com/neuefische/ds-dimensionalitaetsreduktion-de.git) erklärt Support Vector Machines, falls jemand das Thema vertiefen möchte.

 
