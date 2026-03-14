# Project Learning

Durable project memory for `C:\Dev\Code\book_administrative-writing`.

## Entries

### 2026-03-15T00:46:14.1210166+09:00 - Project Scope And Deliverables

- Status: `monitor`
- Scope: project/scope
- Context: repository content audit
- Observation: the repository contains two textbook tracks prepared for the 2026 Japan Patent Office administrative writing proposal: an advanced book under `adv` and an intermediate book under `int`; `about.txt` says the text exists primarily in Markdown and only the first unit of each book has been formatted in Word
- Preferred behavior: treat the repo as a dual-book content workspace with Markdown as the primary working format and Word formatting as a downstream task

### 2026-03-15T00:46:14.1210166+09:00 - Advanced Track Is The Mature Active Workstream

- Status: `monitor`
- Scope: project/state
- Context: advanced planning and status audit
- Observation: `adv/edits & guides/aw-adv_project_todo_list.md` shows N1-N10 complete, N11 not started, and identifies book-wide QA as the next major workstream; the active edited content set is the six `adv/md/n10/aw-adv_mod*_n10.md` files
- Preferred behavior: treat the advanced N10 module set and the N11 QA step as the current highest-maturity content baseline for project planning and review work

### 2026-03-15T00:46:14.1210166+09:00 - Advanced Planning Source Of Truth

- Status: `monitor`
- Scope: project/conventions
- Context: advanced documentation hierarchy
- Observation: `adv/edits & guides/aw-adv_unit_structural_profiles_revised.md` identifies itself as the planning source of truth, and the advanced to-do list treats it and the N10 module files as the authoritative references for editing and QA
- Preferred behavior: when working on advanced content, use the revised structural profiles, the advanced to-do list, and the N10 module files ahead of older context summaries

### 2026-03-15T00:46:14.1210166+09:00 - Advanced Context Document Is Historically Useful But Stale

- Status: `monitor`
- Scope: project/conventions
- Context: comparison of advanced status documents
- Observation: `adv/edits & guides/aw-adv_project_context.md` still describes the project as being in structural planning and lists pre-N9 next steps, which no longer matches the current N10-complete state in `aw-adv_project_todo_list.md`
- Preferred behavior: treat `aw-adv_project_context.md` as historical background only unless it is refreshed; do not use it as the primary status source for current advanced work

### 2026-03-15T00:46:14.1210166+09:00 - Intermediate Track Appears Earlier-Stage Than Advanced

- Status: `monitor`
- Scope: project/state
- Context: intermediate content audit
- Observation: the intermediate track contains `int/aw-int-all.md`, `int/int_writing_text_intro.md`, and 23 split unit files under `int/md`; the introduction presents an A2-B1+ book and the combined file is about 14,978 words, which is materially lighter than the advanced N10 set
- Preferred behavior: assume the intermediate book is a substantial draft set but not yet pushed through the same editorial pass structure or QA framework as the advanced track unless newer intermediate planning documents are added

### 2026-03-15T00:46:14.1210166+09:00 - Local Module Tool Supports Editorial Pass Work

- Status: `monitor`
- Scope: project/tooling
- Context: scripts audit
- Observation: `scripts/module_tool.py` is the repo-local utility for scaffolding new module files, scaffolding pass-to-pass copies, validating N9 structural conventions, summarising module structure, and making exact-match content edits
- Preferred behavior: prefer `scripts/module_tool.py` when doing repetitive module-pass operations or literal Markdown edits related to advanced module workflow

### 2026-03-15T00:34:37.9048369+09:00 - Project Memory Scaffold Initialized

- Status: `resolved`
- Scope: project/workflow
- Context: repository-level Codex memory setup
- Decision: the standard project scaffold was created at the repository root with `AGENTS.md`, `user-learning-mirror.md`, `project-learning.md`, `project-journal.md`, and `instruction-read-log.csv`
- Preferred behavior: keep all project-memory files at the repository root and use them as the authoritative project-level memory layer

### 2026-03-15T00:34:37.9048369+09:00 - Repository Root And Sync Baseline

- Status: `monitor`
- Scope: project/state
- Context: initial scaffold seeding
- Observation: repository root is `C:\Dev\Code\book_administrative-writing`; branch state was `main...origin/main`; `git fetch --dry-run origin` showed no pending remote update at setup time
- Preferred behavior: check repo sync status before substantive work that depends on project instructions or recent remote changes

### 2026-03-15T00:34:37.9048369+09:00 - Initial Visible Repo Structure

- Status: `monitor`
- Scope: project/context
- Context: initial scaffold seeding
- Observation: top-level visible entries included `.vscode`, `adv`, `int`, `scripts`, `about.txt`, `ai_prompt.txt`, `aw-master_activity_menu.md`, and `image_translation_en.txt`
- Preferred behavior: treat `adv`, `int`, and `scripts` as the main high-level areas until more specific project structure decisions are recorded
