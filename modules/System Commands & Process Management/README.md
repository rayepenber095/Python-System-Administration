# System Commands & Process Management

## Overview

This module provides scripts for running external commands, handling shell-safe parsing, checking exit codes, enforcing command timeouts, and basic process control operations.

## Scripts Included

| Script | Description |
|---|---|
| `execute_external_command.py` | Run a command directly without shell invocation. |
| `execute_shell_command_securely.py` | Parse command text with `shlex.split` and execute safely. |
| `get_exit_status.py` | Execute a command and print its return code. |
| `run_command_with_timeout.py` | Run a command and terminate it after a timeout. |
| `check_command_exists.py` | Check whether a command is available in PATH. |
| `list_running_processes.py` | List currently running processes using OS tools. |
| `retry_command.py` | Retry a command multiple times until success or limit reached. |
| `run_command_in_directory.py` | Run a command from a specified working directory. |
| `stream_command_output_live.py` | Stream command output in real time. |
| `terminate_process_by_pid.py` | Send terminate/kill signals to a process ID. |

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
    ├── check_command_exists.py
    ├── execute_external_command.py
    ├── execute_shell_command_securely.py
    ├── get_exit_status.py
    ├── list_running_processes.py
    ├── retry_command.py
    ├── run_command_in_directory.py
    ├── run_command_with_timeout.py
    ├── stream_command_output_live.py
    └── terminate_process_by_pid.py
```

## Usage

```bash
python scripts/execute_external_command.py python --version
python scripts/execute_shell_command_securely.py "python --version"
python scripts/get_exit_status.py python --version
python scripts/run_command_with_timeout.py 2 python --version
python scripts/check_command_exists.py python
python scripts/list_running_processes.py --head 10
python scripts/retry_command.py --retries 3 --delay 1 python --version
python scripts/run_command_in_directory.py . python --version
python scripts/stream_command_output_live.py python --version
python scripts/terminate_process_by_pid.py 12345
```

## Expected Output

```text
FOUND: python -> /usr/bin/python
Python 3.11.x
Exit status: 0
```

## Requirements

- Python standard library only.

## Learning Objectives

- Run subprocess commands safely and predictably.
- Capture command output and interpret return codes.
- Prevent long-running commands from hanging automation.
- Execute commands with retries and directory context.
- Perform basic process discovery and termination workflows.

## Notes

- Timeout script returns exit code `124` when command duration exceeds the provided limit.
- Shell command parsing errors are reported with clear failure messages.
- Process listing and signal behavior can vary by operating system.
