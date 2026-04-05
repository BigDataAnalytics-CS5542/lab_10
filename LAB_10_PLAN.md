# Lab 10 — AI Challenge Project Plan

**CS 5542 Big Data Analytics and Applications**
**Challenge: AI for Substance Abuse Risk Detection from Social Signals**
**Due: April 6, 2026 at 12:00 PM (Noon)**

---

## Deliverables

- [ ] 4-page report
- [ ] 3-minute video
- [ ] GitHub repository (clean, documented, reproducible)
- [ ] Submit to Canvas
- [ ] Submit to Research-A-Thon

---

## Project Concept

Build an ML pipeline that analyzes CDC overdose data and substance use datasets to detect trends, risk signals, and demographic patterns in substance abuse. The system should produce interpretable visualizations and insights at the population level.

### Core Tasks We'll Address

1. **Temporal & Behavioral Analysis** — Trend analysis on fatal/non-fatal overdose data over time (spikes, seasonal patterns, year-over-year changes)
2. **Risk Signal Detection** — Identify high-risk demographics, substances, and geographic regions from the data
3. **Explainability** — Interpretable visualizations and summaries of findings

### Methods

- **Trend analysis** — Time series analysis on overdose rates
- **Classification/Clustering** — Group demographics or regions by risk level
- **Visualization/Dashboard** — Charts showing trends, heatmaps, risk breakdowns
- **LLM Summarization** (optional) — Generate interpretable summaries of findings

---

## Datasets

| Dataset | Source | Format |
|---|---|---|
| Fatal overdose data | [CDC SUDORS Dashboard](https://www.cdc.gov/overdose-prevention/data-research/facts-stats/sudors-dashboard-fatal-overdose-data-accessible.html) | XLSX |
| Non-fatal overdose data | [CDC DOSE Dashboard](https://www.cdc.gov/overdose-prevention/data-research/facts-stats/dose-dashboard-nonfatal-discharge-data.html) | XLSX |
| Florida drugs in system post-overdose | [FDLE MEC Publications](https://www.fdle.state.fl.us/MEC/Publications-and-Forms) | — |
| Substance use by demographic | [Monitoring the Future (Panel)](https://monitoringthefuture.org/data/panel/) | — |
| Alcohol use rate (high schoolers) | [Monitoring the Future (Prevalence)](https://monitoringthefuture.org/data/bx-by/drug-prevalence/#drug="") | — |

**Primary datasets**: Fatal + Non-fatal overdose (first two). Others are supplementary.

---

## Work Division

### Kenneth — Data & Report
- Download and clean the CDC overdose datasets
- Exploratory data analysis
- Document preprocessing steps and model details
- Write the 4-page report

### Ron — Video & Submission
- Record/edit the 3-minute demo video
- Handle submissions (Canvas + Research-A-Thon)
- Contribute to report sections (dataset description, ethical considerations)

### Blake — Modeling, Visualization & GitHub
- Build ML models (clustering by region/demographic, trend detection)
- Build visualizations (trend charts, risk heatmaps, demographic breakdowns)
- Set up Lab 10 code in the GitHub repo (separate directory or separate repo)
- Contribute to report sections (ML/AI methods, experimental design, results & discussion)
- README with setup instructions and dataset info

---

## Report Outline (4 pages max)

1. **Project Title & Team Members**
2. **Problem Statement** — Substance abuse is a major public health crisis; early detection of risk signals can inform intervention
3. **Datasets Used** — CDC fatal/non-fatal overdose data, supplementary demographic data
4. **Data Preprocessing** — Cleaning, handling missing values, normalization, feature extraction
5. **ML/AI Methods** — Trend analysis, clustering, classification (describe each)
6. **Experimental Design** — Train/test splits, evaluation metrics, comparison of approaches
7. **Results & Discussion** — Key findings with figures/tables
8. **Ethical Considerations** — Population-level only, no individual identification, public data, responsible AI
9. **Conclusion & Future Work** — Summary of insights, limitations, next steps

---

## Technical Pipeline

```
Raw Data (XLSX)
    → Preprocessing (pandas: clean, normalize, feature extraction)
    → EDA (matplotlib/seaborn: distributions, correlations)
    → Modeling
        → Time series trend analysis (overdose rates over time)
        → Clustering (K-means/DBSCAN on regions or demographics)
        → Classification (risk level prediction)
    → Visualization (dashboard or static charts)
    → LLM Summary (optional: Gemini generates interpretable narrative)
    → Report & Video
```

---

## Timeline

| When | What |
|---|---|
| **Saturday morning** | Kenneth: cleaned datasets ready. Blake: repo structure + start report |
| **Saturday afternoon** | Kenneth: models running. Blake: visualizations + report draft |
| **Saturday evening** | Integrate all pieces. Review report draft together |
| **Sunday morning** | Ron: record video. Blake: finalize report + GitHub README |
| **Sunday by 11 AM** | Submit to Canvas + Research-A-Thon |

---

## Open Questions

- Do we need a separate GitHub repo for Lab 10, or a subdirectory in the existing repo?
- Which specific ML models does Kenneth plan to use?
- Does Ron want to narrate the video or should we split narration?
