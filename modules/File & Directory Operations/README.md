# File & Directory Operations

## Overview

This module contains scripts for common filesystem automation tasks such as listing, creating, copying, moving, deleting, searching, archiving, and checksum verification.

## Scripts Included

| Script | Description |
|---|---|
| `list_directory.py` | List files and folders in a target directory. |
| `copy_file.py` | Copy one file to a destination path. |
| `move_file.py` | Move one file to a destination path. |
| `calculate_hash.py` | Generate MD5/SHA1/SHA256 checksums for a file. |
| `create_directory.py` | Create a directory path (with optional exist-ok behavior). |
| `delete_path.py` | Delete files or directories. |
| `find_files.py` | Find files recursively using glob patterns. |
| `compress_directory.py` | Create a ZIP archive from a directory. |
| `extract_archive.py` | Extract a supported archive into a directory. |
| `get_file_metadata.py` | Print file/directory metadata such as size and timestamps. |

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
    ├── compress_directory.py
    ├── copy_file.py
    ├── create_directory.py
    ├── delete_path.py
    ├── extract_archive.py
    ├── find_files.py
    ├── get_file_metadata.py
    ├── list_directory.py
    └── move_file.py
```

## Usage

```bash
python scripts/list_directory.py .
python scripts/create_directory.py data/archive
python scripts/copy_file.py source.txt backup/source.txt
python scripts/move_file.py backup/source.txt archive/source.txt
python scripts/find_files.py . "*.txt"
python scripts/get_file_metadata.py archive/source.txt
python scripts/compress_directory.py archive archive_backup.zip
python scripts/extract_archive.py archive_backup.zip restored_archive
python scripts/delete_path.py restored_archive --recursive
python scripts/calculate_hash.py archive/source.txt --algorithm sha256
```

## Expected Output

```text
INFO: Created directory: /path/data/archive
INFO: Copied /path/source.txt -> /path/backup/source.txt
sha256:...  source.txt
```

## Requirements

- Python standard library only.

## Learning Objectives

- Work with filesystem paths using `pathlib`.
- Safely create, copy, move, and remove paths from CLI scripts.
- Search filesystem structures using glob patterns.
- Package and extract archives for backup workflows.
- Validate file integrity and inspect filesystem metadata.

## Notes

- Scripts return non-zero exit codes on failures.
- Paths are resolved from the current runtime environment.
- `delete_path.py` without `--recursive` only removes empty directories.
