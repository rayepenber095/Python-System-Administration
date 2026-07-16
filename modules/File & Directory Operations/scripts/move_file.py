#!/usr/bin/env python3
"""Move a file from source to destination."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Move a file.")
    parser.add_argument("source", help="Path to source file.")
    parser.add_argument("destination", help="Path to destination file.")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    source = Path(args.source).expanduser().resolve()
    destination = Path(args.destination).expanduser().resolve()

    if not source.exists() or not source.is_file():
        logging.error("Source file does not exist: %s", source)
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    logging.info("Moved %s -> %s", source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
