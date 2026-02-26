# Tag 22, 17.02.2026

# Natürliche Sprachverarbeitung

## Notizen 

### Motivation: "Unendliche Bibliothek“
- Es gibt unendlich viele Bücher, aber es ist unmöglich, alle zu lesen.
- Wenn alles Wissen existiert - wie findet man das Wahre?
- Hier: alle Zeichenpermutationen existieren, mehr Rauschen als Inhalt

### Natural Language Processing
- Sprache, wie sie gesprochen wird (nicht formalisiert -> natürlich)

### Warum ist Text wichtig?
- Viele Systeme arbeiten mit der Erkennung, Verabeitung und Erzeugung von Sprache

### Arbeiten mit Text
- Algorithem fuktionieren gut mit Zahlen => Sprache als Zahlen umwandeln
- Mehrdeutigkeitsproblem (Ein Thema kann auf unterschiedliche Weisen besprochen werden)
- Granularität (Einzelnes Wort, Satz, Volltext)
- Unstrukturiert (vgl. Tabellendaten)
- Kontext (z.B. Sarkasmus)

### Lokale Darstellung
- Kodierung mit eindeutiger Nummer (Jedes Token wird durch einen Vektor mit genau einer aktiven Position dargestellt)
- Statistische Kodierung
- Matrizen großteils leer

### Verteilte Darstellung
- Word Embeddings
- niedrigdimensionale Vektorrepräsentation
- Bedeutung über mehrere Dimensionen verteilt => Matrizen dicht gefüllt
- Enthält semantische Struktur (ähnliche Wörter sind nah)

` v("Hund") ≈ v("Katze") ` \
\
` v("König") - v("Mann") + v("Frau") ≈ v("Königin") `

### Aufteilung in Token
- Einzelne Wörter als Token
- Ganze Sätze als Token

### N-Gramme
- Eis + creme als 2 Wort Token zusammenfassen (n=2)

### Normalisierung
- Groß / Kleinschreibung kann sehr relevant sein
- "Text-Adventure" Spiel hat nur auf exakt korrekte Antworten reagiert
- S-Key-Folding => Sonderzeichen werden in ASCII Zeichen umgewandelt
	=> Wörter werden vereinheitlicht

###  Stemming
- Grundwort finden (lists -> list, listings -> list)
- Schneidet viel weg => Bedeutung geht leichter verloren


### Lemmatisierung
- Grundwort finden (lists -> list, listings -> listing)
- Aber: Nomen bleiben Nomen, Verben bleiben Verben

### Stopwörter
- Füllwörter entfernen.

## Statistische Kodierung

### Count Vectorizer
- Vektor enthält die Anzahl, wie oft ein Wort vorkommt
- Ein Vektor pro "Satz"
- Ignoriert Kontext / Satzreihenfolge

### TD-IDF
- Term Frequency * Inverse Document Frequency
- Wichtigkeit eines Wortes für Dokument bestimmen
- Bindewörter werden heruntergestuft

### Dokumentenähnlichkeit
- Dokument ist Vektor von Merkmalen
- Ähnlichkeit von Vektoren => Ähnlichkeit von Dokumentenähnlichkeit

### Textklassifizierung
- Logisitische Regression gibt gute Baseling
- AUC-Score als Metrik
- Spam-Erkennung
- Sentiment-Analyse

## Word embeddings
- Vortrainierte Modelle verwenden!
- BackPropagation bei langen texten schlecht, (nur nahe Nachbarn werden betrachtet)
- Transformer können auf alles schaun 

### Continuous Bag of Words
- "One word was (missing) in all that.
- Aus vielen input Wörtern ein verstecktes Wort finden
- Je mehr ein input zum finden beiträgt, desto höher das Gewicht

### Skip-Gramm
- Aus einem Wort den Kontext zu finden
- Assoziationen herausfinden / als Vektor darstellen

### Übersetzer
- Eingabe wird durch encoder gejagt und an decoder gesendet
- Ausgabe wird von decoder zusammengebaut

## Transformer
- Vortrainierte Modelle verwenden! (Hugging Face)

### Zero-Shot Learning
- Sentiment-Analyse
- Bei wenig Daten: Vorhersagen für Dinge treffen, die nicht trainiert wurden.

    ![Zero-Shot-Learning-Gif](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXd2ODR4ajFibm40ZDVhNmxiNGJodW5oMzF0cmY5NmJtZmR1dGNsNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oEgFCYah70Bg985N5b/giphy.gif)
