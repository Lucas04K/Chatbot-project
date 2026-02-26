# Tag 04, 22.01.2026

Einführung in explanative Datenvisualisierung:

Wie Diagramme Informationen transportieren, wie sie manipulieren können und wie man sie sinnvoll, verständlich und zielgruppengerecht gestaltet.

> Ein Diagramm ist nur dann gut, wenn jemand, der es nicht erstellt hat, sofort versteht, was es sagen soll.

---
## __Grundlegender Überblick__


* Zentrale Kernbotschaft
* Konkrete Beispiele für wissenschaftlichen Betrug
* Warum Plots so gefährlich mächtig sind
* Klassisches Positivbeispiel: Napoleon-Diagramm
* Vergleich konkreter Diagrammtypen
* Zentrale Gestaltungsregeln
* Explorativ vs. Explanativ
* Praktische Übung „Wintersport-Datensätze“


---
##  __Zeitplan__

|Zeit|Inhalt|
|---|---|
|09:00 - 09:50|Daily Review|
|10:00 - 10:45|Erste theoretische Inputs|
|10:45 - 11:17|Übung Diagramm|
|11:17 - 12:30|Weitere theoretische Inputs|
|12:30 - 13:30|Mittagspause| 
|13:30 - 15:00|Praktische Übungen (Visualisierung)|
|15:00 - 15:30|Tägliches Stand-up|
|16:30 - 18:00|Weitere Übungen (Group Work)|


---
## __Erste inhaltliche Notizen__

### 1. Zentrale Kernbotschaft ###
Menschen hinterfragen selten Rohdaten, sondern vertrauen Visualisierungen. Genau deshalb können Plots: aufklären, überzeugen oder manipulieren.
Die Wahl von Diagrammtyp, Skala, Farben und Darstellung ist nie neutral.


### 2. Konkrete Beispiele für wissenschaftlichen Betrug ###
> Lernpunkt: Weil Visualisierungen starkes Vertrauen erzeugen, müssen sie kritisch geprüft werden und tragen eine besondere Verantwortung in Wissenschaft und Öffentlichkeit.

Beispiel 1: Francesca Gino (Psychologie / Verhaltensforschung)
Francesca Gino, Professorin an einer Eliteuniversität, manipulierte ihre eigenen Studiendaten durch Cherry Picking und gezielte Optimierung auf statistische Signifikanz. Der Betrug blieb lange unentdeckt, da die Plots plausibel, sauber und überzeugend wirkten und kaum jemand die Rohdaten prüfte. Konsequenz waren der Verlust von Professur und Tenure sowie ein nachhaltiger Reputationsschaden; 


> Lernpunkt: Auch überzeugende und sauber wirkende Plots können auf manipulierten oder erfundenen Daten beruhen und dürfen nicht unkritisch vertraut werden.

Beispiel 2: Jan Hendrik Schön (Physik, Bell Labs)
Jan Hendrik Schön, ein junger Physiker bei Bell Labs, veröffentlichte in kurzer Zeit außergewöhnlich viele Arbeiten und behauptete bahnbrechende Ergebnisse wie funktionierende organische Transistoren und den Nachweis des Quanten-Hall-Effekts, weshalb er zeitweise als Nobelpreiskandidat galt. Der Betrug bestand darin, dass die Experimente nie durchgeführt wurden und die Daten vollständig aus Modellen und Lehrbüchern erfunden waren; aufgedeckt wurde dies durch auffallend perfekte, zu glatte Diagramme mit identischem Rauschen in mehreren Publikationen. 


### 3. Warum Plots so gefährlich mächtig sind ###
* Niemand liest tausende Messwerte
* Vertrauen entsteht visuell
* Plots ersetzen für viele Menschen die Daten selbst


### 4. Klassisches Positivbeispiel: Napoleon-Diagramm ###
> Lernpunkt:
Eine brillante Grafik ist nicht automatisch für jeden Kontext geeignet.

Die Grafik „Napoleons Marsch nach Moskau“ von Charles Joseph Minard aus dem Jahr 1869 zeigt gleichzeitig die Truppenstärke der französischen Armee, die geografische Route, die Marschrichtung, den Zeitverlauf sowie die Temperatur und vereint damit extrem viele Informationen in einer einzigen Darstellung. Gerade diese hohe Informationsdichte macht die Grafik komplex, aber auch besonders eindrucksvoll und ästhetisch, sodass sie Zeit und Aufmerksamkeit zum Verstehen erfordert. Sie eignet sich daher gut für Museen, Geschichtsbücher und vertiefte Analysen, ist jedoch ungeeignet für schnelle Reports, Magazine oder allgemein verständliche Kurzpräsentationen.


