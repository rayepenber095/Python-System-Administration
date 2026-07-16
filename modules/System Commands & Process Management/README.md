# System Commands & Process Management

## Overview

This module provides scripts for running external commands, handling shell-safe parsing, checking exit codes, and enforcing command timeouts.

## Scripts Included

| Script | Description |
|---|---|
| `execute_external_command.py` | Run a command directly without shell invocation. |
| `execute_shell_command_securely.py` | Parse command text with `shlex.split` and execute safely. |
| `get_exit_status.py` | Execute a command and print its return code. |
| `run_command_with_timeout.py` | Run a command and terminate it after a timeout. |

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
System Commands & Process Management/
├── README.md
└── scripts/
    ├── execute_external_command.py
    ├── execute_shell_command_securely.py
    ├── get_exit_status.py
    └── run_command_with_timeout.py
```

## Usage

```bash
python scripts/execute_external_command.py python --version
python scripts/execute_shell_command_securely.py "python --version"
python scripts/get_exit_status.py python --version
python scripts/run_command_with_timeout.py 2 python --version
```

## Expected Output

```text
Python 3.11.x
Exit status: 0
```

## Requirements

- Python standard library only.

## Learning Objectives

- Run subprocess commands safely and predictably.
- Capture command output and interpret return codes.
- Prevent long-running commands from hanging automation.

## Notes

- Timeout script returns exit code `124` when command duration exceeds the provided limit.
- Shell command parsing errors are reported with clear failure messages.
