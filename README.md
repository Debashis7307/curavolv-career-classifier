# Curavolv Career Classifier

This project implements a rule-based, explainable classification system that maps candidate profiles to:

- Top 3 healthcare career tracks
- Recommended degree pathway

## Approach

The system uses a weighted scoring model based on:

- Academic subjects → mapped to clusters → degree signals
- Work experience → domain alignment
- SOP (Statement of Purpose) → keyword-based intent detection
- Strengths → minor supporting signals

## Architecture

Candidate → Feature Extraction → Scoring Engine → Ranking → Output JSON

## How to Run

```bash
python main.py