#!/usr/bin/env python3
"""Print common metadata for a file or directory path."""

from __future__ import annotations

import argparse
import datetime as dt
import logging
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Show file metadata.")
    parser.add_argument("path", help="Path to inspect.")
    return parser


def to_iso(timestamp: float) -> str:
    return dt.datetime.fromtimestamp(timestamp, tz=dt.timezone.utc).isoformat()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    target = Path(args.path).expanduser().resolve()

    if not target.exists():
        logging.error("Path does not exist: %s", target)
        return 1

    stats = target.stat()
    print(f"path: {target}")
    print(f"type: {'directory' if target.is_dir() else 'file'}")
    print(f"size_bytes: {stats.st_size}")
    print(f"modified_utc: {to_iso(stats.st_mtime)}")
    print(f"accessed_utc: {to_iso(stats.st_atime)}")
    print(f"created_utc: {to_iso(stats.st_ctime)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
