# Advanced `md` Folder

## Active working area — `working/`

- `working/aw-adv-styleref.docx` — reference DOCX, single source of truth for all style definitions.
- `working/<date>.md` — active combined Markdown source for the current conversion pass (e.g. `aw-adv-all_0516.md`).
- `working/aw-adv-all.docx` / `.pdf` — generated build outputs from the current pass.

## Edit history — `edits/`

- `edits/modules/` — canonical module source files (`aw-adv_mod1_n10.md` to `aw-adv_mod6_n10.md`).
- `edits/supplemental/` — companion materials such as the Unit 23 capstone rubric.
- `edits/aw-adv-all_<date>.md` — combined snapshots from previous conversion passes (0510, 0512, 0514).

## Backups — `bak/`

- Backup copies of the reference DOCX before in-place updates.

## Archived material

- Historical source layers live under `adv/archive/md`.

Edit module source files in `edits/modules/` only. Run builds from `working/`.
