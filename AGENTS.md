# Project Agent Instructions

Scope:

- the current repository root containing this `AGENTS.md`

This file defines the project-level Codex memory workflow for this repository.

## Workspace Authority

Use this authority order when deciding which project instructions apply:

1. the user's explicit statement about the current workspace
2. the current VS Code workspace or IDE context
3. this repository-root `AGENTS.md`
4. shell cwd only as a fallback when the higher-priority signals are absent

Do not let stale shell cwd or prior-project context override the current workspace.

## Startup Read Order

After the user-level startup files are read, read:

1. `<repo-root>\AGENTS.md`
2. `<repo-root>\user-learning-mirror.md`
3. `<repo-root>\project-learning.md`
4. `<repo-root>\project-journal.md`

Use recent journal entries by default. Read older archive segments only when needed.

## Startup Audit

In the first substantive reply of a new session or after a workspace switch, explicitly report:

- the workspace root being used
- which user-level and project files were read
- whether the repository is a git repo
- whether repo/sync status was checked
- whether project memory already existed
- whether project memory was created or updated during startup handling

Append CSV rows for instruction and memory file reads to:

- `<repo-root>\instruction-read-log.csv`

CSV columns:

- `timestamp_iso`
- `workspace_root`
- `scope`
- `file_path`
- `reason`

## Missing-File Bootstrap

At session start, do not treat missing memory files as a reason to skip the workflow. Create the missing files immediately when they are expected for the active workspace.

Create as needed:

- `%USERPROFILE%\.codex\AGENTS.md` as the canonical user-level instruction file
- `%USERPROFILE%\.codex\memories\user-learning.md` as the canonical machine-local user memory file
- `<repo-root>\user-learning-mirror.md` as the portable workspace mirror of cross-project user memory
- `<repo-root>\project-learning.md` as the durable project-memory file
- `<repo-root>\project-journal.md` as the chronological project log
- `<repo-root>\instruction-read-log.csv` as the startup/read audit log with the required CSV header

If a repo-root `AGENTS.md` exists but the companion memory files do not, create the companion files before continuing startup handling.

## User-Learning Mirror Sync

User-level memory in this repository uses:

- portable mirror: `<repo-root>\user-learning-mirror.md`
- machine-local canonical file: `%USERPROFILE%\.codex\memories\user-learning.md`

At session start, when both files exist:

- compare them
- prefer the mirror as the portable source in this workspace
- dual-write new cross-project lessons to both files when both are available
- merge duplicates instead of appending near-identical entries

If only one exists in the current environment, keep using that one and sync later.

What must be synced and where:

- Cross-project user lessons belong in both `%USERPROFILE%\.codex\memories\user-learning.md` and `<repo-root>\user-learning-mirror.md` when both files exist
- The canonical machine-local copy lives at `%USERPROFILE%\.codex\memories\user-learning.md`
- The portable workspace copy lives at `<repo-root>\user-learning-mirror.md`
- Project-specific facts, decisions, and status do not go into the user-learning files; they belong in `<repo-root>\project-learning.md`
- Chronological project events do not go into the user-learning files; they belong in `<repo-root>\project-journal.md`
- Instruction-read audit rows do not go into markdown memory files; they belong in `<repo-root>\instruction-read-log.csv`

## Project Logging Rules

Use:

- `project-learning.md` for durable project facts, goals, constraints, decisions, conventions, and milestone state
- `project-journal.md` for chronological events, actions, outcomes, and follow-up notes

Automatically log:

- milestone or stage starts, completions, blocks, or abandonment
- goal or scope changes
- durable decisions about tasks, content, structure, tooling, or direction
- reusable constraints, risks, dependencies, or assumptions
- rejected or replaced approaches and why

## Temporary Compatibility Rules

While the Windows Codex sidebar local-link issue remains unresolved:

- prefer plain string file paths for local file references in this pane
- continue to use normal clickable links for web URLs unless a separate issue says otherwise
