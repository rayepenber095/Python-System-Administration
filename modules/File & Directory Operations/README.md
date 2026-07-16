# File & Directory Operations

## Overview

This module contains scripts for common filesystem automation tasks such as listing, copying, moving, and checksum verification.

## Scripts Included

| Script | Description |
|---|---|
| `list_directory.py` | List files and folders in a target directory. |
| `copy_file.py` | Copy one file to a destination path. |
| `move_file.py` | Move one file to a destination path. |
| `calculate_hash.py` | Generate MD5/SHA1/SHA256 checksums for a file. |

## Installation

- Python: **3.11+**

```bash
python -m venv .venv
```

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

No third-party dependencies are required.

## Folder Structure

```text
File & Directory Operations/
├── README.md
└── scripts/
    ├── calculate_hash.py
    ├── copy_file.py
    ├── list_directory.py
    └── move_file.py
```

## Usage

```bash
python scripts/list_directory.py .
python scripts/copy_file.py source.txt backup/source.txt
python scripts/move_file.py backup/source.txt archive/source.txt
python scripts/calculate_hash.py archive/source.txt --algorithm sha256
```

## Expected Output

```text
INFO: Copied /path/source.txt -> /path/backup/source.txt
INFO: Moved /path/backup/source.txt -> /path/archive/source.txt
sha256:...  source.txt
```

## Requirements

- Python standard library only.

## Learning Objectives

- Work with filesystem paths using `pathlib`.
- Safely copy and move files from CLI scripts.
- Validate file integrity using checksums.

## Notes

- Scripts return non-zero exit codes on failures.
- Paths are resolved from the current runtime environment.
