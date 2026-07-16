# Python System Administration

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A practical, module-based repository of production-minded Python scripts for system administration, DevOps automation, and operational tooling.

## Features

- Single-purpose scripts (one task per file)
- Beginner-friendly but production-oriented examples
- Cross-platform scripting patterns where possible
- Consistent CLI usage with clear output and exit codes
- Module-level documentation and dependency guidance

## Repository Structure

```text
Python-System-Administration/
├── README.md
└── modules/
    ├── Input & Output Handling/
    │   ├── README.md
    │   ├── requirements.txt
    │   └── scripts/
    ├── File & Directory Operations/
    │   ├── README.md
    │   └── scripts/
    └── System Commands & Process Management/
        ├── README.md
        └── scripts/
```

## Learning Path

1. **Input & Output Handling**: CLI basics, streams, structured input parsing
2. **System Commands & Process Management**: subprocess patterns and process lifecycle control
3. **File & Directory Operations**: filesystem automation and integrity workflows

## Prerequisites

- Python 3.11+
- Basic terminal knowledge
- `pip` available in your environment

## Installation

```bash
git clone https://github.com/rayepenber095/Python-System-Administration.git
cd Python-System-Administration
python -m venv .venv
```

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Install module dependencies as needed, for example:

```bash
pip install -r "modules/Input & Output Handling/requirements.txt"
```

## How Modules Are Organized

- Each module has its own `README.md`
- Scripts are stored in `scripts/` with lowercase underscore filenames
- Optional dependencies are scoped at the module level

## How Scripts Are Organized

- One script = one topic = one responsibility
- Scripts provide runnable entry points (`if __name__ == "__main__":`)
- Scripts should emit meaningful success/error output

## How to Run Scripts

```bash
python "modules/Input & Output Handling/scripts/input_from_file.py" sample.txt
python "modules/Input & Output Handling/scripts/read_json_input.py" sample.json
python "modules/Input & Output Handling/scripts/argparse_options.py" --help
```

## Table of Modules

| Module | Focus Area | Status |
|---|---|---|
| Input & Output Handling | Streams, CLI input, structured parsing | Available |
| File & Directory Operations | Filesystem and archive workflows | In progress |
| System Commands & Process Management | Subprocess and process control | In progress |

## Project Goals

- Provide high-quality script references for common admin tasks
- Encourage safe, repeatable, and auditable automation
- Build a strong foundation for larger internal tooling

## Best Practices Followed

- PEP 8 naming and readability
- `argparse` for CLI interfaces
- `pathlib` for path handling where appropriate
- Explicit exception handling and clear errors
- No hardcoded environment-specific paths

## Repository Statistics

- Module directories: **3**
- Script files: **33**
- Current focus: **standardizing module quality and coverage**

## Contribution Guide

1. Fork the repository
2. Create a feature branch
3. Add or improve one single-purpose script
4. Update module README tables and usage examples
5. Open a pull request with clear change notes

## License

Distributed under the terms of the [MIT License](LICENSE).
