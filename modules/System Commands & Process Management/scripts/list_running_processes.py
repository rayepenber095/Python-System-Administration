#!/usr/bin/env python3
"""List running processes using a platform-appropriate command."""

from __future__ import annotations

import argparse
import platform
import subprocess


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="List running processes.")
    parser.add_argument(
        "--head",
        type=int,
        default=20,
        help="Number of process lines to print (default: 20).",
    )
    return parser


def get_process_command() -> list[str]:
    if platform.system().lower().startswith("win"):
        return ["tasklist"]
    return ["ps", "-eo", "pid,ppid,comm"]


def main() -> int:
    args = build_parser().parse_args()
    completed = subprocess.run(get_process_command(), check=False, capture_output=True, text=True)

    if completed.returncode != 0:
        if completed.stderr:
            print(completed.stderr, end="")
        return completed.returncode

    lines = completed.stdout.splitlines()
    for line in lines[: max(args.head, 1)]:
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
