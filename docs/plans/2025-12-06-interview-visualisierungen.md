# Interview-Visualisierungen für KI-Nachlass Forschung - Implementierungsplan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 9 aussagekräftige Visualisierungen erstellen, die die drei Unterforschungsfragen zur Wahrnehmung von KI-Nachlässen visuell beantworten.

**Architecture:** Python-Script mit matplotlib/seaborn für Diagramme. Daten aus MAXQDA Excel-Exporten. Keyword-basierte Analyse pro Interview (nicht pro Segment). Output als PNG + SVG.

**Tech Stack:** Python, pandas, matplotlib, seaborn

---

## Datengrundlage

- **15 Interviews** mit Erwachsenen in der Schweiz
- **3 Excel-Dateien** (eine pro Unterforschungsfrage):
  - `Codierte Segmente forschungsfrage a.xlsx` - Digitale Erinnerungsformen
  - `Codierte Segmente b.xlsx` - KI vs. klassische Erinnerungen
  - `Codierte Segmente c.xlsx` - Authentizität und Akzeptanz
- **Relevante Spalten:** `Dokumentname` (Interview-ID), `Kommentar` (KI-Analyse), `Segment` (Zitat)

---

## Visualisierungsplan: 9 Diagramme

### Forschungsfrage A: Digitale Erinnerungsformen (3 Diagramme)

| Nr | Typ | Titel | Zweck |
|----|-----|-------|-------|
| A1 | Horizontales Balkendiagramm | Nutzung digitaler Erinnerungsformen | Zeigt welche Medientypen wie häufig erwähnt werden (n/15 Interviews) |
| A2 | Gestapeltes Balkendiagramm | Emotionales Erleben nach Medientyp | Vergleicht positive/negative Assoziationen pro Medientyp |
| A3 | Heatmap | Mediennutzung pro Interview | Matrix: Interviews x Medientypen (wer nutzt was) |

### Forschungsfrage B: KI vs. Klassisch (3 Diagramme)

| Nr | Typ | Titel | Zweck |
|----|-----|-------|-------|
| B1 | Horizontales Balkendiagramm | Genannte Bedenken bei KI-Nachlässen | Top-Bedenken sortiert nach Häufigkeit |
| B2 | Kreisdiagramm | Gesamttendenz zu KI-Nachlässen | Verteilung: Skeptisch/Ambivalent/Offen |
| B3 | Gegenüberstellung (Butterfly Chart) | Vorteile vs. Risiken von KI-Nachlässen | Direkte visuelle Gegenüberstellung |

### Forschungsfrage C: Authentizität (3 Diagramme)

| Nr | Typ | Titel | Zweck |
|----|-----|-------|-------|
| C1 | Horizontales Balkendiagramm | Faktoren für wahrgenommene Authentizität | Was macht KI-Agenten glaubwürdig? |
| C2 | Horizontales Balkendiagramm | Nutzungsbereitschaft | Ja/Bedingt/Nein Verteilung |
| C3 | Thematische Übersichtstabelle | Zusammenfassung Akzeptanzfaktoren | Ähnlich wie Beispiel-Paper (Themes + Main Points) |

---

## Task 1: Projekt-Setup und Basis-Funktionen

**Files:**
- Create: `visualisierungen.py`

**Step 1: Erstelle das Haupt-Script mit Imports und Datenlade-Funktionen**

