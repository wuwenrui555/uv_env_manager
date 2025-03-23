# Scanpy Environment Setup with `uv`

This repository contains a Python environment setup for [Scanpy](https://scanpy.readthedocs.io/en/stable/), a scalable toolkit for analyzing single-cell gene expression data.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) package manager

## Installation

Set up the environment with the following commands:

```bash
# Initialize uv with Python 3.12
uv init -p 3.12
uv python install cpython-3.12

# Install required packages
uv add scanpy ipykernel
```

## Verification

You can check the installed packages and test the environment:

```bash
# View installed packages
uv tree -d 1

# Run the test script to verify imports work correctly
uv run python test_imports.py
```

## Usage

Access this environment from your project using one of the methods described in the main README.md file:

1. Symbolic links (read-only access)
2. Copy environment (full access)
3. Direct reference without copying
