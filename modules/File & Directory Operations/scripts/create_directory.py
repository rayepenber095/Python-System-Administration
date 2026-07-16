#!/usr/bin/env python3
"""Create a directory path with optional parent creation."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a directory.")
    parser.add_argument("path", help="Directory path to create.")
    parser.add_argument(
        "--exist-ok",
        action="store_true",
        help="Do not fail if the directory already exists.",
    )
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    directory = Path(args.path).expanduser().resolve()

    try:
        directory.mkdir(parents=True, exist_ok=args.exist_ok)
    except FileExistsError:
        logging.error("Directory already exists: %s", directory)
        return 1

    logging.info("Created directory: %s", directory)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
