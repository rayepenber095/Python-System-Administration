#!/usr/bin/env python3
"""Calculate file hash using md5/sha1/sha256."""

from __future__ import annotations

import argparse
import hashlib
import logging
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate file checksum.")
    parser.add_argument("file", help="File path.")
    parser.add_argument("--algorithm", choices=["md5", "sha1", "sha256"], default="sha256")
    return parser


def checksum(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    file_path = Path(args.file).expanduser().resolve()

    if not file_path.exists() or not file_path.is_file():
        logging.error("Invalid file: %s", file_path)
        return 1

    digest = checksum(file_path, args.algorithm)
    print(f"{args.algorithm}:{digest}  {file_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
