# Visualisierungen für KI-Nachlass-Studie

## Übersicht

**Forschungsfrage:** Wie werden KI-generierte Agenten als digitale Nachlassform von Erwachsenen in der Schweiz im Jahr 2025 wahrgenommen und akzeptiert?

**Datenbasis:** 926 manuell kodierte Segmente aus 15 Interviews
- FF A (Mediennutzung): 200 Segmente
- FF B (KI vs. Klassisch): 343 Segmente
- FF C (Authentizität): 383 Segmente

**Zielformat:** Wissenschaftlich korrekte Charts für Thesis

---

## Design-Entscheidungen

| Aspekt | Entscheidung |
|--------|--------------|
| Anzahl Charts | 12 (umfassend) |
| Chart-Typen | Mix: Klassisch + Modern je nach Aussage |
| Farbpalette | Divergierend (Blau-Weiß-Rot) für Pro/Contra, Kategorisch für andere |
| Sprache | Deutsch |
| Struktur | Isoliert pro FF + Synthese-Charts |

---

## FF A - Aktuelle digitale Erinnerungsformen (3 Charts)

### A1 - Mediennutzung & Emotionale Intensität
- **Typ:** Horizontale Balken + Punkte/Marker
- **Balken:** Anzahl Interviews die das Medium nutzen (0-15)
- **Punkte/Linie:** Durchschnittliche emotionale Intensität
- **Farben:** Balken blau, Punkte rot
- **Aussage:** "Fotos werden am häufigsten genutzt UND haben höchste emotionale Bedeutung"

### A2 - Heatmap Mediennutzung × Interview
- **Typ:** Heatmap mit binärer Farbkodierung
- **Zeilen:** 15 Interviews (anonymisiert: I01-I15)
- **Spalten:** 6 Medientypen
- **Farben:** Dunkelblau = nutzt, Hellgrau = nutzt nicht
- **Aussage:** "Muster sichtbar: Wer Fotos nutzt, nutzt meist auch Videos"

### A3 - Präsenzgefühl pro Medientyp
- **Typ:** Diverging Bar oder Lollipop Chart
- **Zeigt:** Welches Medium vermittelt stärkste Nähe zur verstorbenen Person
- **Farben:** Divergierend (schwach → stark)
- **Aussage:** "Videos vermitteln stärkstes Präsenzgefühl, gefolgt von Sprachnachrichten"

---

## FF B - KI vs. Klassische Formen (4 Charts)

### B1 - Vorteile vs. Bedenken pro Interview
- **Typ:** Diverging Bar Chart (Schmetterlings-Diagramm)
- **Mitte:** Interview-Namen (I01-I15)
- **Links (rot):** Anzahl Bedenken-Segmente
- **Rechts (blau):** Anzahl Vorteil-Segmente
- **Aussage:** "Bei allen Interviews überwiegen Bedenken, aber Intensität variiert stark"

### B2 - Bedenken-Kategorien gestapelt
- **Typ:** Stacked Horizontal Bar pro Interview
- **Kategorien:** Authentizität, Trauerprozess, Totenruhe/Ethik, Gesellschaft, Manipulation
- **Farben:** 5 unterscheidbare Farben (kategorisch)
- **Aussage:** "Authentizität und Trauerprozess sind die dominanten Bedenken über alle Interviews"

### B3 - Akzeptanz verschiedener KI-Formen
- **Typ:** Radar/Spider Chart
- **Achsen:** Chatbot, Audio, Hologramm, Avatar, Roboter
- **Linien:** 2 Linien - "Würde nutzen" vs. "Lehnt ab"
- **Aussage:** "Chatbot am ehesten akzeptiert, Roboter fast universell abgelehnt"

### B4 - Fluss: Haltung → Bedenken → Nutzung
- **Typ:** Sankey-Diagramm
- **Links:** Grundhaltung (positiv/ambivalent/negativ)
- **Mitte:** Hauptbedenken-Typ
- **Rechts:** Nutzungsbereitschaft (ja/bedingt/nein)
- **Aussage:** "Auch ambivalente Haltung führt meist zu 'bedingt' oder 'nein'"

---

## FF C - Authentizität & Identität (3 Charts)

### C1 - Authentizitäts-Bewertung pro Interview
- **Typ:** Grouped Bar + Linie
- **Balken:** Anzahl Segmente mit Authentizitäts-Thematik pro Interview
- **Linie:** Anteil "kritisch" vs. "thematisiert"
- **Farben:** Balken grau, Linie rot
- **Aussage:** "Authentizität wird in allen Interviews thematisiert, überwiegend kritisch"

### C2 - Grenzen-Heatmap
- **Typ:** Heatmap
- **Zeilen:** 15 Interviews
- **Spalten:** Grenzen-Kategorien (Roboter, Hologramm, Emotional, Nur fachlich, Zeitlich)
- **Farben:** Rot = abgelehnt, Gelb = bedingt, Grün = akzeptiert, Grau = nicht erwähnt
- **Aussage:** "Roboter universell abgelehnt, Hologramme differenziert bewertet"

### C3 - Kontrolle: Wer soll entscheiden?
- **Typ:** Stacked Bar oder Pie Chart
- **Kategorien:** Verstorbene, Hinterbliebene, Beide, Nicht erwähnt
- **Farben:** Kategorisch unterscheidbar
- **Aussage:** "Mehrheit fordert Kontrolle durch Verstorbene zu Lebzeiten"

---

## Synthese (2 Charts)

### S1 - Sankey: Mediennutzung → KI-Haltung → Authentizitäts-Fokus
- **Typ:** Sankey-Diagramm (Flussdiagramm)
- **Links:** Mediennutzung (Fotos/Videos häufig vs. Chat/Social Media selten)
- **Mitte:** KI-Grundhaltung (positiv/ambivalent/negativ)
- **Rechts:** Authentizitäts-Bedenken (kritisch/thematisiert/nicht erwähnt)
- **Farben:** Farbverlauf entlang der Flüsse
- **Aussage:** "Wer klassische Medien bevorzugt, ist auch bei KI authentizitäts-kritischer"

### S2 - Multi-Panel Summary
- **Typ:** 3 kleine Charts nebeneinander (1 Zeile, 3 Spalten)
- **Panel 1 (FF A):** Mini-Balken "Top 3 Medientypen"
- **Panel 2 (FF B):** Mini-Donut "Grundhaltung zu KI"
- **Panel 3 (FF C):** Mini-Balken "Top 3 Bedenken"
- **Farben:** Konsistent über alle Panels
- **Aussage:** "Gesamtbild auf einen Blick: Fotos dominieren, KI skeptisch gesehen, Authentizität Hauptsorge"

---

## Technische Spezifikationen

- **Format:** PNG (300 DPI) + SVG
- **Schriftart:** Sans-serif (Arial oder Helvetica)
- **Schriftgröße:** Titel 14pt, Achsen 10pt, Labels 8pt
- **Größe:** 1200x800px (Einzelcharts), 1800x600px (Multi-Panel)
- **Bibliothek:** Python matplotlib + seaborn, plotly für Sankey

---

## Quelldateien

- `Kodierung_FF_A.xlsx/csv` - 200 Segmente
- `Kodierung_FF_B.xlsx/csv` - 343 Segmente
- `Kodierung_FF_C.xlsx/csv` - 383 Segmente
- `Kodierung_ZUSAMMENFASSUNG.xlsx/csv` - 15 Interviews
