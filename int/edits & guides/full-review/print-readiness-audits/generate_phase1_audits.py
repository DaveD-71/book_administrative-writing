from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "int" / "md" / "working" / "aw-int-all_0519.md"
OUT = Path(__file__).resolve().parent


UNIT_RE = re.compile(r"^## Unit (\d+)\. (.+)$")
H3_RE = re.compile(r"^### (.+)$")
H4_RE = re.compile(r"^#### (.+)$")
LETTER_RE = re.compile(r"^([A-H])\. (.+)$")
DIV_OPEN_RE = re.compile(r"^:::[ \t]+([\w-]+)[ \t]*$")
DIV_CLOSE_RE = re.compile(r"^:::[ \t]*$")
PH_RE = re.compile(r"\{\{(PH-\d+):\s*([^|}]+?)(?:\s*\|\s*rows=(\d+))?\s*\}\}")


def write_csv(name: str, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path = OUT / name
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def unit_ranges(lines: list[str]) -> list[dict[str, object]]:
    units: list[dict[str, object]] = []
    for idx, line in enumerate(lines, 1):
        match = UNIT_RE.match(line)
        if match:
            units.append(
                {
                    "unit": int(match.group(1)),
                    "title": match.group(2),
                    "start": idx,
                    "end": len(lines),
                }
            )
    for pos, unit in enumerate(units[:-1]):
        unit["end"] = int(units[pos + 1]["start"]) - 1
    return units


def containing_unit(units: list[dict[str, object]], line_no: int) -> tuple[str, str]:
    for unit in units:
        if int(unit["start"]) <= line_no <= int(unit["end"]):
            return str(unit["unit"]), str(unit["title"])
    return "", ""


def h3s_for_unit(lines: list[str], unit: dict[str, object]) -> list[tuple[int, str]]:
    heads: list[tuple[int, str]] = []
    for line_no in range(int(unit["start"]), int(unit["end"]) + 1):
        match = H3_RE.match(lines[line_no - 1])
        if match:
            heads.append((line_no, match.group(1)))
    return heads


def main() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    units = unit_ranges(lines)

    heading_rows: list[dict[str, object]] = []
    duplicate_rows: list[dict[str, object]] = []
    first_a_rows: list[dict[str, object]] = []
    h4_letter_rows: list[dict[str, object]] = []
    shell_role_rows: list[dict[str, object]] = []

    for unit in units:
        h3s = h3s_for_unit(lines, unit)
        letters = []
        first_a_line = ""
        first_a_text = ""
        for line_no, text in h3s:
            letter = LETTER_RE.match(text)
            if letter:
                letters.append((line_no, letter.group(1), letter.group(2), text))
                if letter.group(1) == "A" and not first_a_line:
                    first_a_line = str(line_no)
                    first_a_text = text
        sequence = "".join(letter for _, letter, _, _ in letters)
        heading_rows.append(
            {
                "unit": unit["unit"],
                "title": unit["title"],
                "start_line": unit["start"],
                "end_line": unit["end"],
                "h3_letter_sequence": sequence,
                "h3_letter_count": len(letters),
                "first_a_line": first_a_line,
                "first_a_text": first_a_text,
                "clean_standard_sequence": sequence == "ABCDEFGH",
            }
        )

        counts = Counter(letter for _, letter, _, _ in letters)
        by_letter = {letter: full_text for _, letter, _, full_text in letters}
        f_text = by_letter.get("F", "")
        g_text = by_letter.get("G", "")
        f_ok = bool(re.search(r"\b(edit|editing|revision|revise|rewrite)\b", f_text, re.I))
        g_ok = bool(re.search(r"\b(self-check|check|reflection|reflect|review)\b", g_text, re.I))
        if sequence == "ABCDEFGH" and (not f_ok or not g_ok):
            shell_role_rows.append(
                {
                    "unit": unit["unit"],
                    "title": unit["title"],
                    "f_heading": f_text,
                    "g_heading": g_text,
                    "issue": "; ".join(
                        issue
                        for issue, present in [
                            ("F is not editing/revision", not f_ok),
                            ("G is not self-check/reflection/review", not g_ok),
                        ]
                        if present
                    ),
                }
            )
        for letter, count in sorted(counts.items()):
            if count > 1:
                duplicate_rows.append(
                    {
                        "unit": unit["unit"],
                        "title": unit["title"],
                        "letter": letter,
                        "count": count,
                        "instances": " | ".join(
                            f"L{line_no}: {full_text}"
                            for line_no, ltr, _, full_text in letters
                            if ltr == letter
                        ),
                    }
                )

        before_first_a_h4 = []
        if first_a_line:
            first_a_num = int(first_a_line)
            for line_no in range(int(unit["start"]), first_a_num):
                match = H4_RE.match(lines[line_no - 1])
                if match:
                    before_first_a_h4.append(f"L{line_no}: {match.group(1)}")
        if before_first_a_h4 or (first_a_text.startswith("A. Warm-Up") and any("What " in item for item in before_first_a_h4)):
            first_a_rows.append(
                {
                    "unit": unit["unit"],
                    "title": unit["title"],
                    "first_a_line": first_a_line,
                    "first_a_text": first_a_text,
                    "h4_before_first_a": " | ".join(before_first_a_h4),
                }
            )

        for line_no in range(int(unit["start"]), int(unit["end"]) + 1):
            match = H4_RE.match(lines[line_no - 1])
            if not match:
                continue
            letter = LETTER_RE.match(match.group(1))
            if letter:
                h4_letter_rows.append(
                    {
                        "unit": unit["unit"],
                        "title": unit["title"],
                        "line": line_no,
                        "letter": letter.group(1),
                        "heading": match.group(1),
                    }
                )

    write_csv(
        "phase1_unit_heading_sequence_audit.csv",
        [
            "unit",
            "title",
            "start_line",
            "end_line",
            "h3_letter_sequence",
            "h3_letter_count",
            "first_a_line",
            "first_a_text",
            "clean_standard_sequence",
        ],
        heading_rows,
    )
    write_csv(
        "phase1_duplicate_ah_heading_audit.csv",
        ["unit", "title", "letter", "count", "instances"],
        duplicate_rows,
    )
    write_csv(
        "phase1_first_a_preservation_audit.csv",
        ["unit", "title", "first_a_line", "first_a_text", "h4_before_first_a"],
        first_a_rows,
    )
    write_csv(
        "phase1_h4_ah_subordinate_heading_audit.csv",
        ["unit", "title", "line", "letter", "heading"],
        h4_letter_rows,
    )
    write_csv(
        "phase1_shell_role_order_audit.csv",
        ["unit", "title", "f_heading", "g_heading", "issue"],
        shell_role_rows,
    )

    div_rows: list[dict[str, object]] = []
    div_stack: list[tuple[int, str]] = []
    div_counts: Counter[str] = Counter()
    unmatched_closes = []
    for idx, line in enumerate(lines, 1):
        opener = DIV_OPEN_RE.match(line)
        if opener:
            cls = opener.group(1)
            div_stack.append((idx, cls))
            div_counts[cls] += 1
            unit_no, title = containing_unit(units, idx)
            div_rows.append({"line": idx, "event": "open", "class": cls, "unit": unit_no, "title": title})
            continue
        if DIV_CLOSE_RE.match(line):
            unit_no, title = containing_unit(units, idx)
            if div_stack:
                open_line, cls = div_stack.pop()
                div_rows.append({"line": idx, "event": "close", "class": cls, "unit": unit_no, "title": title})
            else:
                unmatched_closes.append(idx)
                div_rows.append({"line": idx, "event": "unmatched_close", "class": "", "unit": unit_no, "title": title})
    for open_line, cls in div_stack:
        unit_no, title = containing_unit(units, open_line)
        div_rows.append({"line": open_line, "event": "unclosed_open", "class": cls, "unit": unit_no, "title": title})
    write_csv("phase1_div_balance_and_class_audit.csv", ["line", "event", "class", "unit", "title"], div_rows)

    placeholder_rows: list[dict[str, object]] = []
    placeholder_size_rows: list[dict[str, object]] = []
    seen_ids: Counter[str] = Counter()
    for idx, line in enumerate(lines, 1):
        for match in PH_RE.finditer(line):
            ph_type, ph_id, rows = match.groups()
            seen_ids[ph_id.strip()] += 1
            unit_no, title = containing_unit(units, idx)
            context = ""
            for lookback in range(idx - 1, max(idx - 8, 0), -1):
                if H3_RE.match(lines[lookback - 1]) or H4_RE.match(lines[lookback - 1]) or DIV_OPEN_RE.match(lines[lookback - 1]):
                    context = lines[lookback - 1].strip()
                    break
            numbered_items_since_context = 0
            if context:
                context_line = next(
                    (
                        lookback
                        for lookback in range(idx - 1, 0, -1)
                        if lines[lookback - 1].strip() == context
                    ),
                    max(idx - 12, 1),
                )
            else:
                context_line = max(idx - 12, 1)
            for scan_line in range(context_line + 1, idx):
                if re.match(r"^\s*(?:\*\*)?\d+[\.)]", lines[scan_line - 1]):
                    numbered_items_since_context += 1
            immediately_after_single_item = any(
                re.match(r"^\s*(?:\*\*)?\d+[\.)]", lines[lookback - 1])
                for lookback in range(max(1, idx - 3), idx)
            )
            placeholder_rows.append(
                {
                    "unit": unit_no,
                    "title": title,
                    "line": idx,
                    "type": ph_type,
                    "id": ph_id.strip(),
                    "rows": rows or "",
                    "has_rows": bool(rows),
                    "context": context,
                    "raw": match.group(0),
                }
            )
            if (
                rows
                and numbered_items_since_context
                and int(rows) < numbered_items_since_context
                and not immediately_after_single_item
            ):
                placeholder_size_rows.append(
                    {
                        "unit": unit_no,
                        "title": title,
                        "line": idx,
                        "id": ph_id.strip(),
                        "rows": rows,
                        "numbered_items_since_context": numbered_items_since_context,
                        "context": context,
                        "raw": match.group(0),
                    }
                )
    for row in placeholder_rows:
        row["duplicate_id_count"] = seen_ids[row["id"]]
    write_csv(
        "phase1_placeholder_inventory.csv",
        ["unit", "title", "line", "type", "id", "rows", "has_rows", "duplicate_id_count", "context", "raw"],
        placeholder_rows,
    )
    write_csv(
        "phase1_placeholder_size_risk_audit.csv",
        ["unit", "title", "line", "id", "rows", "numbered_items_since_context", "context", "raw"],
        placeholder_size_rows,
    )

    list_style_rows = []
    list_item_re = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.+)$")
    for idx, line in enumerate(lines, 1):
        match = list_item_re.match(line)
        if not match:
            continue
        item_text = match.group(3).strip()
        if not item_text or item_text.startswith("[ ]"):
            continue
        previous_nonblank = ""
        for lookback in range(idx - 1, 0, -1):
            if lines[lookback - 1].strip():
                previous_nonblank = lines[lookback - 1].strip()
                break
        starts_lower = item_text[0].islower()
        lacks_terminal = item_text[-1] not in ".?!:;"
        follows_colon_or_sentence = previous_nonblank.endswith(":") or previous_nonblank.endswith(".")
        fragment_leadin = bool(re.search(r"\b(include|includes|such as|for example|for instance):$", previous_nonblank, re.I))
        is_fragment_list = fragment_leadin and not re.match(
            r"(?i)^(read|write|choose|underline|complete|use|finish|check|rewrite|revise|compare|identify|state|request|explain|circle|highlight|answer|select|add|remove)\b",
            item_text,
        )
        if follows_colon_or_sentence and not is_fragment_list and (starts_lower or lacks_terminal):
            unit_no, title = containing_unit(units, idx)
            list_style_rows.append(
                {
                    "unit": unit_no,
                    "title": title,
                    "line": idx,
                    "issue": "; ".join(
                        issue
                        for issue, present in [
                            ("starts_lowercase", starts_lower),
                            ("missing_terminal_punctuation", lacks_terminal),
                        ]
                        if present
                    ),
                    "previous_line": previous_nonblank,
                    "item": item_text,
                }
            )
    write_csv(
        "phase1_list_capitalization_punctuation_audit.csv",
        ["unit", "title", "line", "issue", "previous_line", "item"],
        list_style_rows,
    )

    generic_rows = []
    generic_re = re.compile(r"\b(Write Here|Use this box|Write your answer below|Response|Your answer)\b", re.I)
    for idx, line in enumerate(lines, 1):
        if generic_re.search(line):
            unit_no, title = containing_unit(units, idx)
            generic_rows.append({"unit": unit_no, "title": title, "line": idx, "text": line.strip()})
    write_csv("phase1_generic_label_audit.csv", ["unit", "title", "line", "text"], generic_rows)

    blank_rows = []
    run_start = None
    run_len = 0
    for idx, line in enumerate(lines + ["not blank"], 1):
        if line.strip() == "":
            if run_start is None:
                run_start = idx
            run_len += 1
        else:
            if run_len >= 3 and run_start is not None:
                unit_no, title = containing_unit(units, run_start)
                blank_rows.append({"unit": unit_no, "title": title, "start_line": run_start, "blank_line_count": run_len})
            run_start = None
            run_len = 0
    write_csv("phase1_excessive_blank_line_audit.csv", ["unit", "title", "start_line", "blank_line_count"], blank_rows)

    arrow_rows = []
    for idx, line in enumerate(lines, 1):
        if "->" in line or "→" in line:
            unit_no, title = containing_unit(units, idx)
            arrow_rows.append({"unit": unit_no, "title": title, "line": idx, "text": line.strip()})
    write_csv("phase1_visible_arrow_spacing_audit.csv", ["unit", "title", "line", "text"], arrow_rows)

    module_rows = []
    in_review = False
    review_heading = ""
    for idx, line in enumerate(lines, 1):
        if line.startswith("## Module ") and "Review Workshop" in line:
            in_review = True
            review_heading = line[3:]
        elif line.startswith("## Unit "):
            in_review = False
            review_heading = ""
        elif in_review and line.startswith("### "):
            text = line[4:]
            module_rows.append(
                {
                    "review": review_heading,
                    "line": idx,
                    "heading": text,
                    "starts_lowercase": bool(text and text[0].islower()),
                    "contains_lowercase_module": "module " in text,
                }
            )
    write_csv(
        "phase1_module_review_heading_capitalization_audit.csv",
        ["review", "line", "heading", "starts_lowercase", "contains_lowercase_module"],
        module_rows,
    )

    summary = OUT / "phase1_audit_summary.md"
    summary.write_text(
        "\n".join(
            [
                "# Phase 1 Audit Summary",
                "",
                f"Source: `{SRC.relative_to(ROOT)}`",
                "",
                f"- Units found: {len(units)}",
                f"- Units with clean `ABCDEFGH` H3 letter sequence: {sum(1 for r in heading_rows if r['clean_standard_sequence'])}",
                f"- Clean-sequence units with wrong F/G role labels: {len(shell_role_rows)}",
                f"- Duplicate A-H heading rows: {len(duplicate_rows)}",
                f"- First-A preservation review rows: {len(first_a_rows)}",
                f"- Lettered H4 subordinate headings: {len(h4_letter_rows)}",
                f"- Div opens by class: {dict(sorted(div_counts.items()))}",
                f"- Unclosed div opens: {sum(1 for r in div_rows if r['event'] == 'unclosed_open')}",
                f"- Unmatched div closes: {len(unmatched_closes)}",
                f"- Placeholders: {len(placeholder_rows)}",
                f"- Placeholders without rows: {sum(1 for r in placeholder_rows if not r['has_rows'])}",
                f"- Placeholder IDs with duplicates: {sum(1 for k, v in seen_ids.items() if v > 1)}",
                f"- Placeholder size risk rows: {len(placeholder_size_rows)}",
                f"- List capitalization/punctuation review rows: {len(list_style_rows)}",
                f"- Generic label hits: {len(generic_rows)}",
                f"- Excessive blank-line runs: {len(blank_rows)}",
                f"- Visible arrow hits: {len(arrow_rows)}",
                f"- Module review heading rows: {len(module_rows)}",
                "",
                "CSV files in this folder contain the detailed inventories.",
                "",
            ]
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