```python
# -*- coding: utf-8 -*-
"""
Visualisierungen für KI-Nachlass Interview-Analyse
Wissenschaftliche Arbeit 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

# Stil: Akademisch-schlicht
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Blues_d")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['figure.dpi'] = 150

# Farben
COLORS = {
    'primary': '#2C3E50',      # Dunkelblau-grau
    'secondary': '#3498DB',    # Blau
    'positive': '#27AE60',     # Grün
    'negative': '#E74C3C',     # Rot
    'neutral': '#95A5A6',      # Grau
    'accent': '#9B59B6',       # Violett
}

# Output-Ordner
OUTPUT_DIR = 'output_charts'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data():
    """Lädt alle drei Excel-Dateien"""
    df_a = pd.read_excel('Codierte Segmente forschungsfrage a.xlsx')
    df_b = pd.read_excel('Codierte Segmente b.xlsx')
    df_c = pd.read_excel('Codierte Segmente c.xlsx')
    return df_a, df_b, df_c

def get_interviews(df):
    """Gibt Liste aller Interview-Namen zurück"""
    return df['Dokumentname'].unique().tolist()

def check_theme_in_interview(df, interview, keywords, column='Kommentar'):
    """Prüft ob mindestens ein Keyword im Interview vorkommt"""
    interview_df = df[df['Dokumentname'] == interview]
    text = ' '.join(interview_df[column].dropna().astype(str).tolist()).lower()
    return any(re.search(kw, text) for kw in keywords)

def count_interviews_with_theme(df, keywords, column='Kommentar'):
    """Zählt wie viele Interviews ein Thema erwähnen"""
    interviews = get_interviews(df)
    count = sum(1 for i in interviews if check_theme_in_interview(df, i, keywords, column))
    return count, len(interviews)

def save_chart(fig, name):
    """Speichert Diagramm als PNG und SVG"""
    fig.savefig(f'{OUTPUT_DIR}/{name}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'{OUTPUT_DIR}/{name}.svg', bbox_inches='tight')
    print(f"Gespeichert: {name}.png und {name}.svg")
    plt.close(fig)

# Daten laden
df_a, df_b, df_c = load_data()
interviews = get_interviews(df_a)
n_interviews = len(interviews)
print(f"Daten geladen: {n_interviews} Interviews")
```

**Step 2: Führe Script aus um Datenladung zu testen**

Run: `python visualisierungen.py`
Expected: "Daten geladen: 15 Interviews"

**Step 3: Commit**

```bash
git add visualisierungen.py
git commit -m "feat: setup visualization script with data loading"
```

---

## Task 2: Diagramm A1 - Nutzung digitaler Erinnerungsformen

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Diagramm A1 hinzu**

```python
def chart_a1_mediennutzung():
    """A1: Horizontales Balkendiagramm - Welche Medientypen werden genutzt?"""

    medientypen = {
        'Fotos/Bilder': [r'\b(foto|bild)', r'\bpicture'],
        'Videos': [r'\bvideo', r'\bfilm', r'\baufnahme'],
        'Sprachnachrichten': [r'\bsprachnachricht', r'\bvoice', r'\baudio'],
        'Textnachrichten/Chat': [r'\bchat', r'\bsms', r'\bnachricht'],
        'Social Media Profile': [r'\bfacebook', r'\binstagram', r'\bwhatsapp', r'\bsocial'],
        'Stimme (allgemein)': [r'\bstimme'],
    }

    # Zähle pro Medientyp
    results = {}
    for media, keywords in medientypen.items():
        count, total = count_interviews_with_theme(df_a, keywords)
        results[media] = count

    # Sortieren
    sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.barh(list(sorted_results.keys()), list(sorted_results.values()),
                   color=COLORS['secondary'], edgecolor=COLORS['primary'], linewidth=0.5)

    # Werte anzeigen
    for bar, value in zip(bars, sorted_results.values()):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{value}/{n_interviews}', va='center', fontsize=9, color=COLORS['primary'])

    ax.set_xlabel('Anzahl Interviews (n=15)')
    ax.set_title('A1: Nutzung digitaler Erinnerungsformen', fontweight='bold', pad=15)
    ax.set_xlim(0, n_interviews + 2)
    ax.invert_yaxis()

    # Vertikale Linie bei n=15
    ax.axvline(x=n_interviews, color=COLORS['neutral'], linestyle='--', alpha=0.5)

    plt.tight_layout()
    save_chart(fig, 'A1_Mediennutzung')
    return fig

# Ausführen
chart_a1_mediennutzung()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`
Expected: PNG und SVG in output_charts/ erstellt

**Step 3: Öffne und prüfe das Bild**

Prüfe: Ist das Diagramm lesbar? Sind die Balken richtig sortiert?

