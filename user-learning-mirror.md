# User Learning Mirror

Portable mirror of user-level lessons relevant to this workspace.

Sync rule:

- compare this file with `%USERPROFILE%\.codex\memories\user-learning.md` at session start when both exist
- prefer this mirror as the portable source in this workspace
- dual-write new cross-project lessons to both files when both are available
- merge duplicates instead of appending near-identical entries

## Entries

### ISSUE 2026-03-14-EXT-01 - Codex VS Code Local File Links Open In Browser

- Timestamp: `2026-03-14T00:00:00+09:00`
- Status: `open`
- Scope: `extension`
- Context: local file links generated in the Codex VS Code sidebar on Windows
- Observation: local file links can route through the browser/webview path instead of opening in a VS Code editor tab
- Preferred behavior: use plain string file paths for local references until the tracked extension issue is fixed and revalidated locally

### 2026-03-14T23:30:00+09:00 - User-Level AGENTS Must Live Under Codex Home

- Status: `workaround`
- Scope: user/workflow
- Context: global Codex instruction discovery
- Observation: the canonical user-level instructions file must live at `%USERPROFILE%\.codex\AGENTS.md`
- Preferred behavior: do not treat `%USERPROFILE%\AGENTS.md` as authoritative unless `CODEX_HOME` is explicitly changed

### 2026-03-15T00:34:37.9048369+09:00 - Workspace Scope Must Follow User Statement And VS Code Workspace

- Status: `workaround`
- Scope: user/workflow
- Context: workspace switching
- Observation: explicit user statements and current VS Code workspace must outrank stale shell cwd and prior-project context
- Preferred behavior: treat previous-project instructions as out of scope immediately once the workspace changes

### 2026-03-15T00:20:00+09:00 - Read Confirmation Events Belong In CSV

- Status: `workaround`
- Scope: user/workflow
- Context: auditing instruction-file reads
- Observation: read-confirmation events should be kept in `instruction-read-log.csv`, not mixed into narrative memory
- Preferred behavior: use CSV for lightweight read audits and markdown for durable lessons

### 2026-03-17T18:58:15.2116200+09:00 - Mixed-Encoding Audit CSVs Must Be Archived And Reset

- Status: `workaround`
- Scope: user/workflow
- Context: repairing `instruction-read-log.csv` after mixed UTF-8 and CP932/Shift-JIS content was detected
- Observation: appending new rows to a mixed-encoding audit CSV makes patching, decoding, and path verification unreliable
- Preferred behavior: keep `instruction-read-log.csv` as UTF-8 text only; if the file is not valid UTF-8, archive the old file, create a new UTF-8 log with the required header, and resume logging there
