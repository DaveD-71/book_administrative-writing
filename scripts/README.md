# Scripts

Utilities for editing and validating the Markdown source files in this repo.

## Current tools

### `module_tool.py`

Small stdlib-only CLI for:

- safely scaffolding a new module output file from an existing source file
- scaffolding a new editorial-pass file by renaming the pass tag automatically
- performing exact-match text edits in Markdown files with Python instead of shell commands
- validating common `N9` structural conventions in a module Markdown file
- reporting unit headings and E/H word-count declarations

### `check_mojibake.py`

Small UTF-8 scanner for common mojibake patterns in repo text files.

## Usage

From the repo root:

```powershell
python scripts/module_tool.py scaffold `
  --source adv/md/revised_modules_step13/aw-adv_mod4_revised.md `
  --dest adv/md/revised_modules_n9/aw-adv_mod4_n9.md
```

```powershell
python scripts/module_tool.py scaffold-pass `
  --source adv/md/revised_modules_n9/aw-adv_mod1_n9.md `
  --dest-dir adv/md/n10 `
  --from-tag _n9 `
  --to-tag _n10
```

```powershell
python scripts/module_tool.py validate `
  --path adv/md/revised_modules_n9/aw-adv_mod3_n9.md
```

```powershell
python scripts/module_tool.py summary `
  --path adv/md/revised_modules_n9/aw-adv_mod3_n9.md
```

```powershell
python scripts/module_tool.py insert-after `
  --path adv/md/n10/aw-adv_mod2_n10.md `
  --unit 4 `
  --marker "#### B1. Compare Two Versions`n" `
  --content "`n> **Why this works:** ...`n"
```

```powershell
python scripts/module_tool.py replace-literal `
  --path adv/md/n10/aw-adv_mod2_n10.md `
  --unit 4 `
  --old-file scripts/tmp/old_block.md `
  --new-file scripts/tmp/new_block.md
```

```powershell
python scripts/check_mojibake.py
```

## Notes

- The script uses only the Python standard library.
- Validation is intentionally conservative: it checks structure and conventions, not writing quality.
- The script is meant to support pass-to-pass module work such as `N9` and `N10`, and can be extended later for broader QA work.
- The editing commands use exact literal matching by default to reduce accidental wide-scope replacements.
- Run `check_mojibake.py` before large regeneration steps or before commit if encoding drift is suspected.

