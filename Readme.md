# Field Boundary Detection for Small Indian Chilli Farms

This repository contains an implementation of the Field Boundary Detection Model (FBDM) for small Indian chilli farms. The model is based on the FracTAL ResUNet architecture, developed by CSIRO. FBDM uses deep neural networks for accurate mapping of field boundaries using satellite imagery.

## Overview

- **Model Architecture:** FracTAL ResUNet
- **Framework:** MXNet
- **Data Source:** Sentinel Hub
- **Training Approach:** Pre-trained on a large public dataset from Netherlands, fine-tuned on a small labeled Indian dataset using Jupyter Notebooks

## Project Structure

- `/notebooks`: Jupyter notebooks for data preprocessing, model training, and evaluation.
- `/decode_fh`: Source code for the FracTAL ResUNet model.
- `/data`: Placeholder for dataset (not included in this repository).

## Usage

1. **Clone Repository:**
   ```bash
   git clone https://github.com/manib/FBDM.git
   cd FBDM

If you use this code or the FBDM model in your research, please cite the original paper:

@Article{rs13112197,
AUTHOR = {Waldner, François and Diakogiannis, Foivos I. and Batchelor, Kathryn and Ciccotosto-Camp, Michael and Cooper-Williams, Elizabeth and Herrmann, Chris and Mata, Gonzalo and Toovey, Andrew},
TITLE = {Detect, Consolidate, Delineate: Scalable Mapping of Field Boundaries Using Satellite Images},
JOURNAL = {Remote Sensing},
VOLUME = {13},
YEAR = {2021},
NUMBER = {11},
ARTICLE-NUMBER = {2197},
URL = {https://www.mdpi.com/2072-4292/13/11/2197},
ISSN = {2072-4292},
ABSTRACT = {...},
DOI = {10.3390/rs13112197}
}

