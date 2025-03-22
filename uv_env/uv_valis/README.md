# VALIS Environment Setup with `uv`

This repository contains setup instructions for creating a Python environment for [VALIS](https://valis.readthedocs.io/) (Visualization and Analysis of Large-scale Image Sets), a toolkit for working with whole slide images in digital pathology.

## Prerequisites

- [conda](https://docs.conda.io/en/latest/miniconda.html) or [mamba](https://mamba.readthedocs.io/en/latest/installation.html) conda-compatible package manager
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Installation

### Step 1: Create Conda Environment

> **Note**: We use conda/mamba for two types of dependencies:
>
> 1. **pyvips**: Requires libvips which is not a Python package but a system library. Using conda helps install this in a controlled environment when you don't have root access or to avoid conflicts with other packages.
> 2. **tesseract**: Required as a dependency for Python OCR functionality, but tesseract itself is not a Python package.
>
> If your base environment already has usable libvips installed, or if you don't need OCR functionality with tesseract, you can skip creating this conda environment.

```bash
mamba create -n uv_valis pyvips tesseract 
mamba activate uv_valis
```

### Step 2: Install Python Packages with UV

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

```bash
# Install core VALIS package
uv add valis-wsi==1.1.0

# Install additional dependencies
uv add imagecodecs zarr pytesseract pydantic ipykernel
uv add numpy==1.26.4 
uv add geopandas rasterio
```

## Verification

You can check the installed packages and test the environment:

```bash
# View installed packages
uv tree -d 1

# Run the test script to verify imports work correctly
uv run python test_imports.py
```
