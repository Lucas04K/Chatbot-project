# Tag 23, 18.02.2026

# Clustering-Algorithmen

---

## Recap

- Spamerkennung
  - GMX (Statistik, XGBoost?)
  - GMAIL (Statistik, Transformer?)

- Hugging Face
  - Ästhetik, ursprünglich ein Chatbot Startup für Teenager
  - Bietet gute Tutorien an


---

## Anekdote

Autor Borges  
Enzyklopädie "Emporio celestial de conocimientos benévolos"  
Klassifizierung von  Tieren, wenn auch nach eher absurden Kriterien

---

## Haupt Take-Away

Clustering ist unbeaufsichtigtes Lernen – ähnliche Punkte werden gruppiert, ohne Labels. Die drei Hauptalgorithmen unterscheiden sich grundlegend: **K-Means** ist schnell, braucht aber k als Vorgabe und setzt kugelförmige Cluster voraus. **Hierarchisches Clustering** baut eine Cluster-Hierarchie schrittweise auf (sichtbar im Dendrogramm). **DBSCAN** erkennt dichte Regionen beliebiger Form, markiert Rauschen explizit und bestimmt die Clusteranzahl selbst – dafür sind `eps` und `min_samples` entscheidend.

---

## Inhalt

### 1. Einordnung

Clustering ist neben Dimensionsreduktion (PCA, t-SNE) eine der Hauptmethoden des unbeaufsichtigten Lernens.
- Ziel: ähnliche Beobachtungen gruppieren, ohne Labels.
- Typische Anwendungen: Kundensegmentierung, Anomalieerkennung, Empfehlungssysteme.

**Wichtig:** Features vor dem Clustering skalieren – sonst dominieren Variablen mit großem Wertebereich.

---

### 2. Ähnlichkeitsmaße

- **Euklidisch**: geometrische Luftlinie (Standard bei K-Means und Ward).
- **Manhattan**: Summe der absoluten Differenzen (robuster gegenüber Ausreißern).
- **Minkowski**: Verallgemeinerung mit Parameter k.
- **Kosinus-Ähnlichkeit**: Winkel zwischen Vektoren; relevant bei Text-/Frequenzdaten.
- **Jaccard-Index**: Ähnlichkeit von Mengen, z. B. bei binären Features.

---

### 3. K-Means

**Idee:** k Zentroide so platzieren, dass die Intra-Cluster-Abstände (Trägheit) minimiert werden.

**Algorithmus:**
1. Zufällige Initialisierung von k Zentroiden (k-means++ wählt gut verteilte Startpunkte).
2. Jeden Punkt dem nächsten Zentroid zuweisen.
3. Zentroide als Mittelwert der zugehörigen Punkte neu berechnen.
4. Wiederholen bis Konvergenz.

**Wahl von k:**
- **Ellbogen-Methode**: Trägheit über k plotten; optimales k am Knick.
- **Silhouetten-Plot**: Koeffizienten pro Cluster vergleichen; alle „Messer" sollten die Durchschnittslinie überschreiten und ähnlich groß sein.

| Vorteile | Nachteile |
|----------|-----------|
| Sehr schnell | Setzt kugelförmige, gleich große Cluster voraus |
| Einfach interpretierbar | k muss vorab festgelegt werden |
| k kann aus Anforderungen vorgegeben werden | Ergebnis abhängig von Initialisierung (lok. Minimum) |
| | Kein Umgang mit Rauschen |

---

### 4. Hierarchisches Clustering (Agglomerativ)

**Idee:** Bottom-up – jede Beobachtung startet als eigenes Cluster; die zwei ähnlichsten werden schrittweise zusammengeführt.

**Linkage-Methoden:**
- **Ward**: minimiert quadrierte Differenzen innerhalb der Cluster (robusteste Methode).
- **Complete**: maximaler Abstand zwischen Punkten zweier Cluster.
- **Average**: Durchschnitt aller paarweisen Abstände.
- **Single**: minimaler Abstand (neigt zu elongierten Clustern).

**Dendrogramm:** y-Achse = Unähnlichkeit bei Zusammenführung. Optimale Clusteranzahl: größter vertikaler Sprung ohne Kreuzung einer horizontalen Linie.

