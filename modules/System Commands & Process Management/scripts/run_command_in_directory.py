#!/usr/bin/env python3
"""Run a command in a specified working directory."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run command in a specific directory.")
    parser.add_argument("directory", help="Working directory path.")
    parser.add_argument("command", nargs="+", help="Command and arguments.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    directory = Path(args.directory).expanduser().resolve()

    if not directory.exists() or not directory.is_dir():
        print(f"Invalid directory: {directory}")
        return 1

    completed = subprocess.run(
        args.command,
        check=False,
        capture_output=True,
        text=True,
        cwd=directory,
    )

    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="")

    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
