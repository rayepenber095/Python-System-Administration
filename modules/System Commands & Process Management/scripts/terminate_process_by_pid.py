#!/usr/bin/env python3
"""Terminate or kill a process by PID."""

from __future__ import annotations

import argparse
import os
import signal


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Terminate process by PID.")
    parser.add_argument("pid", type=int, help="Target process ID.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Use SIGKILL where available instead of SIGTERM.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    sig = signal.SIGTERM
    if args.force and hasattr(signal, "SIGKILL"):
        sig = signal.SIGKILL

    try:
        os.kill(args.pid, sig)
    except ProcessLookupError:
        print(f"No process found with PID {args.pid}.")
        return 1
    except PermissionError:
        print(f"Permission denied for PID {args.pid}.")
        return 1

    print(f"Signal {sig.name} sent to PID {args.pid}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