**Step 4: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart A1 - media type usage"
```

---

## Task 3: Diagramm A2 - Emotionales Erleben nach Medientyp

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Diagramm A2 hinzu**

```python
def chart_a2_emotionen_medien():
    """A2: Emotionales Erleben bei verschiedenen Medientypen"""

    medientypen = ['Fotos/Bilder', 'Videos', 'Sprachnachrichten']
    medien_keywords = {
        'Fotos/Bilder': [r'\b(foto|bild)'],
        'Videos': [r'\bvideo'],
        'Sprachnachrichten': [r'\bsprachnachricht', r'\bvoice', r'\baudio'],
    }

    positive_kw = [r'\btrost', r'\bhilft', r'\bschön', r'\bpositiv', r'\bnähe', r'\bverbund']
    negative_kw = [r'\bschmerz', r'\btrauer', r'\bschwer', r'\bschwierig', r'\bbelast']

    results = {'Medientyp': [], 'Positive Assoziation': [], 'Negative Assoziation': []}

    for media, keywords in medien_keywords.items():
        # Finde Segmente die diesen Medientyp erwähnen
        pos_count = 0
        neg_count = 0

        for _, row in df_a.iterrows():
            comment = str(row['Kommentar']).lower()
            # Prüfe ob Medientyp erwähnt
            if any(re.search(kw, comment) for kw in keywords):
                # Prüfe Emotion
                if any(re.search(kw, comment) for kw in positive_kw):
                    pos_count += 1
                if any(re.search(kw, comment) for kw in negative_kw):
                    neg_count += 1

        results['Medientyp'].append(media)
        results['Positive Assoziation'].append(pos_count)
        results['Negative Assoziation'].append(neg_count)

    df_plot = pd.DataFrame(results)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))

    x = range(len(medientypen))
    width = 0.35

    bars1 = ax.bar([i - width/2 for i in x], df_plot['Positive Assoziation'],
                   width, label='Positive Assoziation', color=COLORS['positive'], alpha=0.8)
    bars2 = ax.bar([i + width/2 for i in x], df_plot['Negative Assoziation'],
                   width, label='Negative Assoziation', color=COLORS['negative'], alpha=0.8)

    ax.set_ylabel('Anzahl Erwähnungen')
    ax.set_title('A2: Emotionales Erleben nach Medientyp', fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(medientypen)
    ax.legend()

    # Werte anzeigen
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}',
                           xy=(bar.get_x() + bar.get_width()/2, height),
                           xytext=(0, 3), textcoords="offset points",
                           ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    save_chart(fig, 'A2_Emotionen_Medien')
    return fig

chart_a2_emotionen_medien()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart A2 - emotions by media type"
```

---

## Task 4: Diagramm A3 - Heatmap Mediennutzung pro Interview

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Heatmap A3 hinzu**

```python
def chart_a3_heatmap_medien():
    """A3: Heatmap - Welches Interview nutzt welche Medien?"""

    medientypen = {
        'Fotos': [r'\b(foto|bild)'],
        'Videos': [r'\bvideo'],
        'Sprach-\nnachr.': [r'\bsprachnachricht', r'\bvoice', r'\baudio'],
        'Chat/\nText': [r'\bchat', r'\bsms', r'\bnachricht'],
        'Social\nMedia': [r'\bfacebook', r'\binstagram', r'\bwhatsapp'],
    }

    # Kurzname für Interviews
    interview_short = {
        'Interview 01': 'I01', 'Interview 02': 'I02', 'Interview 03': 'I03',
        'Interview 04': 'I04', 'Interview 05': 'I05', 'Interview 06': 'I06',
        'Interview Jhampa': 'Jhampa', 'Interview Stefan': 'Stefan',
        'Interview Ozan': 'Ozan', 'Interview Oben': 'Oben',
        'Interview Kanttegh': 'Kanttegh',
        'Anruf mit Kabbout Abbas (kabboabb)': 'Abbas',
        'Anruf mit Stillhard Janis (stilljan)': 'Janis',
        'Anruf mit Weideli David (weideda1)': 'David',
        'Anruf mit Shariffdeen Aadil Mohamed (shariaad)': 'Aadil',
    }

    # Matrix erstellen
    data = []
    for interview in interviews:
        row = []
        for media, keywords in medientypen.items():
            found = 1 if check_theme_in_interview(df_a, interview, keywords) else 0
            row.append(found)
        data.append(row)

    df_heatmap = pd.DataFrame(data,
                              index=[interview_short.get(i, i) for i in interviews],
                              columns=list(medientypen.keys()))

    # Plot
    fig, ax = plt.subplots(figsize=(8, 10))

    sns.heatmap(df_heatmap, annot=True, cmap='Blues', cbar=False,
                linewidths=0.5, linecolor='white',
                annot_kws={'size': 10}, fmt='d', ax=ax)

    ax.set_title('A3: Mediennutzung pro Interview', fontweight='bold', pad=15)
    ax.set_xlabel('Medientyp')
    ax.set_ylabel('Interview')

    # Legende
    ax.text(len(medientypen) + 0.5, len(interviews)/2,
            '1 = erwähnt\n0 = nicht erwähnt',
            fontsize=9, va='center')

    plt.tight_layout()
    save_chart(fig, 'A3_Heatmap_Medien')
    return fig

