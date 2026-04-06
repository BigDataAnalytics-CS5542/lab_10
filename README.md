# Digital Sentinels: AI-Driven Risk Signal Detection for Substance Abuse

**CS 5542 Big Data Analytics and Applications — Lab 10**  
**UMKC 2026 Spring Research-A-Thon — NSF NRT AI Challenge**

---

## Team

| Name | Role |
|---|---|
| Kenneth | Data Engineering, Preprocessing, Modeling, Report, Video Production |
| Blake Simpson | ML Pipeline, Visualizations, GitHub |
| Rohan Ashraf Hashmi | Submissions |

---

## Demo Video

🎥 [Watch the 3-minute demo](https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b2c82bcf-a54f-4a1b-b5ef-b42400a3ec95)

---

## Problem Statement

Substance abuse is a critical public health crisis. Early warning signals frequently emerge in digital environments — such as medical review forums — before manifesting in clinical data. **Digital Sentinels** is an AI-driven pipeline that identifies risk signals related to substance dependency from public, anonymized drug reviews, producing interpretable population-level insights to support early public health awareness.

---

## Dataset

| Field | Detail |
|---|---|
| **Source** | [UCI KUC Hackathon Winter 2018 — Drug Reviews](https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018) |
| **Size** | ~160,000 patient drug reviews |
| **Fields** | review text, drug name, condition, rating, date |

**Setup:** Download the dataset from the link above and place the raw CSV files in `data/raw/` before running the pipeline.

---

## System Pipeline

```
Phase 1 — Risk Signal Detection
────────────────────────────────────────────────────────
Raw CSV
  → loader.py          (batch streaming + Pydantic validation)
  → preprocessor.py    (regex: strip HTML, normalize text)
  → detection/engine.py
      ├── RuleDetector      (regex match: substance + distress terms)
      └── EmbeddingDetector (all-MiniLM-L6-v2 semantic similarity)
  → processed_signals.csv + embeddings.npz

Phase 2 — Temporal & Behavioral Analysis
────────────────────────────────────────────────────────
processed_signals.csv + embeddings.npz
  → notebooks/processing_results.ipynb
      ├── Spike Detection    (Z-score on drug risk scores over time)
      ├── KMeans Clustering  (group distress vectors semantically)
      └── TF-IDF Extraction  (keywords per cluster → narratives)
  → visualizations/
```

---

## Methods

**Hybrid Detection Engine (`src/detection/engine.py`)**
- **Rule-Based:** Compiled regex patterns match substance terms (opioids, stimulants, benzodiazepines, alcohol) and distress keywords (relapse, withdrawal, suicidal, cravings)
- **Semantic Embedding:** `all-MiniLM-L6-v2` computes cosine similarity against 3 distress anchor phrases. Score > 0.55 = high semantic risk. Both detectors firing boosts final score by +0.3.

**Phase 2 Analysis (`notebooks/processing_results.ipynb`)**
- Z-score spike detection identifies when a drug's risk score statistically deviates from its baseline
- K-Means clustering on embeddings groups mathematically similar distress patterns
- TF-IDF extracts top keywords per cluster to produce human-readable narratives

---

## Installation

Requires Python 3.8+.

```bash
git clone https://github.com/<your-username>/lab_10.git
cd lab_10
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the Project

**Step 1 — Signal Detection**
```bash
python main.py
```
> ⚠️ Embedding generation takes **30–40 minutes** on most hardware.

Outputs: `data/processed_signals.csv` (160K rows) and `data/embeddings.npz`

**Step 2 — Clustering & Visualization**

Open and run all cells in `notebooks/processing_results.ipynb`. Charts are saved to `visualizations/`.

---

## Key Findings

K-Means clustering on 160,000 reviews isolated 4 distinct behavioral narratives:

| Cluster | Label | Top Keywords | Insight |
|---|---|---|---|
| 0 | Mental Health & Psychological Distress | anxiety, withdrawal, suicidal, depression | Psychiatric toll of dependency or rapid cessation of neuro-active medications |
| 1 | Physical Dependency & Pain Management | pain, withdrawal, months, years, effects | Chronic pain patients facing opioid dependency and diminishing returns |
| 2 | Semantic False Positive — Side Effects | weight, lost, cravings, eat, started | Food/weight-loss "cravings" isolated from drug-dependency signals |
| 3 | Medication-Assisted Treatment & Recovery | suboxone, methadone, day, years, life | Recovery journeys and MAT tapering complexity |

---

## Project Structure

```
lab_10/
├── main.py                        # Phase 1 entry point
├── requirements.txt
├── data/
│   ├── README.md                  # Dataset download instructions
│   ├── processed_signals.csv      # Phase 1 output (160K rows)
│   ├── heatmap.csv                # Drug × cluster distribution
│   └── raw/                       # Raw CSV files (gitignored)
├── src/
│   ├── loader.py                  # CSV ingestion + batch streaming
│   ├── preprocessor.py            # Text cleaning
│   ├── schemas.py                 # Pydantic data models
│   ├── dictionaries.py            # Substance + distress term lists
│   └── detection/
│       └── engine.py              # Hybrid rule + embedding detection
├── notebooks/
│   └── processing_results.ipynb   # Phase 2: clustering + visualization
├── visualizations/                # Generated charts (6 PNG files)
└── report/
    └── Lab 10 Report.pdf
```

---

## Ethical Considerations

- All analysis is performed at the **population level** — no individual identification
- Only **publicly available** datasets used (Kaggle UCI drug reviews)
- Results presented with appropriate context and limitations
- Focused on **responsible AI practices** and transparent methodology

---

## Deliverables

- [4-Page Report](report/Lab%2010%20Report.pdf)
- [3-Minute Video](https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b2c82bcf-a54f-4a1b-b5ef-b42400a3ec95)
- This GitHub Repository

---

## Acknowledgments

**Course:** CS 5542 Big Data Analytics and Applications  
**Event:** [UMKC Research-A-Thon 2026](https://sites.google.com/view/research-a-thon-2026/home)  
**Challenge:** NRT Challenge 1 — AI for Substance Abuse Risk Detection from Social Signals
