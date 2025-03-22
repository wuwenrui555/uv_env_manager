# Mesmer Environment Setup with `uv`

This repository contains a Python environment setup for [Mesmer](https://deepcell.readthedocs.io/en/master/app-gallery/mesmer.html), a deep learning algorithm for segmenting nuclei and whole cells in tissue images.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) package manager

## Installation

Set up the environment with the following commands:

```bash
# Initialize uv with Python 3.10
uv init -p 3.10
uv python install cpython-3.10

# Install required packages
uv add deepcell==0.12.6 
uv add git+https://github.com/SizunJiangLab/pycodex.git@v0.1.9
uv add git+https://github.com/wuwenrui555/pyqupath.git@v0.0.4
uv add tqdm_joblib ipykernel geopandas imagecodecs
```

## Verification

You can check the installed packages and test the environment:

```bash
# View installed packages
uv tree -d 1

# Run the test script to verify imports work correctly
uv run python test_imports.py
```