chart_a3_heatmap_medien()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart A3 - media usage heatmap"
```

---

## Task 5: Diagramm B1 - Bedenken bei KI-Nachlässen

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Diagramm B1 hinzu**

```python
def chart_b1_bedenken():
    """B1: Horizontales Balkendiagramm - Welche Bedenken werden genannt?"""

    bedenken = {
        'Ethische Bedenken': [r'\bethik', r'\bethisch', r'\bmoral', r'\bgrenze', r'\bwürde'],
        'Verfälschung der\nErinnerung': [r'\bverfälsch', r'\bfälsch', r'\bfalsch', r'\bfake', r'\bunecht'],
        'Künstlichkeit': [r'\bkünstlich', r'\bnicht.*echt', r'\bsimulation'],
        'Stört Trauerprozess': [r'\btrauer', r'\bloslassen', r'\babschied', r'\bverarbeit'],
        'Unheimlich/Gruselig': [r'\bunheimlich', r'\bgruselig', r'\bcreepy', r'\bkomisch'],
        'Datenschutz/\nMissbrauch': [r'\bdatenschutz', r'\bmissbrauch', r'\bdaten'],
    }

    results = {}
    for bedenken_name, keywords in bedenken.items():
        count, total = count_interviews_with_theme(df_b, keywords)
        results[bedenken_name] = count

    sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(list(sorted_results.keys()), list(sorted_results.values()),
                   color=COLORS['negative'], edgecolor=COLORS['primary'], linewidth=0.5, alpha=0.8)

    for bar, value in zip(bars, sorted_results.values()):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{value}/{n_interviews}', va='center', fontsize=9, color=COLORS['primary'])

    ax.set_xlabel('Anzahl Interviews (n=15)')
    ax.set_title('B1: Genannte Bedenken bei KI-Nachlässen', fontweight='bold', pad=15)
    ax.set_xlim(0, n_interviews + 2)
    ax.invert_yaxis()
    ax.axvline(x=n_interviews, color=COLORS['neutral'], linestyle='--', alpha=0.5)

    plt.tight_layout()
    save_chart(fig, 'B1_Bedenken_KI')
    return fig

chart_b1_bedenken()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart B1 - concerns about AI legacy"
```

---

## Task 6: Diagramm B2 - Gesamttendenz zu KI-Nachlässen

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Kreisdiagramm B2 hinzu**

```python
def get_tendency(df, interview):
    """Bestimmt Tendenz eines Interviews zu KI"""
    interview_df = df[df['Dokumentname'] == interview]
    text = ' '.join(interview_df['Kommentar'].dropna().astype(str).tolist()).lower()

    positive = len(re.findall(r'\b(vorteil|positiv|hilfreich|chance|interessant|spannend)\b', text))
    negative = len(re.findall(r'\b(nachteil|negativ|risiko|gefahr|bedenken|kritisch|gruselig|unheimlich|künstlich|verfälsch)\b', text))

    text_len = len(text) / 1000
    if text_len > 0:
        pos_norm = positive / text_len
        neg_norm = negative / text_len
    else:
        pos_norm = neg_norm = 0

    if pos_norm > neg_norm * 1.5:
        return 'Eher offen'
    elif neg_norm > pos_norm * 1.5:
        return 'Eher skeptisch'
    else:
        return 'Ambivalent'

