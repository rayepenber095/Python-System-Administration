#!/usr/bin/env python3
"""Find files by glob pattern under a root directory."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Find files under a directory.")
    parser.add_argument("root", help="Root directory for the search.")
    parser.add_argument("pattern", help='Glob pattern, for example "*.log".')
    parser.add_argument(
        "--include-directories",
        action="store_true",
        help="Include directories in results.",
    )
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    root = Path(args.root).expanduser().resolve()

    if not root.exists() or not root.is_dir():
        logging.error("Invalid directory: %s", root)
        return 1

    matches = []
    for path in root.rglob(args.pattern):
        if path.is_file() or args.include_directories:
            matches.append(path)

    for match in sorted(matches):
        print(match)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
