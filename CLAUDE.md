# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

CS 5542 Big Data Analytics and Applications — Lab 10. AI for Substance Abuse Risk Detection from Social Signals (NSF NRT AI Challenge, UMKC 2026 Spring Research-A-Thon).

Team: Kenneth (data cleaning & report), Ron (video & submission), Blake (modeling, visualization & GitHub).

## Setup

```bash
pip install -r requirements.txt
```

Dependencies: pandas, numpy, matplotlib, seaborn, scikit-learn, jupyter, openpyxl.

Raw datasets are gitignored. See `data/README.md` for download links. Place XLSX files in `data/raw/`.

## Running

```bash
jupyter notebook notebooks/    # EDA and modeling notebooks
python src/main.py              # ML pipeline (when implemented)
```

## Architecture

- **`data/raw/`** — Original XLSX files from CDC (gitignored)
- **`data/processed/`** — Cleaned CSVs output by preprocessing (gitignored)
- **`notebooks/`** — Jupyter notebooks for EDA and model experimentation
- **`src/`** — Reusable Python modules (preprocessing, models, visualization)
- **`visualizations/`** — Saved figures for the report
- **`report/`** — 4-page report deliverable

Pipeline flow: raw XLSX → preprocessing (pandas) → EDA → modeling (time series, clustering, classification) → visualization → report.

## Key Constraints

- All analysis must be population-level only — no individual identification
- Only publicly available or instructor-approved datasets
- Primary datasets: CDC SUDORS (fatal overdose) and CDC DOSE (non-fatal overdose)
- Submission deadline: April 6, 2026 at noon; Research-A-Thon event: April 10, 2026
