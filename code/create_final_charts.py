# -*- coding: utf-8 -*-
"""
Finale Diagramme basierend auf qualitativer Analyse aller 15 Interviews
KI-Agenten als digitaler Nachlass - Schweiz 2025
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Matplotlib Einstellungen
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Output Ordner
os.makedirs('output_charts', exist_ok=True)

print("="*60)
print("ERSTELLE FINALE DIAGRAMME")
print("="*60)

# ============================================================================
# CHART 1: Haeufigste Medien
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

medien_data = {
    'Fotos': 9,
    'Videos': 1,
    'Chatverlaeufe': 1,
    'Muendliche\nGeschichten': 1,
    'Analoge\nMedien': 1,
    'Verschiedene': 2
}

labels = list(medien_data.keys())
values = list(medien_data.values())
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f39c12', '#95a5a6']

bars = ax.bar(labels, values, color=colors, edgecolor='white', linewidth=2)

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{val}', ha='center', fontsize=12, fontweight='bold')

ax.set_ylabel('Anzahl Personen (n=15)', fontsize=11)
ax.set_title('Haeufigste Medien zur Erinnerung an Verstorbene', fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, max(values) + 1.5)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('output_charts/01_Haeufigste_Medien.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 1 erstellt: Haeufigste Medien")


# ============================================================================
# CHART 2: Staerkstes Praesenzgefuehl
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

praesenz_data = {
    'Videos/Stimme': 9,
    'Briefe/Texte': 2,
    'Sprachnachrichten': 1,
    'Fotos (von\nPerson gemacht)': 1,
    'Geschichten': 1,
    'Analoge\nGegenstaende': 1
}

labels = list(praesenz_data.keys())
values = list(praesenz_data.values())
colors = ['#e74c3c', '#3498db', '#f39c12', '#2ecc71', '#9b59b6', '#1abc9c']

bars = ax.barh(labels, values, color=colors, edgecolor='white', linewidth=2)

for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2,
            f'{val}/15', va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Anzahl Personen', fontsize=11)
ax.set_title('Welches Medium vermittelt das staerkste Praesenzgefuehl?', fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, max(values) + 1.5)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('output_charts/02_Staerkstes_Praesenzgefuehl.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 2 erstellt: Staerkstes Praesenzgefuehl")


# ============================================================================
# CHART 3: Personen-Typen
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

typen_data = {
    'Kategorischer\nAblehner': 2,
    'Authentizitaets-\nSkeptiker': 6,
    'Differenziert-\nSkeptisch': 5,
    'Offen-Positiv': 2
}

labels = list(typen_data.keys())
values = list(typen_data.values())
colors = ['#c0392b', '#e74c3c', '#f39c12', '#27ae60']

bars = ax.bar(labels, values, color=colors, edgecolor='white', linewidth=2)

for bar, val in zip(bars, values):
    pct = val/15*100
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            f'{val}', ha='center', fontsize=12, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
            f'{pct:.0f}%', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

ax.set_ylabel('Anzahl Personen (n=15)', fontsize=11)
ax.set_title('Personen-Typen nach KI-Grundhaltung', fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, max(values) + 1.5)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('output_charts/03_Personen_Typen_KI_Haltung.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 3 erstellt: Personen-Typen KI-Haltung")


# ============================================================================
# CHART 4: KI Nutzungsbereitschaft (Pie)
# ============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

nutzung_data = {
    'Definitiv Nein': 4,
    'Nein (mit Einschraenkungen)': 3,
    'Bedingt/Begrenzt': 7,
    'Ja': 1
}

labels = list(nutzung_data.keys())
values = list(nutzung_data.values())
colors = ['#c0392b', '#e74c3c', '#f39c12', '#27ae60']

wedges, texts, autotexts = ax.pie(values, labels=labels, colors=colors, autopct='%1.0f%%',
                                   startangle=90, explode=(0.02, 0.02, 0.02, 0.05))
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

ax.set_title('Wuerden Sie einen KI-Agenten nutzen?', fontsize=14, fontweight='bold', pad=15)

legend_labels = [f'{l} ({v}/15)' for l, v in zip(labels, values)]
ax.legend(wedges, legend_labels, loc='lower right', fontsize=9)

plt.tight_layout()
plt.savefig('output_charts/04_KI_Nutzungsbereitschaft.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 4 erstellt: KI Nutzungsbereitschaft")


# ============================================================================
# CHART 5: Hauptbedenken (SORTIERT nach Groesse)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

# Sortiert nach Groesse (groesste zuerst)
bedenken_data = [
    ('Trauerprozess behindern', 12),
    ('Authentizitaet/Verfaelschung', 10),
    ('Gesellschaftliche Folgen', 7),
    ('Totenruhe/Ethik', 4),
    ('Datenschutz', 2),
]

labels = [x[0] for x in bedenken_data]
values = [x[1] for x in bedenken_data]
colors = plt.cm.Reds(np.linspace(0.8, 0.4, len(labels)))

bars = ax.barh(labels, values, color=colors, edgecolor='white', linewidth=2)

for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{val}/15', va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Anzahl Personen', fontsize=11)
ax.set_title('Hauptbedenken gegenueber KI-Agenten als digitaler Nachlass', fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, max(values) + 2)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('output_charts/05_Hauptbedenken.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 5 erstellt: Hauptbedenken (sortiert)")


# ============================================================================
# CHART 6: Zusammenfassung 3-Panel
# ============================================================================
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: Medien-Nutzung vs Praesenz
ax1 = axes[0]
kategorien = ['Fotos', 'Videos', 'Audio/Text']
nutzung = [9, 1, 5]
praesenz = [1, 9, 5]

x = np.arange(len(kategorien))
width = 0.35
bars1 = ax1.bar(x - width/2, nutzung, width, label='Haeufigste Nutzung', color='#3498db')
bars2 = ax1.bar(x + width/2, praesenz, width, label='Staerkstes Praesenzgefuehl', color='#e74c3c')

ax1.set_xticks(x)
ax1.set_xticklabels(kategorien)
ax1.set_ylabel('Anzahl Personen')
ax1.set_title('Nutzung vs. Praesenzgefuehl', fontweight='bold')
ax1.legend(fontsize=8)
ax1.set_ylim(0, 12)

# Panel 2: KI-Haltung
ax2 = axes[1]
typen = ['Ablehner', 'Skeptiker', 'Differenziert', 'Offen']
werte = [2, 6, 5, 2]
farben = ['#c0392b', '#e74c3c', '#f39c12', '#27ae60']
ax2.bar(typen, werte, color=farben, edgecolor='white', linewidth=2)
ax2.set_ylabel('Anzahl Personen')
ax2.set_title('KI-Grundhaltung', fontweight='bold')
ax2.set_ylim(0, 8)

# Panel 3: Vermaechtnis
ax3 = axes[2]
verm_labels = ['Traditionell', 'KI-Agent']
verm_values = [14, 1]
verm_colors = ['#3498db', '#e74c3c']
bars3 = ax3.bar(verm_labels, verm_values, color=verm_colors, edgecolor='white', linewidth=2)
ax3.set_ylabel('Anzahl Personen')
ax3.set_title('Eigenes Vermaechtnis', fontweight='bold')
ax3.set_ylim(0, 16)

for bar, val in zip(bars3, verm_values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f'{val}', ha='center', fontsize=11, fontweight='bold')

fig.suptitle('Zusammenfassung: KI-Agenten als digitaler Nachlass (n=15)', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('output_charts/06_Zusammenfassung_3Panel.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 6 erstellt: Zusammenfassung 3-Panel")


# ============================================================================
# CHART 7: Vergleichsmatrix
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 10))

interviews = ['I01', 'I02', 'I03', 'I04', 'I05', 'I06', 'I07', 'I08', 'I09', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15']

eigenschaften = [
    'Fotos als\nHauptmedium',
    'Videos\nbenutzt',
    'Vermeidet\nbestimmte\nInhalte',
    'KI\nkritisch',
    'Lehnt KI\nab',
    'Authentizitaet\nwichtig',
    'Traditionelles\nVermaechtnis'
]

matrix_data = [
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 1],
]

matrix = np.array(matrix_data)

cmap = plt.cm.colors.ListedColormap(['#ecf0f1', '#3498db'])
im = ax.imshow(matrix, cmap=cmap, aspect='auto')

ax.set_xticks(np.arange(len(eigenschaften)))
ax.set_yticks(np.arange(len(interviews)))
ax.set_xticklabels(eigenschaften, fontsize=9, rotation=0, ha='center')
ax.set_yticklabels(interviews, fontsize=10)

for i, row_sum in enumerate(matrix.sum(axis=1)):
    ax.text(len(eigenschaften) + 0.3, i, f'{int(row_sum)}/7', va='center', fontsize=9)

for j, col_sum in enumerate(matrix.sum(axis=0)):
    ax.text(j, len(interviews) + 0.5, f'{int(col_sum)}/15', ha='center', fontsize=9, fontweight='bold')

ax.set_title('Vergleichsmatrix aller 15 Interviews\n(blau = trifft zu)', fontsize=14, fontweight='bold', pad=15)

ax.set_xticks(np.arange(-.5, len(eigenschaften), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(interviews), 1), minor=True)
ax.grid(which='minor', color='white', linestyle='-', linewidth=2)

plt.tight_layout()
plt.savefig('output_charts/07_Vergleichsmatrix.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 7 erstellt: Vergleichsmatrix")


# ============================================================================
# CHART 8: KI-Akzeptanz nach Form
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

ki_formen = ['Chatbot', 'Bewegte\nFotos', 'Hologramme', 'Avatare', 'Roboter', 'Fachlicher\nBot']
akzeptiert = [1, 1, 4, 0, 0, 2]
abgelehnt = [13, 0, 2, 3, 8, 0]

x = np.arange(len(ki_formen))
width = 0.35

bars1 = ax.bar(x - width/2, akzeptiert, width, label='Akzeptiert', color='#27ae60', edgecolor='white', linewidth=2)
bars2 = ax.bar(x + width/2, abgelehnt, width, label='Abgelehnt', color='#e74c3c', edgecolor='white', linewidth=2)

for bar in bars1:
    if bar.get_height() > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{int(bar.get_height())}', ha='center', fontsize=10, fontweight='bold', color='#27ae60')
for bar in bars2:
    if bar.get_height() > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{int(bar.get_height())}', ha='center', fontsize=10, fontweight='bold', color='#e74c3c')

ax.set_xticks(x)
ax.set_xticklabels(ki_formen, fontsize=10)
ax.set_ylabel('Anzahl Personen', fontsize=11)
ax.set_title('KI-Akzeptanz nach Form des digitalen Nachlasses', fontsize=14, fontweight='bold', pad=15)
ax.legend(loc='upper right')
ax.set_ylim(0, 16)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('output_charts/08_KI_Akzeptanz_nach_Form.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 8 erstellt: KI-Akzeptanz nach Form")


# ============================================================================
# CHART 9: THEMEN-MATRIX im LaTeX-Style (wie Beispielbild)
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 18))
ax.axis('off')

# Umfassende Themen-Matrix basierend auf allen 3 Forschungsfragen
# FF A: Mediennutzung, FF B: KI vs Klassisch, FF C: Authentizitaet/Grenzen/Kontrolle
table_data = [
    # Thema in Spalte 1, Main Point in Spalte 2, Interviews in Spalte 3
    # Aktuelle Mediennutzung (FF A)
    ['Aktuelle Mediennutzung\n(FF A)', 'Fotos als haeufigste Erinnerungsform', 'I01, I02, I04, I05, I07, I08, I09, I10, I14'],
    ['', 'Videos vermitteln staerkstes Praesenzgefuehl durch Stimme', 'I01, I03, I04, I05, I08, I09, I10, I11, I15'],
    ['', 'Bewusste Vermeidung bestimmter Inhalte (z.B. Krankheitsphase)', 'I02, I03, I04, I05, I06, I07, I11, I13, I15'],
    ['', 'Physische Medien haben besonderen emotionalen Wert', 'I07, I12, I13'],
    ['', 'Handschrift/persoenliche Note wichtiger als Medium selbst', 'I02, I07'],

    # Emotionale Bindung (FF B)
    ['Emotionale Bindung und\nPraesenzgefuehl (FF B)', 'KI kann emotionale Naehe nicht ersetzen', 'I01, I05, I06, I07, I08, I11, I13'],
    ['', 'Echte Aufnahmen werden kuenstlichen vorgezogen', 'I01, I05, I06, I11, I13, I14'],
    ['', 'Stimme/Bewegung erzeugt staerkere Praesenz als statische Bilder', 'I01, I03, I04, I05, I08, I09, I10, I11, I15'],
    ['', 'KI koennte bei ploetzlichem Tod Abschied ermoeglichen', 'I04'],

    # Trauerprozess (FF B)
    ['Trauerprozess und\nBewaeltigung (FF B)', 'KI koennte Loslassen/Abschliessen verhindern', 'I01, I02, I03, I05, I06, I07, I08, I09, I12, I13, I14, I15'],
    ['', 'Zeitlicher Abstand vor KI-Nutzung wichtig', 'I05, I06, I07'],
    ['', 'Zeitliche Begrenzung der Nutzung sinnvoll', 'I03, I15'],
    ['', 'Realisation des Todes ist wichtiger Schritt', 'I07'],

    # Authentizitaet (FF C)
    ['Authentizitaet und\nEchtheit (FF C)', 'KI kann Gefuehle/Persoenlichkeit nicht nachbilden', 'I01, I05, I06, I07, I08, I11, I13'],
    ['', 'Verfaelschung der Person moeglich', 'I01, I02, I05, I06'],
    ['', 'KI koennte Dinge sagen, die Person nie gesagt haette', 'I01, I02, I07'],
    ['', 'Authentizitaet wichtiger als Interaktionsmoeglichkeit', 'I01, I05, I06, I11, I13, I14'],

    # Ethik und Kontrolle (FF C)
    ['Ethik, Totenruhe und\nKontrolle (FF C)', 'Tote sollen ruhen / natuerlicher Zyklus', 'I05, I12, I13, I14'],
    ['', 'Religioese Bedenken gegen KI-Nachlass', 'I05'],
    ['', 'Einwilligung der verstorbenen Person noetig', 'I02, I03, I04, I05, I06, I07, I09, I11, I13'],
    ['', 'Verstorbene Person sollte KI selbst gestalten', 'I02, I03, I04, I05, I06, I07, I09, I11, I13'],
    ['', 'Hinterbliebene sollten Kontrolle haben', 'I01, I10'],

    # Gesellschaft
    ['Gesellschaftliche\nAuswirkungen', 'Tod/Leben verliert an Bedeutung', 'I02, I03, I04, I05, I06, I08, I09'],
    ['', 'Menschsein geht verloren', 'I08'],
    ['', 'Datenschutzbedenken bei Speicherung', 'I02, I03'],
    ['', 'Abhaengigkeit von Technologie', 'I10'],

    # Akzeptierte Formen
    ['Akzeptierte vs.\nabgelehnte KI-Formen', 'Chatbots werden stark abgelehnt', 'I01, I02, I03, I05, I06, I07, I08, I09, I11, I12, I13, I14, I15'],
    ['', 'Hologramme (echte Videos) teilweise akzeptiert', 'I02, I03, I05, I06'],
    ['', 'Fachlicher Bot (Rezepte, Wissen) eher akzeptiert', 'I07, I09'],
    ['', 'Roboter werden stark abgelehnt', 'I01, I02, I03, I07, I09, I10, I11, I13'],

    # Potenzielle Vorteile
    ['Potenzielle Vorteile\nvon KI-Nachlass', 'Interaktionsmoeglichkeit mit Verstorbenen', 'I02, I03, I04'],
    ['', 'Fachwissen/Rezepte weitergeben', 'I07, I09'],
    ['', 'Fuer nachfolgende Generationen (Enkel)', 'I07, I09'],
    ['', 'Abschied finden bei ploetzlichem Tod', 'I04'],
    ['', 'Letzte Fragen stellen koennen', 'I04'],
]

# Tabelle im LaTeX-Style erstellen
table = ax.table(
    cellText=table_data,
    colLabels=['Thema', 'Hauptpunkt', 'Interviews'],
    colWidths=[0.22, 0.53, 0.25],
    loc='center',
    cellLoc='left'
)

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)

# Header formatieren (dunkelblau)
for j in range(3):
    cell = table[(0, j)]
    cell.set_text_props(fontweight='bold', color='white')
    cell.set_facecolor('#2c3e50')
    cell.set_height(0.025)

# Zellen formatieren - abwechselnde Farben, Thema-Zellen grau
current_theme = None
for i, row in enumerate(table_data, start=1):
    theme = row[0]

    # Bestimme Hintergrundfarbe
    if theme:  # Neue Thema-Zeile
        current_theme = theme
        bg_color = '#d5d8dc'  # Grau fuer Thema-Zeile
    else:
        bg_color = '#ffffff' if i % 2 == 0 else '#f8f9fa'

    for j in range(3):
        cell = table[(i, j)]
        cell.set_facecolor(bg_color)
        cell.set_height(0.022)

        # Thema-Text kursiv
        if j == 0 and theme:
            cell.set_text_props(style='italic', fontweight='bold')

ax.set_title('Themen-Matrix: Einflussfaktoren auf die Einstellung zu KI-Agenten als digitaler Nachlass\n(basierend auf 15 Interviews, Schweiz 2025)',
             fontsize=13, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('output_charts/09_Themen_Matrix_Tabelle.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Chart 9 erstellt: Themen-Matrix Tabelle (LaTeX-Style)")


print("\n" + "="*60)
print("ALLE 9 DIAGRAMME ERFOLGREICH ERSTELLT!")
print("="*60)
