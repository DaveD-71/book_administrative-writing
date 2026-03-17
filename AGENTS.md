# Codex Memory Bootstrap Instructions

Bootstrap-Version: 2026-03-17T18:58:15.2116200+09:00

Scope:

- this file is a duplicated bootstrap instruction file
- the duplicated copies are expected at `%USERPROFILE%\.codex\AGENTS.md` and `<repo-root>\AGENTS.md`

This file defines the shared bootstrap workflow for local and project memory.

## Duplication Rule

- `%USERPROFILE%\.codex\AGENTS.md` and `<repo-root>\AGENTS.md` must carry the same file contents
- do not rewrite, summarize, or manually reconstruct one file from the other
- when one `AGENTS.md` file is missing, create it by direct file copy from the existing one
- treat differences in line endings or filesystem metadata as incidental; the instruction content itself should remain the same

## Workspace Authority

Use this authority order when deciding which project instructions apply:

1. the user's explicit statement about the current workspace
2. the current VS Code workspace or IDE context
3. the repository-root `AGENTS.md` for the active workspace
4. shell cwd only as a fallback when the higher-priority signals are absent

Do not let stale shell cwd or prior-project context override the current workspace.

## Startup Read Order

At session start, read:

1. `%USERPROFILE%\.codex\AGENTS.md` if it exists
2. `<repo-root>\AGENTS.md` if it exists
3. `%USERPROFILE%\.codex\memories\user-learning.md` if it exists

Then, if the active workspace has a repository root, read the repo companion files in this order when they exist:

1. `<repo-root>\user-learning-mirror.md`
2. `<repo-root>\project-learning.md`
3. `<repo-root>\project-journal.md`

Use recent journal entries by default. Read older archive segments only when needed.

## Startup Audit

In the first substantive reply of a new session or after a workspace switch, explicitly report:

- the workspace root being used
- which user-level and project files were read
- whether the repository is a git repo
- whether repo/sync status was checked
- whether project memory already existed
- whether project memory was created or updated during startup handling

If the active workspace contains `<repo-root>\instruction-read-log.csv`, append CSV rows for instruction and memory file reads there.

CSV columns:

- `timestamp_iso`
- `workspace_root`
- `scope`
- `file_path`
- `reason`

CSV encoding rule:

- `<repo-root>\instruction-read-log.csv` must be maintained as UTF-8 text
- if the existing log is not valid UTF-8 or is mixed-encoding, do not keep appending to it
- archive the old log file as-is, create a new UTF-8 `instruction-read-log.csv` with the required header, and continue logging in the new file
- when repairing the log, note the rule in bootstrap memory so the encoding issue is not silently reintroduced

## Missing-File Bootstrap

At session start, do not treat missing memory files as a reason to skip the workflow. Create the missing files immediately when they are expected for the active workspace.

Create as needed:

- `%USERPROFILE%\.codex\AGENTS.md`
- `%USERPROFILE%\.codex\memories\user-learning.md`
- `<repo-root>\AGENTS.md`
- `<repo-root>\user-learning-mirror.md`
- `<repo-root>\project-learning.md`
- `<repo-root>\project-journal.md`
- `<repo-root>\instruction-read-log.csv` with the required CSV header

Bootstrap rule for `AGENTS.md`:

- if one `AGENTS.md` copy exists and the other does not, create the missing copy by direct file copy
- if both copies are missing, create the first copy from the latest approved version-controlled bootstrap source, then direct-copy it to the second location when needed

Bootstrap rule for user-learning:

- if one of `%USERPROFILE%\.codex\memories\user-learning.md` or `<repo-root>\user-learning-mirror.md` exists and the other does not, create the missing file by direct file copy

Bootstrap rule for repo companion files:

- if `<repo-root>\project-learning.md`, `<repo-root>\project-journal.md`, or `<repo-root>\instruction-read-log.csv` is missing, create it at startup before continuing the repo-level workflow

## AGENTS Versioning And Merge

`AGENTS.md` uses versioned merge rules because source authority depends on the situation.

Version rules:

- `Bootstrap-Version` is the required version field for `AGENTS.md`
- a file with no `Bootstrap-Version` is a legacy file
- if both `AGENTS.md` files exist, do not use direct overwrite as the default behavior
- read both `AGENTS.md` copies before deciding whether bootstrap, merge, or conflict handling is required

When both `AGENTS.md` files exist:

1. if one file is legacy and the other is versioned:
   merge the legacy content into the versioned file carefully, then write the resolved result back to both files with a current `Bootstrap-Version`
2. if both files are versioned and the versions differ:
   perform a two-way merge; do not overwrite one side blindly
3. if both files are versioned, the versions match, and the contents differ:
   treat that as drift and perform a two-way merge
4. after a successful merge:
   write the merged result back to both `AGENTS.md` locations so the duplicated instruction files are identical again
5. if the merge cannot be resolved confidently:
   stop and surface the conflict instead of guessing

Merge goal for `AGENTS.md`:

- preserve one shared bootstrap specification
- preserve the current `Bootstrap-Version` or advance it intentionally as part of the resolved merge
- do not keep divergent user-level and repo-level instruction text after merge

## User-Learning Mirror Sync

Canonical user-level memory uses:

- machine-local canonical file: `%USERPROFILE%\.codex\memories\user-learning.md`

Portable workspace mirror uses:

- `<repo-root>\user-learning-mirror.md`

When both files exist:

- compare them at session start
- prefer a merge over blind overwrite when both sides contain unique entries
- dual-write new cross-project lessons to both files when both are available
- merge duplicates instead of appending near-identical entries

What must be synced and where:

- cross-project user lessons belong in both `%USERPROFILE%\.codex\memories\user-learning.md` and `<repo-root>\user-learning-mirror.md`
- `%USERPROFILE%\.codex\memories\user-learning.md` is the machine-local canonical working copy
- `<repo-root>\user-learning-mirror.md` is the repo-tracked transport and mirror copy

## Repo-Tracked Memory Files

These repo files are managed for cross-device propagation through Git rather than through a second Codex-level duplication protocol:

- `<repo-root>\project-learning.md`
- `<repo-root>\project-journal.md`
- `<repo-root>\instruction-read-log.csv`

Use them as follows:

- `<repo-root>\project-learning.md` for durable project facts, goals, constraints, decisions, conventions, and milestone state
- `<repo-root>\project-journal.md` for chronological events, actions, outcomes, and follow-up notes
- `<repo-root>\instruction-read-log.csv` for startup/read audit rows only

Automatically log:

- milestone or stage starts, completions, blocks, or abandonment
- goal or scope changes
- durable decisions about tasks, content, structure, tooling, or direction
- reusable constraints, risks, dependencies, or assumptions
- rejected or replaced approaches and why

## Portability

- resolve user-level Codex paths from `%USERPROFILE%` on each machine rather than assuming a fixed Windows username
- resolve project memory files from the active repository root rather than assuming a fixed local clone path
- treat older absolute project-path references in memory as historical snapshots unless they explicitly claim to define the current workspace root

## Temporary Compatibility Rules

While the Windows Codex sidebar local-link issue remains unresolved:

- prefer plain string file paths for local file references in this pane
- continue to use normal clickable links for web URLs unless a separate issue says otherwise
