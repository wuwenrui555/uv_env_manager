# Python Environment Manager with `uv`

`uv` is a fast Python package installer and resolver written in Rust, offering up to 100x faster installations than traditional tools. This project provides a centralized system for managing Python environments using `uv`.

## Installation

Install `uv` with a single command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Environment Structure

```tree
uv_env/                   # Root directory for all environments
├── uv_mesmer/            # Project-specific directory
│   ├── .venv/            # Virtual environment directory
│   ├── .python-version   # Python version specification
│   ├── pyproject.toml    # Project definition and dependencies
│   └── uv.lock           # Lock file with exact package versions
```

### Key Components

1. **Root Directory (`uv_env/`)**
   - Central location for all `uv` environments
   - Located in a shared space (e.g., `/mnt/nfs/storage/`)
   - Houses multiple project environments

2. **Project Directory (e.g., `uv_mesmer/`)**
   - Named after your specific project
   - Self-contained environment for your application
   - Multiple projects can coexist under the root directory

3. **Virtual Environment (`.venv/`)**
   - Created using `uv init` and `uv add` commands
   - Contains isolated Python installation with packages
   - Separate from system Python and other environments

4. **Configuration Files**
   - `.python-version`: Defines the Python version
   - `pyproject.toml`: Modern dependency specification
   - `uv.lock`: Ensures reproducible environments

## Usage Options

### Option 1: Symbolic Links (Read-Only Access)

Create symbolic links to an existing environment:

```bash
cd /path/to/your/project
venv_root=/mnt/nfs/storage/uv_env_manager/uv_env
venv_name=uv_mesmer
ln -s ${venv_root}/${venv_name}/.venv .
ln -s ${venv_root}/${venv_name}/pyproject.toml .
ln -s ${venv_root}/${venv_name}/uv.lock .

# Run your script
uv run python your_script.py
```

### Option 2: Copy Environment (Full Access)

Copy an existing environment for local modifications:

```bash
cd /path/to/your/project
venv_root=/mnt/nfs/storage/uv_env_manager/uv_env
venv_name=uv_mesmer
cp -r ${venv_root}/${venv_name}/.venv .
cp ${venv_root}/${venv_name}/pyproject.toml .
cp ${venv_root}/${venv_name}/uv.lock .

# Run your script
uv run python your_script.py
```

### Option 3: Direct Reference

Use an environment in-place without copying:

```bash
venv_root=/mnt/nfs/storage/uv_env_manager/uv_env
venv_name=uv_mesmer
venv_path="${venv_root}/${venv_name}/.venv"

# Use --no-project to ignore local settings
# Use -p to specify the virtual environment path
uv run --no-project -p ${venv_path} python your_script.py
```

## Benefits of `uv`

- **Performance**: 10-100x faster package installation than pip
- **Reliability**: Superior dependency resolution
- **Compatibility**: Works with existing Python tooling
- **Efficiency**: Rust-based implementation for speed
- **Organization**: Centralized environment management

## Available Environments

```tree
/mnt/nfs/storage/uv_env_manager/uv_env
├── uv_mesmer/  # Cell segmentation using Mesmer
├── uv_valis/   # Image alignment with Valis
├── uv_scanpy/  # Single-cell analysis with Scanpy
```
