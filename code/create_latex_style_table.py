# -*- coding: utf-8 -*-
"""
Themen-Matrix im LaTeX-Style (wie akademische Paper)
Saubere Tabelle mit horizontalen Linien bei Themenwechsel
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import numpy as np

# Matplotlib Einstellungen für serifen-Font (wie LaTeX)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'Georgia']
plt.rcParams['axes.unicode_minus'] = False

print("Erstelle Themen-Matrix im LaTeX-Style...")

# Daten gruppiert nach Themen
themes_data = [
    {
        'theme': 'Aktuelle Mediennutzung\n(FF A)',
        'points': [
            ('Fotos als häufigste Erinnerungsform', 'I01, I02, I04, I05, I07, I08, I09, I10, I14'),
            ('Videos vermitteln stärkstes Präsenzgefühl durch Stimme', 'I01, I03, I04, I05, I08, I09, I10, I11, I15'),
            ('Bewusste Vermeidung bestimmter Inhalte (z.B. Krankheitsphase)', 'I02, I03, I04, I05, I06, I07, I11, I13, I15'),
            ('Physische Medien haben besonderen emotionalen Wert', 'I07, I12, I13'),
            ('Handschrift/persönliche Note wichtiger als Medium selbst', 'I02, I07'),
        ]
    },
    {
        'theme': 'Emotionale Bindung und\nPräsenzgefühl (FF B)',
        'points': [
            ('KI kann emotionale Nähe nicht ersetzen', 'I01, I05, I06, I07, I08, I11, I13'),
            ('Echte Aufnahmen werden künstlichen vorgezogen', 'I01, I05, I06, I11, I13, I14'),
            ('Stimme/Bewegung erzeugt stärkere Präsenz als statische Bilder', 'I01, I03, I04, I05, I08, I09, I10, I11, I15'),
            ('KI könnte bei plötzlichem Tod Abschied ermöglichen', 'I04'),
        ]
    },
    {
        'theme': 'Trauerprozess und\nBewältigung (FF B)',
        'points': [
            ('KI könnte Loslassen/Abschliessen verhindern', 'I01, I02, I03, I05, I06, I07, I08, I09, I12, I13, I14, I15'),
            ('Zeitlicher Abstand vor KI-Nutzung wichtig', 'I05, I06, I07'),
            ('Zeitliche Begrenzung der Nutzung sinnvoll', 'I03, I15'),
            ('Realisation des Todes ist wichtiger Schritt', 'I07'),
        ]
    },
    {
        'theme': 'Authentizität und\nEchtheit (FF C)',
        'points': [
            ('KI kann Gefühle/Persönlichkeit nicht nachbilden', 'I01, I05, I06, I07, I08, I11, I13'),
            ('Verfälschung der Person möglich', 'I01, I02, I05, I06'),
            ('KI könnte Dinge sagen, die Person nie gesagt hätte', 'I01, I02, I07'),
            ('Authentizität wichtiger als Interaktionsmöglichkeit', 'I01, I05, I06, I11, I13, I14'),
        ]
    },
    {
        'theme': 'Ethik, Totenruhe und\nKontrolle (FF C)',
        'points': [
            ('Tote sollen ruhen / natürlicher Zyklus', 'I05, I12, I13, I14'),
            ('Religiöse Bedenken gegen KI-Nachlass', 'I05'),
            ('Einwilligung der verstorbenen Person nötig', 'I02, I03, I04, I05, I06, I07, I09, I11, I13'),
            ('Verstorbene Person sollte KI selbst gestalten', 'I02, I03, I04, I05, I06, I07, I09, I11, I13'),
            ('Hinterbliebene sollten Kontrolle haben', 'I01, I10'),
        ]
    },
    {
        'theme': 'Gesellschaftliche\nAuswirkungen',
        'points': [
            ('Tod/Leben verliert an Bedeutung', 'I02, I03, I04, I05, I06, I08, I09'),
            ('Menschsein geht verloren', 'I08'),
            ('Datenschutzbedenken bei Speicherung', 'I02, I03'),
            ('Abhängigkeit von Technologie', 'I10'),
        ]
    },
    {
        'theme': 'Akzeptierte vs. abgelehnte\nKI-Formen',
        'points': [
            ('Chatbots werden stark abgelehnt', 'I01, I02, I03, I05, I06, I07, I08, I09, I11, I12, I13, I14, I15'),
            ('Hologramme (echte Videos) teilweise akzeptiert', 'I02, I03, I05, I06'),
            ('Fachlicher Bot (Rezepte, Wissen) eher akzeptiert', 'I07, I09'),
            ('Roboter werden stark abgelehnt', 'I01, I02, I03, I07, I09, I10, I11, I13'),
        ]
    },
    {
        'theme': 'Potenzielle Vorteile\nvon KI-Nachlass',
        'points': [
            ('Interaktionsmöglichkeit mit Verstorbenen', 'I02, I03, I04'),
            ('Fachwissen/Rezepte weitergeben', 'I07, I09'),
            ('Für nachfolgende Generationen (Enkel)', 'I07, I09'),
            ('Abschied finden bei plötzlichem Tod', 'I04'),
            ('Letzte Fragen stellen können', 'I04'),
        ]
    },
]

# Berechne Gesamtzahl der Zeilen
total_rows = sum(len(t['points']) for t in themes_data)
print(f"Gesamtzahl Zeilen: {total_rows}")

# Figure erstellen
fig, ax = plt.subplots(figsize=(14, 18))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Spaltenbreiten und Positionen
col_widths = [0.18, 0.52, 0.28]
col_starts = [0.01, 0.19, 0.71]

# Zeilenhöhe
row_height = 0.024
header_height = 0.025
y_start = 0.95

# Titel
fig.suptitle('Themen-Matrix: Einflussfaktoren auf die Einstellung zu KI-Agenten als digitaler Nachlass\n(basierend auf 15 Interviews, Schweiz 2025)',
             fontsize=12, fontweight='bold', y=0.98, family='serif')

# Header zeichnen
y = y_start
headers = ['Thema', 'Hauptpunkt', 'Interviews']
for i, header in enumerate(headers):
    ax.text(col_starts[i] + 0.01, y - header_height/2, header,
            fontsize=10, fontweight='bold', va='center', family='serif')

# Dicke Linie unter Header
y -= header_height
ax.plot([0.01, 0.99], [y, y], 'k-', linewidth=1.5)

# Daten zeichnen
for theme_idx, theme_data in enumerate(themes_data):
    theme_name = theme_data['theme']
    points = theme_data['points']

    # Dünne Linie vor jedem Thema (ausser erstem)
    if theme_idx > 0:
        ax.plot([0.01, 0.99], [y, y], 'k-', linewidth=0.5)

    # Thema-Text (kursiv, nur bei erster Zeile des Themas)
    theme_rows = len(points)
    theme_y_center = y - (theme_rows * row_height) / 2

    # Für mehrzeilige Themen
    ax.text(col_starts[0] + 0.01, theme_y_center, theme_name.replace('\n', '\n'),
            fontsize=9, fontstyle='italic', va='center', family='serif',
            linespacing=1.2)

    # Hauptpunkte und Interviews
    for point_idx, (hauptpunkt, interviews) in enumerate(points):
        row_y = y - row_height/2

        # Hauptpunkt
        ax.text(col_starts[1] + 0.01, row_y, hauptpunkt,
                fontsize=9, va='center', family='serif')

        # Interviews
        ax.text(col_starts[2] + 0.01, row_y, interviews,
                fontsize=8, va='center', family='serif')

        y -= row_height

# Linie ganz unten
ax.plot([0.01, 0.99], [y, y], 'k-', linewidth=0.5)

plt.savefig('output_charts/09_Themen_Matrix_Tabelle.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("LaTeX-Style Tabelle erstellt: output_charts/09_Themen_Matrix_Tabelle.png")


# ============================================================================
# MARKDOWN VERSION
# ============================================================================

markdown_content = """# Themen-Matrix: Einflussfaktoren auf die Einstellung zu KI-Agenten als digitaler Nachlass

