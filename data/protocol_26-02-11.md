# Tag 17, 11.02.2026

### Grundlagen von CNNs

---

# Lexikon

| Begriff             | Definition                                                                                                                          |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Faltungsschicht     | Schicht mit Kernels zur Merkmalsextraktion aus Bilddaten; durch elementweise Multiplikation und Summation mit Bildbereichen.        |
| Kernel              | Kleine Matrix (z. B. 3x3), die über das Bild gleitet; Parameter, die während des Trainings optimiert werden.                         |
| Stride              | Schrittweite des Kernels beim Gleiten über das Bild; Standard=1, größere Werte reduzieren die Ausgabegröße.                         |
| Padding             | Hinzufügen von Rändern zum Bild (z. B. 'same' oder 'valid'); steuert die Größe der Feature Maps.                                   |
| Feature Map         | Ausgabe einer Faltungsschicht; zeigt erkannte Merkmale (z. B. Kanten, Texturen) in Form einer 2D-Map.                              |
| Max-Pooling         | Pooling-Methode, die maximalen Wert in einem Fenster auswählt; reduziert Dimensionalität und erhöht Translationsinvarianz.           |
| RGB-Bild            | Farbbild mit 3 Kanälen (Rot, Grün, Blau); jede Farbkanal wird separat gefaltet.                                                    |
| Batch-Normalisierung| Normalisiert Aktivierungen pro Batch; stabilisiert Training, erlaubt höhere Lernraten und reduziert Overfitting.                    |
| Dropout             | Regularisierungstechnik, bei der zufällig Neuronen deaktiviert werden; verhindert Co-Adaptation und Overfitting.                   |
| Transferlernen      | Nutzung vortrainierter CNNs (z. B. auf ImageNet) für neue Aufgaben; nur oberen Schichten werden angepasst.                         |
| Datenaugmentation   | Künstliche Erweiterung von Trainingsdaten durch Transformationen (Rotation, Spiegeln, Helligkeitsänderung); erhöht Robustheit.       |

---

## **Grundlegender Überblick**

- CNNs extrahieren hierarchische Merkmale durch Faltungsschichten und Pooling.  
- **Pooling-Schichten** erhöhen die Translationsinvarianz und reduzieren die Dimensionalität.  
- **Datenaugmentation** verhindert Overfitting und erhöht die Robustheit bei begrenzten Daten.  
- **Batch-Normalisierung** stabilisiert das Training und ermöglicht höhere Lernraten.  
- **Transferlernen** ist effizient für Bildverarbeitungsaufgaben mit begrenzten Trainingsdaten.  
- ReLU ist die Standard-Aktivierungsfunktion in Hidden-Layern; Sigmoid wird nur im Output-Layer bei binärer Klassifikation verwendet.  
- **Adversariale Angriffe** erfordern spezielle Techniken wie adversariales Training (Trainieren mit gestörten Beispielen).  

---

## 1. Faltung (Convolution)

- **Kernel**: Kleine Matrix (z. B. 3x3), die über das Bild gleitet. Elementweise Multiplikation mit überlappendem Bildbereich, Summe der Ergebnisse zu einem Pixel der Feature Map.  
- **Stride**: Schrittweite des Kernels (Standard=1). Größerer Stride reduziert die Ausgabegröße.  
- **Padding**: Hinzufügen von Rändern zum Originalbild, um die Feature Map-Größe zu kontrollieren.  
  - `Valid`: Kein Padding → Ausgabegröße = $n - f + 1$  
  - `Same`: Padding so, dass Ausgabegröße = $n$ → $p = \frac{f - 1}{2}$  
- **Farbbilder**: RGB-Bilder haben 3 Kanäle. Jeder Kanal wird mit separaten Filtern gefaltet, dann summiert zu einer Feature Map pro Filter.  

<img src="https://miro.medium.com/max/1400/1*Fw-ehcNBR9byHtho-Rxbtw.gif" alt="Drawing" style="width: 400px;"/>
---

## 2. Pooling

- **Max-Pooling**: Wählt maximalen Wert in einem Fenster (z. B. 2x2). Verstärkt dominante Merkmale, reduziert Dimension.  
- **Average-Pooling**: Bildet Durchschnittswert im Fenster. Weniger häufig, aber manchmal stabil.  
- **Vorteile**:  
  - Reduziert Rechenaufwand um 75% bei 2x2-Pooling.  
  - Erhöht Translation Invariance (Merkmale erkennbar unabhängig von Position).  
  - Schützt vor Überanpassung durch Reduktion der Feature-Details.  

![max_pooling.png](images/max_pooling.png)
---

## 3. Architektur von CNNs

- **Typische Schichten**:  
  `Conv2D → Pooling → Conv2D → Pooling → Flatten → Dense → Output`  
- **Conv2D**:  
  - Filter-Anzahl (z. B. 32, 64, 128) verdoppelt sich pro Schicht.  
  - Kernel-Größe: 3x3 ist Standard (gute Balance zwischen Rechenaufwand und Repräsentationskraft).  
- **Flatten**:  
  - Konvertiert 3D-Feature Maps in 1D-Vektor für Dense-Schichten.  
- **Dense-Schicht**:  
  - Vollverbundene Schicht für Klassifikation (Softmax für Mehrklassen, Sigmoid für binäre Klassifikation).  

**Beispielarchitektur (LeNet-5)**:  
- 2 Conv2D-Schichten mit Pooling  
- 2 Dense-Schichten  
- Output mit Softmax  


