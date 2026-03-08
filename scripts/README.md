# Scripts

Utilities for editing and validating the Markdown source files in this repo.

## Current tools

### `n9_module_tool.py`

Small stdlib-only CLI for:

- safely scaffolding a new module output file from an existing source file
- validating common `N9` structural conventions in a module Markdown file
- reporting unit headings and E/H word-count declarations

## Usage

From the repo root:

```powershell
python scripts/n9_module_tool.py scaffold `
  --source adv/md/revised_modules_step13/admin-writing-adv_mod4_revised.md `
  --dest adv/md/revised_modules_n9/admin-writing-adv_mod4_n9.md
```

```powershell
python scripts/n9_module_tool.py validate `
  --path adv/md/revised_modules_n9/admin-writing-adv_mod3_n9.md
```

```powershell
python scripts/n9_module_tool.py summary `
  --path adv/md/revised_modules_n9/admin-writing-adv_mod3_n9.md
```

## Notes

- The script uses only the Python standard library.
- Validation is intentionally conservative: it checks structure and conventions, not writing quality.
- The script is meant to support `N9` editing and can be extended later for broader QA work.
