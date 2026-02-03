# YOLOv8 & OpenCV Learning Repository

## Overview

This repository documents my hands-on learning process in computer vision, focusing on:

- YOLOv8 — object detection workflows, parameter exploration, and result analysis
- OpenCV — fundamental image processing techniques and experiments

It combines code, notes, datasets, and generated artifacts to form a reproducible learning pipeline.

## Contents

```bash
.
├── src/                # Source code
│   ├── Yolo/           # YOLOv8 experiments and scripts
│   └── OpenCV/         # Image processing notebooks
│
├── notebook/           # Structured learning notes (Markdown)
│   ├── Yolo/
│   └── OpenCV/
│
├── data/               # Input datasets (images / videos)
│
├── artifacts/          # Generated outputs from experiments
│   ├── OpenCV/         # Processed images
│   └── Yolo/           # Detection results
│
├── models/             # Model weights (e.g., yolov8n.pt)
│
├── runs/               # Ultralytics default output directory
│
├── pyproject.toml      # Dependency management (uv)
└── README.md

```

## Features

- Reproducible YOLOv8 inference workflows
- Parameter sensitivity experiments
- OpenCV preprocessing demonstrations
- Organized Markdown notes for theory + practice
- Clean separation of data → code → artifacts

## Requirements

- Python >= 3.12
- torch, torchvision
- ultralytics (YOLOv8)
- OpenCV
- matplotlib
- jupyterlab

Install dependencies:

```bash
uv sync
```

## Quick Start

Run a YOLO demo

```bash
uv run src/Yolo/01demo/main.py
```

Explore OpenCV Jupyter experiments

```bash
jupyter notebook src/OpenCV/
```