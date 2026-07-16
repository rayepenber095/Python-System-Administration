#!/usr/bin/env python3
"""Run a command and retry on failure."""

from __future__ import annotations

import argparse
import subprocess
import time


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a command with retry logic.")
    parser.add_argument("--retries", type=int, default=3, help="Maximum attempts (default: 3).")
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay in seconds between attempts (default: 1.0).",
    )
    parser.add_argument("command", nargs="+", help="Command and arguments.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    attempts = max(args.retries, 1)

    for attempt in range(1, attempts + 1):
        completed = subprocess.run(args.command, check=False, capture_output=True, text=True)

        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="")

        if completed.returncode == 0:
            print(f"Command succeeded on attempt {attempt}.")
            return 0

        if attempt < attempts:
            print(f"Attempt {attempt} failed with code {completed.returncode}; retrying...")
            time.sleep(max(args.delay, 0.0))

    print(f"Command failed after {attempts} attempts.")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
