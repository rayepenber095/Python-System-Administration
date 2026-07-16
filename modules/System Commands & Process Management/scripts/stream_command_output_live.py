#!/usr/bin/env python3
"""Run a command and stream output live while preserving exit status."""

from __future__ import annotations

import argparse
import subprocess


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stream command output in real time.")
    parser.add_argument("command", nargs="+", help="Command and arguments.")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        process = subprocess.Popen(
            args.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError:
        print(f"Command not found: {args.command[0]}")
        return 1

    assert process.stdout is not None
    for line in process.stdout:
        print(line, end="")

    return process.wait()


if __name__ == "__main__":
    raise SystemExit(main())
