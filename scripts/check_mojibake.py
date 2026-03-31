#!/usr/bin/env python3
"""Scan repo text files for common mojibake patterns."""

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

PATTERNS = (
    "窶",
    "竊",
    "遯ｶ繝ｻ",
    "驕ｯ・ｶ郢晢ｽｻ",
    "隨ｨ繝ｻ",
    "﨟樣箕",
    "﨟樊ｳｯ",
    "﨟樊政",
    "遶翫・",
    "遶｢・ｳ",
    "蜀ｲ",
    "蜀ｱ",
    "窶ｦ",
    "窶釘",
    "窶忤",
    "窶廚",
    "窶弩",
    "窶廬",
    "窶播oes",
    "窶俳nly",
)

SKIP_DIRS = {
    ".git",
    "__pycache__",
}

SKIP_FILES = {
    "check_mojibake.py",
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.suffix.lower() not in DEFAULT_EXTENSIONS:
            continue
        yield path


def scan_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [("decode-error", 0, "File is not valid UTF-8")]

    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        matched = [pattern for pattern in PATTERNS if pattern in line]
        if matched:
            hits.append(("pattern", lineno, f"{', '.join(matched)} :: {line.strip()}"))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Check repository files for mojibake.")
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    findings = []

    for path in iter_files(root):
        hits = scan_file(path)
        if hits:
            findings.append((path, hits))

    if not findings:
        print("No mojibake patterns found.")
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
