# Tag 13, 04.02.2026

Einführung in Feature Engineering

---
## __Grundlegender Überblick__

* Was ist Feature Engineering?
* Feature Engineering Techniken
* ColumnTransformers & Pipelines

---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:45|Daily Review|
|10:00 - 11:30|Feature Engineering|
|11:30 - 12:30|Notebooks zu Feature Engineering|
|12:30 - 13:30|Mittagspause| 
|13:30 - 16:00|Notebooks zu Feature Engineering|
|16:00 - 16:30|Tägliches Stand-up|
|16:30 - 18:00|Übungen und Abschluss|


---
## Haupt-Takeaway
**Welche Kunden zahlen ihren Kredit nicht zurück?**
Oft liegt die Antwort weniger im Modell, sondern in den **Features**.

- Gute, domaingetriebene Features können komplexe Modelle schlagen
- **Feature Engineering** ist einer der größten Performance-Hebel
- Ziel: Rohdaten → **aussagekräftige Merkmale**

> **Bessere Features → bessere Modelle**

---
## Was ist Feature Engineering ###

Feature Engineering ist das **Aufbereiten, Transformieren und Erzeugen von Features**, damit Modelle besser lernen.

- Rohdaten verständlicher machen
- Relevante Information verstärken
- Irrelevantes Rauschen reduzieren

> **Features nur am Train-Set entwickeln, um Data Leakage zu vermeiden!**

---
## Feature-Engineering-Techniken

### Missing Values – Imputation

Füllt fehlende Werte durch statistische Methoden:

- Mittelwert / Median / häufigster Wert
- Konstanter Wert  (z. B. Unbekannt)
- Forward Fill / Backward Fill (bei Zeitreihen)

### Kategoriale Kodierung

Wandelt kategoriale Variablen in numerische Werte um:

- **One-Hot Encoding** – für nominale Kategorien (keine Ordnung)
- **Ordinal Encoding** – für geordnete Kategorien
 *Beispiel: klein < mittel < groß*   
 *Anmerkung: Beim One-Hot Encoding ist eine Spalte vollständig durch die anderen erklärbar. Regressionsmodelle können Koeffizienten nicht eindeutig berechnen, deshalb wird eine Spalte entfernt. Siehe Tutorial*

### Diskretisierung (Binning)

Gruppiert numerische Werte in Kategorien:  
*z. B. Alter → Kind, Jugendlicher, Erwachsener, Senior*

### Feature Splitting

Zerlegt komplexe Features in Einzelteile  
*z. B. Datum -> Tag / Monat / Jahr / Period / Wochentag

### Feature Scaling

Bringt Features auf vergleichbare Skalen:

- **Standardisierung (Z-Score)** – Mittelwert 0, Standardabweichung 1
- **Normalisierung (Min-Max)** – Werte zwischen 0 und 1
- **Robust Scaling** – unempfindlich gegen Ausreißer

### Feature Expansion

Erzeugt neue Features aus bestehenden:

- **Polynomiale Features** – z. B. x² aus x
- **Interaktionen** – z. B. Einkommen × Schulden

### Log-Transformation

Komprimiert große Werte, stabilisiert Verteilungen:  
*z. B. Einkommen, Preise*

### RBF-Transformation

Erzeugt weiche Übergänge statt harter Grenzen:  
*Beispiel: Ordinale Features wie Temperaturzonen (kalt (1-4 Grad) < warm (5-8 Grad) < heiß (9-12 Grad))*

## ColumnTransformers & Pipelines

ColumnTransformers und Pipelines strukturieren die Datenvorverarbeitung sauber, reproduzierbar und fehlerfrei.

### ColumnTransformer

Wendet unterschiedliche Transformationen auf verschiedene Spalten parallel an und fügt die Ergebnisse zusammen.

### Pipeline

Verkettet Vorverarbeitung und Modell sequentiell zu einem einzigen Workflow.

> **Zusammen** machen sie Machine Learning **robust und wartbar**.


## Lexikon
|Technik|Nutzen|
|---|---|
|Imputation|Füllt fehlende Werte durch statistische Methoden aus|
|Categorical Encoding|Kodiert kategoriale Merkmale in numerische Werte|
|Discretization|Gruppiert numerische Merkmale in logische Bins|
|Feature Splitting|Zerlegt komplexe Merkmale in aussagekräftige Teile|
|Feature Scaling|Bringt Features auf vergleichbare Skalen|
|Feature Expansion|Leitet neue Merkmale aus bestehenden ab|
|Log Transformation|Behandelt schiefe Verteilungen und komprimiert große Werte|
|Outlier Handling|Kümmert sich um ungewöhnlich hohe/niedrige Werte im Datensatz|
|RBF Transformation|Verwendet eine kontinuierliche Verteilung zur Kodierung ordinaler Merkmale|
|Data Leakage|Wenn Informationen aus Test-Set in Training einfließen (vermeiden!)|
|Kollinearität|Starke Korrelation zwischen Features (kann Modelle destabilisieren)|


### Referenzen
[All about Feature Scaling](https://towardsdatascience.com/all-about-feature-scaling-bcc0ad75cb35/)   
[One Hot Encoding Tutorial](https://www.datacamp.com/de/tutorial/one-hot-encoding-python-tutorial)   
[OpenML](https://www.openml.org/)  
