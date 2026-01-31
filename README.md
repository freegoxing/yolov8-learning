# YOLOv8 Learning / Tutorial

## Overview

This repository contains my personal learning and experiments with YOLOv8 for object detection.
It includes tutorials, dataset preparation, training, evaluation, and model deployment examples.

## Contents

```bash
src/
├── Yolo/        # YOLOv8 Python scripts (inference, parameter exploration, result analysis)
├── OpenCV/     # OpenCV-based image / video processing demos

models/         # Model weights and checkpoints (optional, recommended via GitHub Releases)

runs/           # YOLO output directory (predictions, visualizations, logs)

notebook/
├── Yolo/       # Markdown notes explaining YOLOv8 workflow, parameters, and results
├── OpenCV/     # Notes and experiments related to OpenCV (optional / future)
```

## Requirements

- Python >= 3.12
- torch, torchvision
- ultralytics (YOLOv8)
- OpenCV, matplotlib

Install dependencies:

```bash
uv sync
```