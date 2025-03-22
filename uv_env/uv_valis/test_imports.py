#!/usr/bin/env python
"""
Test script to verify all required packages can be imported successfully.
"""

import importlib
import sys


def test_imports():
    """Test if all required packages can be imported."""
    packages = [
        # Python packages installed with uv
        "geopandas",
        "imagecodecs",
        "ipykernel",
        "numpy",
        "pydantic",
        "pytesseract",
        "rasterio",
        "valis",  # valis-wsi
        "zarr",
    ]

    results = {}
    all_success = True

    print("Testing imports for VALIS environment packages:")
    print("-" * 50)

    for package in packages:
        try:
            importlib.import_module(package)
            results[package] = "✓ Success"
        except ImportError as e:
            results[package] = f"✗ Failed: {str(e)}"
            all_success = False

    # Print results in a formatted way
    max_package_length = max(len(package) for package in packages)
    for package, result in results.items():
        print(f"{package.ljust(max_package_length + 2)} {result}")

    print("-" * 50)
    if all_success:
        print("All packages imported successfully!")
    else:
        print("Some packages failed to import.")
        sys.exit(1)


if __name__ == "__main__":
    test_imports()