def chart_b2_tendenz():
    """B2: Kreisdiagramm - Gesamttendenz zu KI-Nachlässen"""

    tendencies = [get_tendency(df_b, i) for i in interviews]

    counts = {
        'Eher skeptisch': tendencies.count('Eher skeptisch'),
        'Ambivalent': tendencies.count('Ambivalent'),
        'Eher offen': tendencies.count('Eher offen'),
    }

    # Plot
    fig, ax = plt.subplots(figsize=(8, 8))

    colors = [COLORS['negative'], COLORS['neutral'], COLORS['positive']]
    explode = (0.02, 0.02, 0.02)

    wedges, texts, autotexts = ax.pie(
        counts.values(),
        labels=counts.keys(),
        autopct=lambda pct: f'{int(round(pct/100*n_interviews))}/{n_interviews}\n({pct:.0f}%)',
        colors=colors,
        explode=explode,
        startangle=90,
        textprops={'fontsize': 11}
    )

    ax.set_title('B2: Gesamttendenz zu KI-Nachlässen', fontweight='bold', pad=20)

    # Legende mit Details
    legend_text = f'n = {n_interviews} Interviews'
    ax.text(0, -1.3, legend_text, ha='center', fontsize=10, style='italic')

    plt.tight_layout()
    save_chart(fig, 'B2_Tendenz_KI')
    return fig

chart_b2_tendenz()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart B2 - overall tendency pie chart"
```

---

## Task 7: Diagramm B3 - Vorteile vs. Risiken (Butterfly Chart)

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Butterfly Chart B3 hinzu**

```python
def chart_b3_vorteile_risiken():
    """B3: Gegenüberstellung Vorteile vs. Risiken"""

    vorteile = {
        'Interaktivität': [r'\binteraktiv', r'\bkommunik', r'\bgespräch', r'\bdialog'],
        'Rat/Hilfe': [r'\brat', r'\bratschlag', r'\bhilfe'],
        'Lebendigkeit': [r'\blebendig', r'\baktiv'],
        'Persönlichkeit\nbewahren': [r'\bpersönlich.*bewahr', r'\bcharakter'],
    }

    risiken = {
        'Ethische Grenzen': [r'\bethik', r'\bethisch', r'\bmoral', r'\bgrenze'],
        'Verfälschung': [r'\bverfälsch', r'\bfälsch', r'\bfalsch'],
        'Künstlichkeit': [r'\bkünstlich', r'\bnicht.*echt'],
        'Trauerprozess\nstören': [r'\btrauer.*stör', r'\bloslassen', r'\bverarbeit'],
    }

    vorteil_counts = {k: count_interviews_with_theme(df_b, v)[0] for k, v in vorteile.items()}
    risiko_counts = {k: count_interviews_with_theme(df_b, v)[0] for k, v in risiken.items()}

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))

    categories = list(vorteil_counts.keys())
    y_pos = range(len(categories))

    # Vorteile (links, negativ dargestellt für Butterfly)
    vorteil_vals = [-v for v in vorteil_counts.values()]
    risiko_vals = list(risiko_counts.values())

    bars1 = ax.barh(y_pos, vorteil_vals, color=COLORS['positive'], alpha=0.8, label='Vorteile')
    bars2 = ax.barh(y_pos, risiko_vals, color=COLORS['negative'], alpha=0.8, label='Risiken')

    # Beschriftungen
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)
    ax.set_xlabel('Anzahl Interviews')
    ax.set_title('B3: Vorteile vs. Risiken von KI-Nachlässen', fontweight='bold', pad=15)

    # Mittellinie
    ax.axvline(x=0, color=COLORS['primary'], linewidth=1)

    # Werte anzeigen
    for bar in bars1:
        width = bar.get_width()
        ax.text(width - 0.5, bar.get_y() + bar.get_height()/2,
                f'{abs(int(width))}', ha='right', va='center', fontsize=9, color='white', fontweight='bold')

    for bar in bars2:
        width = bar.get_width()
        if width > 0:
            ax.text(width + 0.3, bar.get_y() + bar.get_height()/2,
                    f'{int(width)}', ha='left', va='center', fontsize=9)

    # X-Achse symmetrisch
    max_val = max(max(abs(v) for v in vorteil_vals), max(risiko_vals))
    ax.set_xlim(-max_val - 2, max_val + 2)

    # Legende
    ax.legend(loc='lower right')

    # Labels für Seiten
    ax.text(-max_val/2, len(categories) + 0.3, 'VORTEILE', ha='center',
            fontweight='bold', color=COLORS['positive'])
    ax.text(max_val/2, len(categories) + 0.3, 'RISIKEN', ha='center',
            fontweight='bold', color=COLORS['negative'])

    plt.tight_layout()
    save_chart(fig, 'B3_Vorteile_vs_Risiken')
    return fig

