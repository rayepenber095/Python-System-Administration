#!/usr/bin/env python3
"""Run a command and print its exit status."""

from __future__ import annotations

import argparse
import logging
import subprocess


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get command exit status.")
    parser.add_argument("command", nargs="+", help="Command and arguments.")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()

    try:
        completed = subprocess.run(args.command, check=False)
    except FileNotFoundError:
        logging.error("Command not found: %s", args.command[0])
        return 1

    print(f"Exit status: {completed.returncode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