| Vorteile | Nachteile |
|----------|-----------|
| Keine Annahme kugelförmiger Cluster | Skaliert schlecht (O(n³)) |
| Stabil (keine zufällige Initialisierung) | Kein Umgang mit Rauschen |
| Dendrogramm gibt Einblick in Hierarchie | Lokal greedy, nicht global optimal |

---

### 5. DBSCAN  
Density-based spatial clustering of applications with noise

**Idee:** Cluster als dichte Regionen, getrennt durch leere Bereiche. Punkte mit wenig Nachbarn = Rauschen.

**Hyperparameter:**
- `eps`: maximaler Radius, innerhalb dessen Punkte als Nachbarn gelten.
- `min_samples`: Mindestanzahl Punkte innerhalb von `eps` für einen Kernpunkt.

**Drei Punkttypen:**
- **Kern-Punkt**: ≥ `min_samples` Nachbarn im Radius `eps`.
- **Grenzpunkt**: liegt im `eps`-Bereich eines Kernpunkts, hat selbst aber weniger Nachbarn.
- **Rausch-Punkt**: weder Kern- noch Grenzpunkt → kein Cluster.

**Wahl von eps:** `NearestNeighbors` mit `n_neighbors = min_samples` fitten, Abstände sortieren und plotten → eps am Punkt maximaler Krümmung.

| Vorteile | Nachteile |
|----------|-----------|
| Clusteranzahl automatisch | Schwierig bei unterschiedlicher Dichte |
| Beliebige Clusterformen | Sensitiv gegenüber `eps` und `min_samples` |
| Rauschen explizit markiert | |
| Stabil und reproduzierbar | |

---

### 6. Vergleich

| Aspekt | K-Means | Hierarchisch | DBSCAN |
|--------|---------|--------------|--------|
| Clusteranzahl | vorab (k) | vorab (n_clusters) | automatisch |
| Clusterform | kugelförmig | flexibler | beliebig |
| Rauschen | alle zugewiesen | alle zugewiesen | explizit als Noise |
| Geschwindigkeit | sehr schnell | langsam bei großen Daten | sehr schnell |
| Stabilität | zufällige Initialisierung | stabil | stabil |

---

## Lexikon

| Wording | Definition |
|---------|------------|
| Clustering | Unbeaufsichtigtes Verfahren zur Gruppierung ähnlicher Datenpunkte ohne Labels. |
| Zentroid | Mittelpunkt eines Clusters; n-dimensionaler Mittelwert aller zugehörigen Beobachtungen. |
| Trägheit (Inertia) | Within-Cluster-Sum-of-Squares; wird von K-Means minimiert. |
| Ellbogen-Methode | Trägheit über k plotten; optimales k am Knick der Kurve. |
| Silhouetten-Koeffizient | Cluster-Qualität zwischen -1 und +1; nahe 1 = gut, nahe 0 = überlappend, nahe -1 = falsch zugewiesen. |
| Dendrogramm | Baumdiagramm zur Visualisierung hierarchischer Cluster. |
| Linkage | Methode zur Abstandsberechnung zwischen Clustern (Ward, Complete, Average, Single). |
| Agglomerativ | Bottom-up: jede Beobachtung startet als eigenes Cluster. |
| DBSCAN | Dichtebasierter Algorithmus, der Rauschen explizit behandelt. |
| Kern-Punkt | Punkt mit ≥ `min_samples` Nachbarn im Radius `eps`. |
| Grenzpunkt | Im `eps`-Bereich eines Kernpunkts, selbst aber < `min_samples` Nachbarn. |
| Rauschen (Noise) | Punkte, die keinem Cluster zugewiesen werden. |
| eps (Epsilon) | Maximale Distanz zwischen zwei Punkten, um als Nachbarn zu gelten. |
| min_samples | Mindestanzahl Punkte innerhalb von `eps` für einen Kernpunkt. |
| Euklidischer Abstand | Geometrische Luftlinie: $d = \sqrt{\sum(a_i - b_i)^2}$. |
| Manhattan-Abstand | Summe der absoluten Differenzen aller Dimensionen. |