*Basierend auf 15 Interviews, Schweiz 2025*

---

| Thema | Hauptpunkt | Interviews |
|-------|------------|------------|
| *Aktuelle Mediennutzung (FF A)* | Fotos als häufigste Erinnerungsform | I01, I02, I04, I05, I07, I08, I09, I10, I14 |
| | Videos vermitteln stärkstes Präsenzgefühl durch Stimme | I01, I03, I04, I05, I08, I09, I10, I11, I15 |
| | Bewusste Vermeidung bestimmter Inhalte (z.B. Krankheitsphase) | I02, I03, I04, I05, I06, I07, I11, I13, I15 |
| | Physische Medien haben besonderen emotionalen Wert | I07, I12, I13 |
| | Handschrift/persönliche Note wichtiger als Medium selbst | I02, I07 |
| *Emotionale Bindung und Präsenzgefühl (FF B)* | KI kann emotionale Nähe nicht ersetzen | I01, I05, I06, I07, I08, I11, I13 |
| | Echte Aufnahmen werden künstlichen vorgezogen | I01, I05, I06, I11, I13, I14 |
| | Stimme/Bewegung erzeugt stärkere Präsenz als statische Bilder | I01, I03, I04, I05, I08, I09, I10, I11, I15 |
| | KI könnte bei plötzlichem Tod Abschied ermöglichen | I04 |
| *Trauerprozess und Bewältigung (FF B)* | KI könnte Loslassen/Abschliessen verhindern | I01, I02, I03, I05, I06, I07, I08, I09, I12, I13, I14, I15 |
| | Zeitlicher Abstand vor KI-Nutzung wichtig | I05, I06, I07 |
| | Zeitliche Begrenzung der Nutzung sinnvoll | I03, I15 |
| | Realisation des Todes ist wichtiger Schritt | I07 |
| *Authentizität und Echtheit (FF C)* | KI kann Gefühle/Persönlichkeit nicht nachbilden | I01, I05, I06, I07, I08, I11, I13 |
| | Verfälschung der Person möglich | I01, I02, I05, I06 |
| | KI könnte Dinge sagen, die Person nie gesagt hätte | I01, I02, I07 |
| | Authentizität wichtiger als Interaktionsmöglichkeit | I01, I05, I06, I11, I13, I14 |
| *Ethik, Totenruhe und Kontrolle (FF C)* | Tote sollen ruhen / natürlicher Zyklus | I05, I12, I13, I14 |
| | Religiöse Bedenken gegen KI-Nachlass | I05 |
| | Einwilligung der verstorbenen Person nötig | I02, I03, I04, I05, I06, I07, I09, I11, I13 |
| | Verstorbene Person sollte KI selbst gestalten | I02, I03, I04, I05, I06, I07, I09, I11, I13 |
| | Hinterbliebene sollten Kontrolle haben | I01, I10 |
| *Gesellschaftliche Auswirkungen* | Tod/Leben verliert an Bedeutung | I02, I03, I04, I05, I06, I08, I09 |
| | Menschsein geht verloren | I08 |
| | Datenschutzbedenken bei Speicherung | I02, I03 |
| | Abhängigkeit von Technologie | I10 |
| *Akzeptierte vs. abgelehnte KI-Formen* | Chatbots werden stark abgelehnt | I01, I02, I03, I05, I06, I07, I08, I09, I11, I12, I13, I14, I15 |
| | Hologramme (echte Videos) teilweise akzeptiert | I02, I03, I05, I06 |
| | Fachlicher Bot (Rezepte, Wissen) eher akzeptiert | I07, I09 |
| | Roboter werden stark abgelehnt | I01, I02, I03, I07, I09, I10, I11, I13 |
| *Potenzielle Vorteile von KI-Nachlass* | Interaktionsmöglichkeit mit Verstorbenen | I02, I03, I04 |
| | Fachwissen/Rezepte weitergeben | I07, I09 |
| | Für nachfolgende Generationen (Enkel) | I07, I09 |
| | Abschied finden bei plötzlichem Tod | I04 |
| | Letzte Fragen stellen können | I04 |

---

## Zusammenfassung der Themen

### FF A: Aktuelle Mediennutzung
- **Fotos** sind das häufigste Medium (9/15)
- **Videos mit Stimme** vermitteln das stärkste Präsenzgefühl (9/15)
- Viele vermeiden bewusst bestimmte Inhalte wie Krankheitsphasen

### FF B: KI vs. Klassische Erinnerungen
- KI kann emotionale Nähe nicht ersetzen (7/15)
- Bedenken: KI könnte Loslassen/Abschliessen verhindern (12/15)
- Einziger klarer Vorteil: Abschied bei plötzlichem Tod (I04)

### FF C: Authentizität, Grenzen, Kontrolle
- Authentizität ist zentral - KI kann Persönlichkeit nicht nachbilden (7/15)
- Einwilligung der verstorbenen Person wird als nötig erachtet (9/15)
- Totenruhe-Bedenken bei 4/15 Personen
"""

with open('output_charts/09_Themen_Matrix_Tabelle.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("Markdown Version erstellt: output_charts/09_Themen_Matrix_Tabelle.md")
print("\nFertig!")