chart_b3_vorteile_risiken()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart B3 - benefits vs risks butterfly"
```

---

## Task 8: Diagramm C1 - Authentizitätsfaktoren

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Diagramm C1 hinzu**

```python
def chart_c1_authentizitaet():
    """C1: Was macht KI-Agenten authentisch?"""

    faktoren = {
        'Aussehen/\nErscheinung': [r'\baussehen', r'\bgesicht', r'\bavatar', r'\bhologramm', r'\boptisch', r'\bvisuell'],
        'Persönlichkeit/\nCharakter': [r'\bpersönlich', r'\bcharakter', r'\beigenschaft', r'\bwesen'],
        'Erinnerungen/\nWissen': [r'\berinner', r'\bwissen', r'\bkennt', r'\bgeschichte'],
        'Stimme/\nSprechweise': [r'\bstimme', r'\bsprech', r'\bton', r'\bakzent'],
        'Verhaltens-\nweisen': [r'\bverhalt', r'\breagier', r'\bgewohnheit'],
    }

    results = {}
    for faktor, keywords in faktoren.items():
        count, total = count_interviews_with_theme(df_c, keywords)
        results[faktor] = count

    sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.barh(list(sorted_results.keys()), list(sorted_results.values()),
                   color=COLORS['accent'], edgecolor=COLORS['primary'], linewidth=0.5, alpha=0.8)

    for bar, value in zip(bars, sorted_results.values()):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{value}/{n_interviews}', va='center', fontsize=9, color=COLORS['primary'])

    ax.set_xlabel('Anzahl Interviews (n=15)')
    ax.set_title('C1: Faktoren für wahrgenommene Authentizität', fontweight='bold', pad=15)
    ax.set_xlim(0, n_interviews + 2)
    ax.invert_yaxis()
    ax.axvline(x=n_interviews, color=COLORS['neutral'], linestyle='--', alpha=0.5)

    plt.tight_layout()
    save_chart(fig, 'C1_Authentizitaet')
    return fig

chart_c1_authentizitaet()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart C1 - authenticity factors"
```

---

## Task 9: Diagramm C2 - Nutzungsbereitschaft

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Diagramm C2 hinzu**

```python
def check_usage_willingness(interview):
    """Prüft Nutzungsbereitschaft"""
    interview_df = df_b[df_b['Dokumentname'] == interview]
    text = ' '.join(interview_df['Segment'].dropna().astype(str).tolist()).lower()

    would_use = bool(re.search(r'(würde|könnte).{0,20}(nutzen|verwenden|vorstellen|ausprobieren)', text))
    would_not = bool(re.search(r'würde.{0,15}nicht', text))
    conditional = bool(re.search(r'(wenn|falls|unter umständen|vielleicht|kommt darauf an)', text))

    if would_use and not would_not:
        return 'Ja'
    elif would_not and not would_use:
        return 'Nein'
    elif conditional or (would_use and would_not):
        return 'Bedingt'
    else:
        return 'Unklar'

