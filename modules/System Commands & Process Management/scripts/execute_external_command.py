#!/usr/bin/env python3
"""Execute an external command without invoking a shell."""

from __future__ import annotations

import argparse
import logging
import subprocess


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run an external command.")
    parser.add_argument("command", nargs="+", help="Command and arguments.")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()

    try:
        completed = subprocess.run(args.command, check=False, capture_output=True, text=True)
    except FileNotFoundError:
        logging.error("Command not found: %s", args.command[0])
        return 1

    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, end="")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
