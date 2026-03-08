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


def find_unit_bounds(text: str, unit_number: int) -> tuple[int, int]:
    units = split_units(text)
    for index, unit in enumerate(units):
        if unit.number == unit_number:
            start = text.index(unit.body)
            end = start + len(unit.body)
            return start, end
    raise ValueError(f"Unit {unit_number} not found")


def scope_text(text: str, unit_number: int | None) -> tuple[str, int, int]:
    if unit_number is None:
        return text, 0, len(text)
    start, end = find_unit_bounds(text, unit_number)
    return text[start:end], start, end


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


def resolve_input(value: str | None, file_path: Path | None, label: str) -> str:
    if value and file_path:
        raise ValueError(f"Specify either --{label} or --{label}-file, not both")
    if file_path:
        return read_text(file_path)
    if value is not None:
        return value
    raise ValueError(f"Missing required value: --{label} or --{label}-file")


def replace_literal(
    path: Path,
    old_text: str,
    new_text: str,
    unit_number: int | None,
    occurrence: int,
) -> int:
    text = read_text(path)
    scoped, scope_start, scope_end = scope_text(text, unit_number)

    matches = list(re.finditer(re.escape(old_text), scoped))
    if not matches:
        target = f"Unit {unit_number}" if unit_number is not None else "file"
        print(f"Literal text not found in {target}: {path}", file=sys.stderr)
        return 1

    if occurrence < 1 or occurrence > len(matches):
        print(
            f"Occurrence {occurrence} out of range; found {len(matches)} match(es) in {path}",
            file=sys.stderr,
        )
        return 1

    match = matches[occurrence - 1]
    replaced_scope = scoped[: match.start()] + new_text + scoped[match.end() :]
    updated = text[:scope_start] + replaced_scope + text[scope_end:]
    write_text(path, updated)
    print(f"Replaced occurrence {occurrence} in {path}")
    return 0


def insert_after_literal(
    path: Path,
    marker_text: str,
    insert_text: str,
    unit_number: int | None,
    occurrence: int,
) -> int:
    text = read_text(path)
    scoped, scope_start, scope_end = scope_text(text, unit_number)

    matches = list(re.finditer(re.escape(marker_text), scoped))
    if not matches:
        target = f"Unit {unit_number}" if unit_number is not None else "file"
        print(f"Marker text not found in {target}: {path}", file=sys.stderr)
        return 1

    if occurrence < 1 or occurrence > len(matches):
        print(
            f"Occurrence {occurrence} out of range; found {len(matches)} match(es) in {path}",
            file=sys.stderr,
        )
        return 1

    match = matches[occurrence - 1]
    insert_at = match.end()
    updated_scope = scoped[:insert_at] + insert_text + scoped[insert_at:]
    updated = text[:scope_start] + updated_scope + text[scope_end:]
    write_text(path, updated)
    print(f"Inserted after occurrence {occurrence} in {path}")
    return 0


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


def scaffold_pass(source: Path, dest_dir: Path, from_tag: str, to_tag: str, force: bool) -> int:
    if not source.exists():
        print(f"Source file does not exist: {source}", file=sys.stderr)
        return 1

    if from_tag not in source.name:
        print(f"Source filename does not contain tag {from_tag!r}: {source.name}", file=sys.stderr)
        return 1

    dest_name = source.name.replace(from_tag, to_tag)
    if dest_name == source.name:
        print(
            f"Destination filename is unchanged after replacing {from_tag!r} with {to_tag!r}: {source.name}",
            file=sys.stderr,
        )
        return 1

    dest = dest_dir / dest_name
    if dest.exists() and not force:
        print(f"Destination already exists: {dest} (use --force to overwrite)", file=sys.stderr)
        return 1

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    print(f"Scaffolded {dest} from {source}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Utilities for module-file scaffolding, validation, and summaries.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold_parser = subparsers.add_parser("scaffold", help="Create a destination module file from a source file.")
    scaffold_parser.add_argument("--source", required=True, type=Path)
    scaffold_parser.add_argument("--dest", required=True, type=Path)
    scaffold_parser.add_argument("--force", action="store_true")

    pass_parser = subparsers.add_parser(
        "scaffold-pass",
        help="Create a new pass file by copying a source file into a destination directory and renaming its pass tag.",
    )
    pass_parser.add_argument("--source", required=True, type=Path)
    pass_parser.add_argument("--dest-dir", required=True, type=Path)
    pass_parser.add_argument("--from-tag", required=True)
    pass_parser.add_argument("--to-tag", required=True)
    pass_parser.add_argument("--force", action="store_true")

    validate_parser = subparsers.add_parser("validate", help="Validate basic structural conventions for a module file.")
    validate_parser.add_argument("--path", required=True, type=Path)

    summary_parser = subparsers.add_parser("summary", help="Print unit and word-count summary for a module file.")
    summary_parser.add_argument("--path", required=True, type=Path)

    replace_parser = subparsers.add_parser(
        "replace-literal",
        help="Replace an exact literal text block in a Markdown file, optionally scoped to one unit.",
    )
    replace_parser.add_argument("--path", required=True, type=Path)
    replace_parser.add_argument("--old")
    replace_parser.add_argument("--old-file", type=Path)
    replace_parser.add_argument("--new")
    replace_parser.add_argument("--new-file", type=Path)
    replace_parser.add_argument("--unit", type=int)
    replace_parser.add_argument("--occurrence", type=int, default=1)

    insert_parser = subparsers.add_parser(
        "insert-after",
        help="Insert text after an exact literal marker, optionally scoped to one unit.",
    )
    insert_parser.add_argument("--path", required=True, type=Path)
    insert_parser.add_argument("--marker")
    insert_parser.add_argument("--marker-file", type=Path)
    insert_parser.add_argument("--content")
    insert_parser.add_argument("--content-file", type=Path)
    insert_parser.add_argument("--unit", type=int)
    insert_parser.add_argument("--occurrence", type=int, default=1)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scaffold":
        return scaffold(args.source, args.dest, args.force)
    if args.command == "scaffold-pass":
        return scaffold_pass(args.source, args.dest_dir, args.from_tag, args.to_tag, args.force)
    if args.command == "validate":
        return validate(args.path)
    if args.command == "summary":
        return summary(args.path)
    if args.command == "replace-literal":
        try:
            old_text = resolve_input(args.old, args.old_file, "old")
            new_text = resolve_input(args.new, args.new_file, "new")
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return replace_literal(args.path, old_text, new_text, args.unit, args.occurrence)
    if args.command == "insert-after":
        try:
            marker_text = resolve_input(args.marker, args.marker_file, "marker")
            content_text = resolve_input(args.content, args.content_file, "content")
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return insert_after_literal(args.path, marker_text, content_text, args.unit, args.occurrence)

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
