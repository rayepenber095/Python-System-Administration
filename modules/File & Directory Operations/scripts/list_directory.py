#!/usr/bin/env python3
"""List files and directories in a target path."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument("path", nargs="?", default=".", help="Directory to inspect.")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    target = Path(args.path).expanduser().resolve()

    if not target.exists() or not target.is_dir():
        logging.error("Invalid directory: %s", target)
        return 1

    for entry in sorted(target.iterdir()):
        kind = "DIR" if entry.is_dir() else "FILE"
        size = "-" if entry.is_dir() else str(entry.stat().st_size)
        print(f"{kind:4} {size:>10} {entry.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
