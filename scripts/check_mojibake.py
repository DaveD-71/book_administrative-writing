#!/usr/bin/env python3
"""Check repo text files for UTF-8 validity and unexpected non-ASCII text."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


DEFAULT_EXTENSIONS = {
    ".md",
    ".txt",
    ".csv",
    ".py",
    ".json",
    ".yml",
    ".yaml",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
}

# A small set of intentional non-ASCII punctuation / symbols is used across the
# repo. Everything else above ASCII is treated as suspicious unless explicitly
# allowlisted by path.
ALLOWED_NON_ASCII_CHARS = {
    "\u00A7",  # section sign
    "\u00E0",  # latin small letter a with grave
    "\u00B7",  # middle dot
    "\u00D7",  # multiplication sign
    "\u2011",  # non-breaking hyphen
    "\u2013",  # en dash
    "\u2014",  # em dash
    "\u2019",  # right single quotation mark
    "\u201C",  # left double quotation mark
    "\u201D",  # right double quotation mark
    "\u2026",  # ellipsis
    "\u2191",  # upwards arrow
    "\u2192",  # rightwards arrow
    "\u23F3",  # hourglass not done
    "\u2605",  # black star
    "\u26A0",  # warning sign
    "\u2713",  # check mark
    "\u2705",  # white heavy check mark
    "\u274C",  # cross mark
    "\u2B1C",  # white large square
    "\uFE0F",  # variation selector-16
    "\U0001F195",  # NEW button
    "\U0001F4CB",  # clipboard
    "\U0001F504",  # anticlockwise arrows button
    "\U0001F534",  # red circle
    "\U0001F7E1",  # yellow circle
}

# Paths listed here are allowed to contain additional intentional non-ASCII text.
# Keep this list small and explicit so mojibake remains easy to catch.
ALLOW_NON_ASCII_PATHS: tuple[str, ...] = ()


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in DEFAULT_EXTENSIONS:
            continue
        yield path


def is_non_ascii_allowed(path: Path, root: Path, extra_allowed: tuple[str, ...]) -> bool:
    rel = path.relative_to(root).as_posix()
    allowed = ALLOW_NON_ASCII_PATHS + extra_allowed
    return any(
        rel == pattern or rel.startswith(f"{pattern}/")
        for pattern in allowed
    )


def find_unexpected_non_ascii(line: str):
    return [
        char for char in line
        if ord(char) > 127 and char not in ALLOWED_NON_ASCII_CHARS
    ]


def scan_file(path: Path, root: Path, extra_allowed: tuple[str, ...]):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [("decode-error", 0, "File is not valid UTF-8")]

    if is_non_ascii_allowed(path, root, extra_allowed):
        return []

    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        bad_chars = find_unexpected_non_ascii(line)
        if bad_chars:
            unique_chars = " ".join(sorted(set(bad_chars)))
            hits.append(
                (
                    "non-ascii",
                    lineno,
                    f"{unique_chars} :: {line.strip()}",
                )
            )
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check repository files for UTF-8 validity and unexpected non-ASCII text."
    )
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan")
    parser.add_argument(
        "--allow-non-ascii",
        action="append",
        default=[],
        metavar="PATH",
        help="Relative file or directory allowed to contain intentional non-ASCII text",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    extra_allowed = tuple(args.allow_non_ascii)
    findings = []

    for path in iter_files(root):
        hits = scan_file(path, root, extra_allowed)
        if hits:
            findings.append((path, hits))

    if not findings:
        print("No encoding or non-ASCII issues found.")
        return 0

    for path, hits in findings:
        rel = path.relative_to(root)
        print(rel.as_posix())
        for kind, lineno, message in hits:
            if kind == "decode-error":
                print(f"  [decode] {message}")
            else:
                print(f"  [line {lineno}] {message}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