### 5. Vergleich konkreter Diagrammtypen ###
* Tortendiagramme sind nur sinnvoll bei zwei Kategorien oder wenn eine Kategorie extrem dominiert
* Man sollte die beste grafische Darstellung wählen, um die zentrale Information zu vermitteln.
* Negativbeispiel mit Sportdiagramm Figuren wurde gezeigt:  große Spieler-Silhouetten, mehrfach dargestellten Zahlen und fehlender klarer Achsenskalierung, bei dem die Bildgröße falsche Zusammenhänge suggeriert. Dadurch entsteht eine starke Informationsüberladung und visuelle Irreführung: Die Grafik wirkt zwar ästhetisch ansprechend, ist inhaltlich jedoch schwach und schwer korrekt zu interpretieren.


### 6. Zentrale Gestaltungsregeln ###
> * Aufmerksamkeit auf die Hauptbotschaft, die man mit dem Diagramm vermitteln möchte
> * Kennen Sie Ihre Zielgruppe. Wer wird diese Grafik sehen?

* klarer Titel für das Diagramm
* Achsen immer beschriften
* Keine doppelten Informationen
* Keine unnötigen visuellen Effekte
* Diagrammtyp bewusst wählen
* Farben funktional, nicht dekorativ einsetzen
* Legende verdeckt nicht die Daten


### 7. Explorativ vs. Explanativ
Explorative Visualisierung: das Ziel ist ein Muster zu finden. 
* Für die eigene Analyse
* Viele schnelle Plots
* Unsauber erlaubt

Explanative Visualisierung: das Ziel ist Verstehen zu ermöglichen
* Für andere Menschen
* Wenige, gezielte Plots
* Sehr klare Aussage


### 8. Praktische Übung "Wintersport-Datensätze" ###
> Focus: Zusammenhang sichtbar machen ohne mathematische Perfektion

Aufgabe:Handgezeichnetes Diagramm, freie Wahl von Variablen, Diagrammtyp, Darstellung





# Lexikon #
| Begriff | Definition |
|---|---|
| Datenvisualisierung | Grafische Darstellung von Daten mit dem Ziel, Muster, Zusammenhänge oder Aussagen verständlich zu machen. |
| Explanative Visualisierung | Form der Datenvisualisierung, deren Ziel es ist, Ergebnisse gezielt zu erklären und für andere verständlich zu kommunizieren. |
| Explorative Visualisierung | Visualisierung zur eigenen Analyse, um Muster, Ausreißer oder Hypothesen in Daten zu entdecken. |
| Plot | Allgemeiner Begriff für eine grafische Darstellung von Daten (z. B. Balken-, Linien- oder Streudiagramm). |
| Diagrammtyp | Art der grafischen Darstellung (z. B. Balkendiagramm, Tortendiagramm, Scatterplot), die bestimmt, wie Daten wahrgenommen werden. |
| Balkendiagramm | Diagramm zur Darstellung und zum Vergleich von Größen oder Kategorien anhand von Balken. |
| Tortendiagramm | Diagramm zur Darstellung von Anteilen eines Ganzen; nur sinnvoll bei sehr wenigen Kategorien oder extremen Verteilungen. |
| Scatterplot (Streudiagramm) | Diagramm zur Darstellung der Beziehung zwischen zwei numerischen Variablen. |
| Achse | Referenzlinie eines Diagramms (x- oder y-Achse), die Wertebereiche und Skalen definiert. |
| Skalierung | Festlegung, wie numerische Werte visuell abgebildet werden; beeinflusst die Interpretation von Größen und Abständen. |
| Informationsdichte | Menge an Information, die in einer Grafik gleichzeitig dargestellt wird. |
| Informationsüberladung | Zustand, in dem eine Grafik zu viele Informationen enthält und dadurch schwer verständlich wird. |
| Visuelle Irreführung | Fehlinterpretation von Daten durch ungünstige Gestaltung, falsche Skalierung oder visuelle Metaphern. |
| Cherry Picking | Selektive Auswahl von Datenpunkten, um ein gewünschtes Ergebnis oder eine bestimmte Aussage zu stützen. |
| Datenmanipulation | Bewusste Veränderung, Auswahl oder Erfindung von Daten mit dem Ziel, Ergebnisse zu verfälschen. |
| Rauschen (Noise) | Zufällige Schwankungen in Messdaten, die in realen Daten immer auftreten. |
| Perfekte Plots | Unnatürlich glatte oder identische Diagramme, die in realen Messdaten ungewöhnlich sind und auf Manipulation hinweisen können. |
| Zielgruppe | Personengruppe, für die eine Visualisierung erstellt wird und die deren Komplexität und Gestaltung bestimmt. |
| Kontext | Nutzungssituation einer Grafik (z. B. Bericht, Präsentation, Museum), die ihre Gestaltung beeinflusst. |
| Best Practice | Bewährte Vorgehensweise zur klaren, verständlichen und verantwortungsvollen Datenvisualisierung. |