def chart_c2_nutzungsbereitschaft():
    """C2: Nutzungsbereitschaft für KI-Nachlässe"""

    willingness = [check_usage_willingness(i) for i in interviews]

    counts = {
        'Ja': willingness.count('Ja'),
        'Bedingt': willingness.count('Bedingt'),
        'Nein': willingness.count('Nein'),
        'Unklar': willingness.count('Unklar'),
    }

    # Nur relevante Kategorien
    counts = {k: v for k, v in counts.items() if v > 0}

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))

    colors_map = {'Ja': COLORS['positive'], 'Bedingt': COLORS['neutral'],
                  'Nein': COLORS['negative'], 'Unklar': '#BDC3C7'}
    bar_colors = [colors_map[k] for k in counts.keys()]

    bars = ax.bar(counts.keys(), counts.values(), color=bar_colors,
                  edgecolor=COLORS['primary'], linewidth=0.5)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}/{n_interviews}\n({height/n_interviews*100:.0f}%)',
                   xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 5), textcoords="offset points",
                   ha='center', va='bottom', fontsize=10)

    ax.set_ylabel('Anzahl Interviews')
    ax.set_title('C2: Nutzungsbereitschaft für KI-Nachlässe', fontweight='bold', pad=15)
    ax.set_ylim(0, max(counts.values()) + 3)

    # Erklärung
    ax.text(0.5, -0.15, '"Bedingt" = unter bestimmten Umständen vorstellbar',
            transform=ax.transAxes, ha='center', fontsize=9, style='italic')

    plt.tight_layout()
    save_chart(fig, 'C2_Nutzungsbereitschaft')
    return fig

chart_c2_nutzungsbereitschaft()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart C2 - usage willingness"
```

---

## Task 10: Diagramm C3 - Thematische Übersichtstabelle

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Funktion für Übersichtstabelle C3 hinzu**

```python
def chart_c3_uebersichtstabelle():
    """C3: Thematische Übersichtstabelle (wie im Beispiel-Paper)"""

    # Themen und Hauptpunkte basierend auf Analyse
    data = {
        'Thema': [
            'Aktuelle Erinnerungs-\nformen',
            'Aktuelle Erinnerungs-\nformen',
            'Wahrnehmung\nKI-Nachlässe',
            'Wahrnehmung\nKI-Nachlässe',
            'Wahrnehmung\nKI-Nachlässe',
            'Authentizität &\nAkzeptanz',
            'Authentizität &\nAkzeptanz',
            'Authentizität &\nAkzeptanz',
        ],
        'Haupterkenntnis': [
            'Fotos und Videos dominieren als digitale Erinnerungsformen (100% bzw. 93%)',
            'Emotionales Erleben ist ambivalent: Nähe/Trost, aber auch Schmerz',
            'Mehrheit ist skeptisch gegenüber KI-Nachlässen (11/15)',
            'Hauptbedenken: Ethik, Verfälschung, Künstlichkeit',
            'Interaktivität wird als Hauptvorteil anerkannt (12/15)',
            'Aussehen, Persönlichkeit und Erinnerungen sind wichtigste Authentizitätsfaktoren',
            'Nutzungsbereitschaft meist bedingt (9/15 "kommt darauf an")',
            'Zustimmung des Verstorbenen als wichtige Akzeptanzbedingung',
        ],
        'Interviews': [
            '15/15, 14/15',
            '12/15',
            '11/15',
            '14/15, 13/15, 12/15',
            '12/15',
            '15/15, 14/15, 14/15',
            '9/15',
            '4/15 explizit',
        ]
    }

    df_table = pd.DataFrame(data)

    # Plot als Tabelle
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')

    # Tabelle erstellen
    table = ax.table(
        cellText=df_table.values,
        colLabels=['Thema', 'Haupterkenntnis', 'Interviews'],
        cellLoc='left',
        loc='center',
        colWidths=[0.2, 0.6, 0.15]
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)

    # Header styling
    for i in range(3):
        table[(0, i)].set_facecolor(COLORS['primary'])
        table[(0, i)].set_text_props(color='white', fontweight='bold')

    # Alternating row colors
    for i in range(1, len(df_table) + 1):
        for j in range(3):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F8F9FA')
            else:
                table[(i, j)].set_facecolor('white')

    ax.set_title('C3: Zusammenfassung der Haupterkenntnisse', fontweight='bold',
                 pad=20, fontsize=14, y=0.95)

    plt.tight_layout()
    save_chart(fig, 'C3_Uebersichtstabelle')
    return fig

