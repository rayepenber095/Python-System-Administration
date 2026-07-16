#!/usr/bin/env python3
"""Delete a file or directory path."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Delete a file or directory.")
    parser.add_argument("path", help="File or directory to delete.")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Allow deleting non-empty directories.",
    )
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    target = Path(args.path).expanduser().resolve()

    if not target.exists():
        logging.error("Path does not exist: %s", target)
        return 1

    if target.is_dir():
        if args.recursive:
            shutil.rmtree(target)
        else:
            target.rmdir()
    else:
        target.unlink()

    logging.info("Deleted path: %s", target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
