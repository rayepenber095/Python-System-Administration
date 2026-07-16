#!/usr/bin/env python3
"""Execute shell-style command text safely with shlex.split."""

from __future__ import annotations

import argparse
import logging
import shlex
import subprocess


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run shell command text safely.")
    parser.add_argument("command", help="Command string, for example: \"python --version\"")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()

    try:
        command_parts = shlex.split(args.command)
        completed = subprocess.run(command_parts, check=False, capture_output=True, text=True)
    except ValueError as exc:
        logging.error("Invalid command string: %s", exc)
        return 1
    except FileNotFoundError:
        logging.error("Command not found.")
        return 1

    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