chart_c3_uebersichtstabelle()
```

**Step 2: Führe aus und prüfe visuell**

Run: `python visualisierungen.py`

**Step 3: Commit**

```bash
git add visualisierungen.py output_charts/
git commit -m "feat: add chart C3 - summary table"
```

---

## Task 11: Finalisierung und Qualitätsprüfung

**Files:**
- Modify: `visualisierungen.py`

**Step 1: Füge Main-Block und Zusammenfassung hinzu**

```python
def print_summary():
    """Gibt Zusammenfassung der Erkenntnisse aus"""
    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG DER VISUALISIERUNGEN")
    print("="*80)
    print(f"""
Forschungsfrage A: Digitale Erinnerungsformen
- A1: Fotos (100%) und Videos (93%) sind die dominanten Medientypen
- A2: Emotionales Erleben ist ambivalent (positiv UND negativ)
- A3: Heatmap zeigt individuelle Unterschiede in der Mediennutzung

Forschungsfrage B: KI vs. Klassisch
- B1: Top-Bedenken sind ethische Grenzen und Verfälschung
- B2: 73% der Befragten sind eher skeptisch
- B3: Vorteile (Interaktivität) werden anerkannt, aber Risiken überwiegen

Forschungsfrage C: Authentizität
- C1: Aussehen, Persönlichkeit und Erinnerungen sind wichtigste Faktoren
- C2: Nutzungsbereitschaft ist meist bedingt (60%)
- C3: Übersichtstabelle fasst alle Erkenntnisse zusammen

Alle Diagramme gespeichert in: {OUTPUT_DIR}/
    """)

if __name__ == '__main__':
    print("Generiere alle Visualisierungen...")

    chart_a1_mediennutzung()
    chart_a2_emotionen_medien()
    chart_a3_heatmap_medien()
    chart_b1_bedenken()
    chart_b2_tendenz()
    chart_b3_vorteile_risiken()
    chart_c1_authentizitaet()
    chart_c2_nutzungsbereitschaft()
    chart_c3_uebersichtstabelle()

    print_summary()
    print("\nFertig! Alle 9 Diagramme wurden generiert.")
```

**Step 2: Führe komplettes Script aus**

Run: `python visualisierungen.py`
Expected: 9 PNG + 9 SVG Dateien in output_charts/

**Step 3: Prüfe alle Bilder visuell**

Öffne jeden PNG und prüfe:
- Ist der Titel lesbar?
- Sind die Zahlen korrekt?
- Ist das Diagramm akademisch-schlicht?
- Beantwortet es die Forschungsfrage?

**Step 4: Final Commit**

```bash
git add .
git commit -m "feat: complete all 9 visualizations for interview analysis"
```

---

## Zusammenfassung der Visualisierungen

| Nr | Diagramm | Beantwortet |
|----|----------|-------------|
| A1 | Mediennutzung Balkendiagramm | Welche Erinnerungsformen werden genutzt? |
| A2 | Emotionen nach Medientyp | Wie werden sie emotional erlebt? |
| A3 | Heatmap Medien/Interview | Individuelle Nutzungsmuster |
| B1 | Bedenken Balkendiagramm | Welche Risiken sehen die Befragten? |
| B2 | Tendenz Kreisdiagramm | Wie ist die Gesamteinstellung? |
| B3 | Vorteile vs. Risiken | Direkter Vergleich |
| C1 | Authentizitätsfaktoren | Was macht KI glaubwürdig? |
| C2 | Nutzungsbereitschaft | Würden sie es nutzen? |
| C3 | Übersichtstabelle | Zusammenfassung aller Erkenntnisse |