![rgb.png](images/rgb.png)

In CNNs verwenden wir im Allgemeinen mehr als einen Filter in jeder Schicht, sodass die dritte Dimension des resultierenden Bildes gleich der Anzahl der verwendeten Filter ist.

![rgb_2.png](images/rgb_2.png)
---

## 4. Regularisierung in CNNs

- **Batch-Normalisierung**:  
  - Normalisiert Aktivierungen pro Batch → stabilisiert Training, erlaubt höhere Lernraten.  
  - Wird **zwischen Conv2D- und Aktivierungsschichten** eingefügt.  
- **Dropout**:  
  - Deaktiviert zufällig 20–50% der Neuronen während Training → verhindert Co-Adaptation.  
  - Wird **nach Dense-Schichten** eingefügt (nicht zwischen Conv2D-Schichten).  
- **Datenaugmentation**:  
  - Rotation (±15°), Spiegeln, Helligkeitsänderung, Zoom → erhöht Trainingsdatenvielfalt.  
  - **Wichtig**: Verhindert, dass das Modell auf Hintergrundartefakte lernt.  

---

## 5. Transferlernen und Datenaugmentation

- **Transferlernen**:  
  - Nutze vortrainierte Modelle (z. B. ResNet50 auf ImageNet).  
  - **Feinabstimmung**: Nur die oberen Schichten neu trainieren (z. B. Dense-Schichten).  
  - **Vorteile**:  
    - 10x weniger Trainingsdaten benötigt.  
    - Schnelleres Training (kein Training von Grund auf).  
- **Datenaugmentation**:  
  - Für kleine Datensätze (z. B. medizinische Bilder) unverzichtbar.  
  - **Praxis-Tipp**: Kombiniere Datenaugmentation mit Transferlernen für maximale Effizienz.  

> ⚠️ **Hinweis**: Bei Transferlernen auf Bildern mit anderen Farbprofilen (z. B. Infrarotbilder) muss die erste Faltungsschicht angepasst werden.

---

## 6. Herausforderungen und Lösungen

- **Überanpassung**:  
  - Lösung: Dropout, BatchNorm, Early Stopping, Datenaugmentation.  
- **Vanishing Gradients**:  
  - Lösung: ReLU-Aktivierung, BatchNorm, Residual Connections (in tiefen Architekturen >50 Schichten).  
- **Adversariale Angriffe**:  
  - Lösung: Adversariales Training (Trainieren mit gestörten Beispielen).  
  - **Beispiel**: "Dazzle-Make-up" (hohe Kontraste im Gesicht) kann Erkennung behindern.  

---

## 7. Praxis-Tipps für CNNs

- **Kernel-Größe**: 3x3 ist Standard (gute Balance zwischen Rechenaufwand und Repräsentationskraft).  
- **Filter-Anzahl**: Verdoppeln pro Schicht (z. B. 32 → 64 → 128).  
- **Lernrate**: Starte mit 0.001, dann mit Learning Rate Scheduling anpassen.  
- **Batch-Größe**: 32–128 (Zweierpotenzen für Effizienz).  
- **Pooling**: Max-Pooling ist meistens die beste Wahl.  
- **Visualisierung**: Feature Maps visualisieren, um zu verstehen, was das Modell lernt (z. B. Kanten in frühen Schichten, Objekte in späten Schichten).  

---

## 8. Tools und Frameworks

- **TensorFlow/Keras**:  
  - Einfache Implementierung von CNNs, gute Dokumentation.  
  - `tf.keras.applications` bietet vortrainierte Modelle (z. B. ResNet, VGG).  
- **PyTorch**:  
  - Flexibler für Forschung, dynamisches Rechenmodell.  
  - `torchvision.models` bietet vortrainierte CNNs (z. B. ResNet, EfficientNet).  
- **Vortrainierte Modelle**:  
  - **ImageNet-Modelle**: Für die meisten Bildverarbeitungsaufgaben geeignet.  
  - **Spezialisierte Modelle**: Z. B. Medizinische Bilder (CheXNet), Satellitenbilder (U-Net).  

---

## 9. Anwendungsbereiche

- **Bildklassifikation**: Erkennung von Objekten (z. B. CIFAR-10, ImageNet).  
- **Objekterkennung**: Lokalisierung und Klassifizierung (z. B. YOLO, Faster R-CNN).  
- **Segmentierung**: Bild in Regionen einteilen (z. B. U-Net für medizinische Bildanalyse).  
- **Autonome Fahrzeuge**: Erkennung von Verkehrszeichen, Fußgängern, Hindernissen.  
- **Medizinische Diagnostik**: Erkennung von Tumoren in Röntgenbildern oder MRT-Scans.  

---

## Hinweise

- **Feature Maps**: Visualisierung zeigt, welche Merkmale von den Filtern erkannt wurden (z. B. Kanten in frühen Schichten, komplexe Objekte in späten Schichten).  
- **ReLU vs. Sigmoid**: ReLU ist Standard in Hidden Layers; Sigmoid nur im Output-Layer für binäre Klassifikation.  
- **Flatten Layer**: Notwendig, um 3D-Feature Maps in 1D für Dense-Schichten zu konvertieren.  
- **Trainingsdauer**: Typisch 10–100 Epochen; frühzeitiges Stoppen bei stagnierendem Validierungsverlust.