#!/usr/bin/env python3
"""Extract a supported archive into a target directory."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract an archive.")
    parser.add_argument("archive", help="Archive file path.")
    parser.add_argument("destination", help="Target extraction directory.")
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    archive = Path(args.archive).expanduser().resolve()
    destination = Path(args.destination).expanduser().resolve()

    if not archive.exists() or not archive.is_file():
        logging.error("Invalid archive path: %s", archive)
        return 1

    destination.mkdir(parents=True, exist_ok=True)

    try:
        shutil.unpack_archive(str(archive), str(destination))
    except (shutil.ReadError, ValueError) as exc:
        logging.error("Unsupported or invalid archive: %s", exc)
        return 1

    logging.info("Extracted %s -> %s", archive, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
