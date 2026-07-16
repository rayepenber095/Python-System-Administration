# Input & Output Handling

## Overview

This module provides focused Python scripts for common CLI input/output workflows used in system automation.

## Scripts Included

| Script | Description |
|---|---|
| `input_from_file.py` | Read text data from a file path. |
| `input_from_pipe.py` | Read piped data from another process. |
| `capture_command_output.py` | Execute a command and capture stdout/stderr. |
| `redirect_streams.py` | Redirect standard streams programmatically. |
| `read_stdin.py` | Read input from standard input. |
| `write_stdout.py` | Write normal output to standard output. |
| `write_stderr.py` | Write error output to standard error. |
| `read_multiline_input.py` | Read multiline terminal input until EOF. |
| `handle_cli_arguments.py` | Parse raw command-line arguments via `sys.argv`. |
| `argparse_options.py` | Build CLI options with `argparse`. |
| `click_options.py` | Build CLI options with `click`. |
| `parse_env_variables.py` | Read configuration from environment variables. |
| `interactive_menu.py` | Run a basic interactive terminal menu. |
| `progress_bar.py` | Display progress indicators for long tasks. |
| `colored_output.py` | Print colored terminal output. |
| `pretty_print_data.py` | Pretty-print nested Python data structures. |
| `read_json_input.py` | Parse JSON input from file or stdin. |
| `read_csv_input.py` | Parse CSV input data. |
| `read_yaml_input.py` | Parse YAML input data. |
| `read_xml_input.py` | Parse XML input data. |
| `read_toml_input.py` | Parse TOML input data. |
| `read_password_protected_file.py` | Read password-protected ZIP contents. |
| `read_stdin_timeout.py` | Read stdin with a timeout (platform-dependent). |
| `interactive_confirmation.py` | Prompt user confirmation before an action. |

## Installation

- Python: **3.11+**
- Create virtual environment:

```bash
python -m venv .venv
```

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
```

## Folder Structure

```text
Input & Output Handling/
├── README.md
├── requirements.txt
└── scripts/
    ├── argparse_options.py
    ├── capture_command_output.py
    ├── click_options.py
    ├── colored_output.py
    ├── handle_cli_arguments.py
    ├── input_from_file.py
    ├── input_from_pipe.py
    ├── interactive_confirmation.py
    ├── interactive_menu.py
    ├── parse_env_variables.py
    ├── pretty_print_data.py
    ├── progress_bar.py
    ├── read_csv_input.py
    ├── read_json_input.py
    ├── read_multiline_input.py
    ├── read_password_protected_file.py
    ├── read_stdin.py
    ├── read_stdin_timeout.py
    ├── read_toml_input.py
    ├── read_xml_input.py
    ├── read_yaml_input.py
    ├── redirect_streams.py
    ├── write_stderr.py
    └── write_stdout.py
```

## Usage

Run from the module directory:

```bash
python scripts/input_from_file.py sample.txt
python scripts/input_from_pipe.py
python scripts/capture_command_output.py --help
python scripts/redirect_streams.py
python scripts/read_stdin.py
python scripts/write_stdout.py
python scripts/write_stderr.py
python scripts/read_multiline_input.py
python scripts/handle_cli_arguments.py arg1 arg2
python scripts/argparse_options.py --help
python scripts/click_options.py --help
python scripts/parse_env_variables.py
python scripts/interactive_menu.py
python scripts/progress_bar.py
python scripts/colored_output.py
python scripts/pretty_print_data.py
python scripts/read_json_input.py sample.json
python scripts/read_csv_input.py sample.csv
python scripts/read_yaml_input.py sample.yaml
python scripts/read_xml_input.py sample.xml
python scripts/read_toml_input.py sample.toml
python scripts/read_password_protected_file.py archive.zip
python scripts/read_stdin_timeout.py
python scripts/interactive_confirmation.py
```

## Expected Output

```text
[INFO] Script started.
[INFO] Input processed successfully.
[ERROR] Invalid input file path.
```

## Requirements

- `click`
- `PyYAML`
- `tqdm`
- `colorama`
- `toml` (only for Python < 3.11)

## Learning Objectives

- Build reliable CLI tools with standard and third-party parsers.
- Separate stdout and stderr clearly for automation pipelines.
- Parse common structured formats used in system administration.
- Handle interactive and non-interactive terminal input patterns.

## Notes

- `read_stdin_timeout.py` uses behavior that may differ between Windows and Unix-like systems.
- `read_password_protected_file.py` is for educational ZIP handling; avoid hardcoded secrets in production.
