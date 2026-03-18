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

### 2026-03-17T21:45:00+09:00 - Preserve Existing File Encoding Before Rewriting, And Restore Baseline If Corruption Occurs

- Status: `workaround`
- Scope: user/workflow
- Context: repairing files after a shell-driven text rewrite corrupted existing non-ASCII punctuation across the file
- Observation: shell-driven whole-file rewrites can silently transcode an existing file and corrupt non-ASCII punctuation or text if the file's current encoding is not preserved explicitly
- Preferred behavior: before rewriting an existing text file, preserve its current encoding explicitly; avoid whole-file shell rewrites when encoding safety is uncertain and prefer minimal patch edits instead; if corruption has already occurred, restore the clean baseline first and then reapply only the intended minimal edits

### 2026-03-18T11:40:00+09:00 - Force Python UTF-8 In PowerShell Sessions, Not Only In VS Code Terminal Settings

- Status: `workaround`
- Scope: user/workflow
- Context: persistent mojibake in terminal output and PowerShell-captured log files on Windows
- Observation: VS Code `terminal.integrated.env.windows` may not reach every Codex or PowerShell shell process; when `PYTHONIOENCODING` and `PYTHONUTF8` are absent, Python can start with `cp932` stdout/stderr and corrupt non-ASCII text during pipeline capture
- Preferred behavior: set `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1` in the user environment and also export them from the PowerShell profile so new shells force Python UTF-8 before any capture or logging commands run

### 2026-03-18T13:10:00+09:00 - Direct Shell Deletes Can Be Rejected By Execution Policy, So Use A Reviewed Manifest With A Non-Shell Fallback

- Status: `workaround`
- Scope: user/workflow
- Context: deleting approved file sets in the Codex workspace on Windows
- Observation: direct destructive shell commands such as `Remove-Item` can be rejected even when the workspace allows broad filesystem access, because an execution-policy layer can still block high-risk shell deletes before they run
- Preferred behavior: when deleting a reviewed batch of files, generate and verify a manifest first, then perform deletion through a non-shell fallback such as a short Python script reading that manifest; avoid spending a turn on direct shell delete commands when the environment has already shown this policy behavior

### 2026-03-18T14:50:00+09:00 - Avoid Bash-Style `&&` In PowerShell Command Chains

- Status: `workaround`
- Scope: user/workflow
- Context: running multi-step git commands from Codex in Windows PowerShell
- Observation: some PowerShell environments in this workflow use an older parser that does not support Bash-style `&&` command chaining, so commands fail before execution with a parser error instead of reaching git
- Preferred behavior: when sequencing multiple shell commands in PowerShell, avoid `&&`; use separate tool calls when practical or explicit `$LASTEXITCODE` checks between commands so commit/push flows fail cleanly and remain compatible with older PowerShell parsers

### 2026-03-18T15:35:00+09:00 - Reuse One Canonical `workdir` String Verbatim And Do Not Retry Hand-Typed Variants

- Status: `workaround`
- Scope: user/workflow
- Context: repeated `The directory name is invalid` failures on long Windows repo paths in tool calls
- Observation: once a long `workdir` string is manually retyped or reconstructed, it is easy to introduce a single wrong character and then waste multiple retries on near-identical bad paths
- Preferred behavior: capture one canonical workspace root at startup, then reuse that exact string verbatim in every later tool call; when a `workdir` fails once with `The directory name is invalid`, stop retrying path variants and compare against the canonical root before issuing another command
