#!/usr/bin/env python3
"""Create a ZIP archive from a directory."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compress a directory into ZIP format.")
    parser.add_argument("source", help="Directory to compress.")
    parser.add_argument("archive", help="Output archive path (without extension or with .zip).")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    source = Path(args.source).expanduser().resolve()
    archive = Path(args.archive).expanduser().resolve()

    if not source.exists() or not source.is_dir():
        logging.error("Invalid source directory: %s", source)
        return 1

    archive_base = archive.with_suffix("") if archive.suffix == ".zip" else archive
    output = shutil.make_archive(str(archive_base), "zip", root_dir=source)
    logging.info("Created archive: %s", output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
