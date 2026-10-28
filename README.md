# Prompt-Driven Interactive Segmentation as a Dataset-Annotation Tool

**Course:** [CSE 681] Digital Image Processing & Video Processing (F26)
**Team:** Abdelhafeez Arif Abdelhafeez Almaz (Student A, Data & Baseline), [اسم B] (Student B, Model/Algorithm), [اسم C] (Student C, Evaluation)

## Goal

Build a small click/box-prompt labeling tool around SAM2 and measure:

1. **Annotation-time savings:** how much faster the tool is compared to manual polygon labeling.
2. **Mask quality:** how close the SAM2 masks are to COCO ground-truth masks, measured with IoU.

## Dataset

- **Source:** COCO val2017 (images and instance annotations)
- **Subset:** a few hundred images (about 300), selected with a fixed random seed
- **Ground truth:** COCO instance annotations converted to binary masks

## Setup

Requires Python 3.10 or newer.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
pip install -r requirements.txt
```

## Repository structure

```
dip-sam2-annotation/
├── data/        # raw COCO and generated masks (not tracked by git)
├── docs/        # dataset card, evaluation rules, proposal
├── notebooks/   # exploration notebooks
├── scripts/     # data preparation and evaluation scripts
├── requirements.txt
└── README.md
```

## Project status

- [ ] Milestone 1 (Week 3): repository, dataset subset, GT masks, proposal
- [ ] Milestone 2 (Week 6): interactive tool, manual timing baseline
- [ ] Milestone 3 (Week 9): final evaluation, report, demo