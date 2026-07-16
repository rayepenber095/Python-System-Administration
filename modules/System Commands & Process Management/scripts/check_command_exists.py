#!/usr/bin/env python3
"""Check whether a command exists on the current system PATH."""

from __future__ import annotations

import argparse
import shutil


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check if a command is available in PATH.")
    parser.add_argument("command", help="Command name to check.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    command_path = shutil.which(args.command)

    if command_path is None:
        print(f"NOT FOUND: {args.command}")
        return 1

    print(f"FOUND: {args.command} -> {command_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
