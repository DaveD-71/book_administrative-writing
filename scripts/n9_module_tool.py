#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


UNIT_HEADING_RE = re.compile(r"^## Unit (\d+) — (.+)$", re.MULTILINE)
SECTION_HEADING_RE = re.compile(r"^### ([A-H])\. (.+)$", re.MULTILINE)
SUBSECTION_HEADING_RE = re.compile(r"^#### (A\d|B\d|C\d|D\d|E\d|F\d|G\d|H\d)\. (.+)$", re.MULTILINE)
JPO_LABEL_RE = re.compile(r"\*\(JPO context\)\*")
WORD_COUNT_RE = re.compile(r"\*\*(\d+–\d+)\s*word\*\*|\*\*(\d+–\d+)\s*words\*\*", re.IGNORECASE)


@dataclass
class UnitBlock:
    number: int
    title: str
    body: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def split_units(text: str) -> list[UnitBlock]:
    matches = list(UNIT_HEADING_RE.finditer(text))
    units: list[UnitBlock] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        units.append(UnitBlock(number=int(match.group(1)), title=match.group(2).strip(), body=body))
    return units


def find_h_subsections(unit_body: str) -> list[str]:
    in_h = False
    found: list[str] = []
    for line in unit_body.splitlines():
        if line.startswith("### "):
            in_h = line.startswith("### H.")
            continue
        if in_h and line.startswith("#### "):
            code = line[5:].split(".", 1)[0]
            if code.startswith("H"):
                found.append(code)
    return found


def extract_word_counts(unit_body: str) -> dict[str, list[str]]:
    counts: dict[str, list[str]] = {"E": [], "H": []}
    current_section = None
    for line in unit_body.splitlines():
        if line.startswith("### E."):
            current_section = "E"
        elif line.startswith("### H."):
            current_section = "H"
        elif line.startswith("### "):
            current_section = None
        if current_section:
            for match in WORD_COUNT_RE.finditer(line):
                counts[current_section].append(match.group(1) or match.group(2))
    return counts


def validate_unit_order(units: Iterable[UnitBlock]) -> list[str]:
    issues: list[str] = []
    numbers = [u.number for u in units]
    if numbers != sorted(numbers):
        issues.append(f"Unit headings are not in ascending order: {numbers}")
    return issues


def validate_sections(unit: UnitBlock) -> list[str]:
    issues: list[str] = []
    found = [m.group(1) for m in SECTION_HEADING_RE.finditer(unit.body)]
    expected = list("ABCDEFGH")
    missing = [s for s in expected if s not in found]
    if missing:
        issues.append(f"Unit {unit.number}: missing section headings {missing}")
    return issues


def validate_h_order(unit: UnitBlock) -> list[str]:
    issues: list[str] = []
    subsections = find_h_subsections(unit.body)
    expected_order = {"H2": 0, "H3": 1, "H1": 2}
    seen = [s for s in subsections if s in expected_order]
    if seen != sorted(seen, key=lambda s: expected_order[s]):
        issues.append(f"Unit {unit.number}: H subsection order is {seen}; expected H2 -> H3 -> H1 when present")
    return issues


def validate_jpo_labels(text: str) -> list[str]:
    issues: list[str] = []
    raw_jpo_mentions = re.findall(r"JPO context", text)
    labelled_mentions = JPO_LABEL_RE.findall(text)
    if len(raw_jpo_mentions) != len(labelled_mentions):
        issues.append("Some JPO mentions are not formatted as *(JPO context)*")
    return issues


def validate(path: Path) -> int:
    text = read_text(path)
    units = split_units(text)
    issues: list[str] = []
    issues.extend(validate_unit_order(units))
    issues.extend(validate_jpo_labels(text))
    for unit in units:
        issues.extend(validate_sections(unit))
        issues.extend(validate_h_order(unit))

    if issues:
        print(f"Validation issues in {path}:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(f"No structural issues found in {path}")
    return 0


def summary(path: Path) -> int:
    text = read_text(path)
    units = split_units(text)
    print(f"Summary for {path}")
    for unit in units:
        counts = extract_word_counts(unit.body)
        h_subsections = find_h_subsections(unit.body)
        print(f"- Unit {unit.number}: {unit.title}")
        if counts["E"]:
            print(f"  E word counts: {', '.join(counts['E'])}")
        if counts["H"]:
            print(f"  H word counts: {', '.join(counts['H'])}")
        if h_subsections:
            print(f"  H subsections: {', '.join(h_subsections)}")
    return 0


def scaffold(source: Path, dest: Path, force: bool) -> int:
    if not source.exists():
        print(f"Source file does not exist: {source}", file=sys.stderr)
        return 1
    if dest.exists() and not force:
        print(f"Destination already exists: {dest} (use --force to overwrite)", file=sys.stderr)
        return 1

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    print(f"Scaffolded {dest} from {source}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Utilities for N9 module editing.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold_parser = subparsers.add_parser("scaffold", help="Create a destination module file from a source file.")
    scaffold_parser.add_argument("--source", required=True, type=Path)
    scaffold_parser.add_argument("--dest", required=True, type=Path)
    scaffold_parser.add_argument("--force", action="store_true")

    validate_parser = subparsers.add_parser("validate", help="Validate basic N9 structure for a module file.")
    validate_parser.add_argument("--path", required=True, type=Path)

    summary_parser = subparsers.add_parser("summary", help="Print unit and word-count summary for a module file.")
    summary_parser.add_argument("--path", required=True, type=Path)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scaffold":
        return scaffold(args.source, args.dest, args.force)
    if args.command == "validate":
        return validate(args.path)
    if args.command == "summary":
        return summary(args.path)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
