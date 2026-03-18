# Project Journal

Chronological project events for the active repository root.

Historical note:

- older entries may contain absolute paths from earlier machines or clone locations
- treat those path values as historical snapshots unless an entry explicitly states it is defining the current workspace root

## Entries

### 2026-03-15T00:46:14.1210166+09:00 - Fresh Startup Pass And Repository Audit

- Performed a clean startup pass using the repo-local scaffold:
  - `C:\Users\daved\.codex\AGENTS.md`
  - `C:\Users\daved\.codex\memories\user-learning.md`
  - `C:\Dev\Code\book_administrative-writing\AGENTS.md`
  - `C:\Dev\Code\book_administrative-writing\user-learning-mirror.md`
  - `C:\Dev\Code\book_administrative-writing\project-learning.md`
  - `C:\Dev\Code\book_administrative-writing\project-journal.md`
- Confirmed repo status remained `main...origin/main` with no pending remote update from `git fetch --dry-run origin`
- Audited substantive project files:
  - top-level context in `about.txt`, `ai_prompt.txt`, and `aw-master_activity_menu.md`
  - advanced planning/status files in `adv/edits & guides`
  - intermediate introduction and combined draft files in `int`
  - local tooling in `scripts/README.md`
- Updated project memory to reflect:
  - dual-book project scope
  - advanced track as the mature active workstream
  - the revised advanced structural profiles and to-do list as the authoritative current references
  - the older advanced context document as stale background
  - the intermediate track as earlier-stage than advanced
  - `scripts/module_tool.py` as the local module-pass utility

### 2026-03-15T00:59:14.7432774+09:00 - N11 QA Workstream Started

- Read the advanced N11 source set:
  - `adv/edits & guides/planning/aw-adv_project_todo_list.md`
  - `adv/edits & guides/references/excerpt from Step14 thread.md`
  - `adv/edits & guides/n10/aw-adv_n10_language_instruction_framework.md`
  - `adv/edits & guides/planning/aw-adv_prompt-writing-policy.md`
  - `adv/md/revised_modules_n9/Codex QA protocol and checks/aw-adv_n9_module_editing_protocol.md`
  - `adv/md/revised_modules_n9/Codex QA protocol and checks/aw-adv_n9_qa_checklist_template.md`
- Drafted the new book-wide QA framework:
  - `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md`
- Updated the advanced to-do list so `N11` is now marked `In progress`
- Recorded in project memory that the new `N11` checklist is the authoritative next-stage QA framework for the advanced track

### 2026-03-15T01:07:00+09:00 - N11 Round 1 Findings Logged

- Ran initial structured checks against the active `n10` module files and supporting project docs
- Recorded the first review note at:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md`
- Confirmed in the active `n10` files:
  - `P2` B7 tasks are present in Units 11, 13, 17, and 21
  - `P6` B6 tasks are present in Units 15, 18, 19, and 22
  - Module 2 Section H ordering remains correct
- Logged active follow-up items:
  - portfolio-task units need manual QA beyond the summary script
  - `P7` remains deferred despite Unit 23 now containing a rubric-based self-edit table
  - `P1` final structural-variety confirmation remains a live `N11` task

### 2026-03-15T01:12:00+09:00 - N11 Manual Pass On Portfolio Units

- Manually reviewed Unit 14 and Unit 22 because `module_tool.py summary` does not fully expose `E4` portfolio-task word counts
- Confirmed:
  - Unit 14 `E4` clearly defines `Task 1` and `Task 2` word-count ranges
  - Unit 22 `E4` clearly defines planning-note and full-document ranges
  - Unit 22 includes explicit fallback and transfer support rather than assuming prior saved work
- Updated `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md` so these items now record as `Pass`, with the tooling limitation noted separately

### 2026-03-15T01:18:00+09:00 - N11 Broader Variety And Support Check

- Counted explanation/support markers across the six active `n10` module files and confirmed the `N10` pedagogical layer is visibly embedded across the full book, though final sufficiency remains a qualitative QA question
- Confirmed broad activity-type variety is present in the active files rather than only in the planning documents
- Identified the remaining likely book-level variety risk as possible scenario-family / JPO-option overlap, especially in some Modules 2 and 4 interoffice coordination prompts
- Updated `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md` with these findings

### 2026-03-15T15:16:24.7226107+09:00 - N11 Sameness Pass Prompt Repairs

- Reviewed clustered prompt families in Modules 2 and 4 for real overlap rather than mere thematic similarity
- Confirmed and repaired four genuine JPO homework-option overlaps in the active `n10` files:
  - Unit 4 `H3`
  - Unit 6 `H3`
  - Unit 13 `H3`
  - Unit 15 `H3`
- The revised prompts now preserve the target skill while using more distinct contexts from their paired freer-writing JPO options
- Recorded the repaired-status finding in `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md`

### 2026-03-15T19:32:00+09:00 - N11 Checklist Tightened And Round 2 Findings Recorded

- Updated `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md` so `N11` now explicitly tests:
  - B1+/B2 prompt readability
  - drift into over-dense or overly sophisticated prompt wording
  - book-level scenario-family clustering, especially in JPO contexts
- Added named requirement sources for those new checks using:
  - `adv/edits & guides/planning/aw-adv_project_context.md`
  - `adv/edits & guides/planning/aw-adv_prompt-writing-policy.md`
  - `adv/edits & guides/planning/aw-adv_unit_structural_profiles_revised.md`
  - `adv/edits & guides/planning/aw-adv_project_todo_list.md`
- Recorded the focused second-pass review at:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md`
- Round 2 conclusion:
  - the earlier overlap repairs improved local distinctness
  - but Modules 2 and 4 still contain JPO prompts that are too dense and too clustered around trilateral / counterpart-office coordination
  - the remaining `N11` correction target is now narrower and clearer than before

### 2026-03-15T19:32:00+09:00 - Full Round 2 Pass Completed Across Units 1-23

- Re-read all six active `n10` module files as a genuine full-book Round 2 pass after the checklist revision
- Treated the earlier Round 1 note as historical background only, because the revised checklist changed the operative QA standard
- Rewrote `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md` so it now records:
  - full-book coverage across Units 1-23 and all A-H sections
  - broad passes in pedagogical support, learner-level scaffolding, progression, and activity-type variety
  - structural / coding cleanup still needed in Modules 1 and 3
  - JPO prompt-load and scenario-clustering problems still active in Modules 2 and 4
- Updated the to-do list so the current `N11` blockers are now stated in that narrower, more accurate form

### 2026-03-15T20:05:00+09:00 - Round 3 Completed After Claude Checklist Verification

- Read and cross-checked:
  - `adv/edits & guides/n11/aw-adv_n11_claude-fb_qa_checklist.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_checklist_v2_claude.md`
  - `adv/edits & guides/n10/aw-adv_n10_claude-fb_mod1-3_v2.md`
  - `adv/edits & guides/n10/aw-adv_n10_claude-fb_mod4-6_v2.md`
  - `adv/edits & guides/steps/aw-adv_step11_learning-goals-mapping.md`
  - live active `n10` module files for the specific open blockers
- Upgraded `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md` so the main checklist now includes the stronger v2 controls rather than leaving them only in the Claude draft
- Created the new operative QA record:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
- Round 3 outcome:
  - kept the Modules 2 and 4 JPO prompt blockers as live
  - confirmed the unresolved H1/profile mismatch in Units 2, 3, 4, 6, and 11 as a real sign-off blocker
  - confirmed Module 1 structural cleanup remains live
  - carried Unit 20 structural defects into the operative blocker list
  - withdrew three older issues from the live blocker list:
    - broader missing-H3 concern across Module 3
    - Unit 21 word-count inconsistency as a current active-file defect
    - Unit 19 Practice D placement problem as a current active-file defect
- Updated the advanced to-do list so Round 3, not Round 2, is now the operative `N11` summary

### 2026-03-16T02:05:00+09:00 - Applied The Full Round 3 Correction Set To The Active Files

- Implemented the H1 decision by updating the structural profiles for Units 2, 3, 4, 6, 11, and 19 and by adding the missing live-file H labels/content in Module 1 and Unit 19
- Removed the duplicate loose `F1` blocks in Module 1 Units 2 and 3 and normalised explicit H3 / H1 sub-labelling across Units 1-3
- Revised the flagged JPO prompts in Modules 2 and 4 so the active options are shorter, less clustered around the same trilateral/counterpart-office family, and more clearly separated within their units
- Resolved Unit 20 structural defects by removing the duplicate `B1` heading and aligning the profile note with the current `D2` design rather than an obsolete `D3` expectation
- Updated the operative checklist and to-do list so the Round 3 blocker set is now treated as corrected-in-source, with a targeted recheck as the next QA step

### 2026-03-16T09:28:49.3778502+09:00 - Completed The Remaining Five-Unit H1 Rollout

- Confirmed and preserved the live H1 additions for Unit 18 and Units 20-23 in the active `n10` files
- Confirmed the corresponding structural-profile rows for Units 18 and 20-23, including Unit 23's capstone-appropriate reflection / transfer framing
- Updated the operative checklist, Round 3 implementation note, and advanced to-do list so they now describe H1 as a book-wide feature rather than as a correction limited to the earlier mismatch set

### 2026-03-15T00:34:37.9048369+09:00 - Codex Memory Scaffold Created

- Workspace root confirmed from VS Code state as `C:\Dev\Code\book_administrative-writing`
- Verified this workspace is a git repository with root `C:\Dev\Code\book_administrative-writing`
- Verified `main...origin/main` and no pending remote update from `git fetch --dry-run origin`

### 2026-03-17T18:58:15.2116200+09:00 - Archived Mixed-Encoding Instruction Read Log And Reset UTF-8 CSV

- Confirmed that `instruction-read-log.csv` was no longer valid UTF-8 because older rows contained CP932/Shift-JIS-era path bytes while newer rows had been appended in UTF-8
- Archived the mixed-encoding log in the repo root rather than continuing to append to it
- Recreated `instruction-read-log.csv` as a clean UTF-8 file with the required header and current-session startup rows only
- Updated the bootstrap instructions and user-learning mirror so future startup logging treats mixed-encoding audit CSVs as repair-and-reset cases rather than append-in-place cases
- Created repository-root memory scaffold:
  - `AGENTS.md`
  - `user-learning-mirror.md`
  - `project-learning.md`
  - `project-journal.md`
  - `instruction-read-log.csv`
- Seeded the scaffold with current user-level compatibility rules and initial repository context

### 2026-03-16T11:07:11.6171964+09:00 - Work PC Local Codex Home Bootstrap

- Read the repository-root memory files during startup handling:
  - `AGENTS.md`
  - `user-learning-mirror.md`
  - `project-learning.md`
  - `project-journal.md`
- Confirmed the repo already contains the project memory scaffold and `instruction-read-log.csv`
- Found that this work PC already has a local Codex home under `C:\Users\d-dobson`, but it did not have the user-level `AGENTS.md` or canonical `memories\user-learning.md` files that this repo expects; the weekend bootstrap had also hardcoded `C:\Users\daved`
- Updated the repo-local memory instructions so repo paths resolve from the active repository root and user-level paths resolve from `%USERPROFILE%\.codex`
- Created the local bootstrap under:
  - `%USERPROFILE%\.codex\AGENTS.md`
  - `%USERPROFILE%\.codex\memories\user-learning.md`
- Read back the new local files and confirmed the canonical user-learning file matches the repo mirror in content
- Noted an environment limitation for this machine session:
  - `.git` exists in the workspace, but `git` is not available on `PATH`, so repo/sync status could not be verified with normal git commands

### 2026-03-16T11:07:11.6171964+09:00 - Work PC Git Shell Access Repaired

- Confirmed Git for Windows was already installed at:
  - `C:\Users\d-dobson\AppData\Local\Programs\Git\cmd\git.exe`
- Found the actual problem was shell environment setup:
  - the user `Path` did not include the Git `cmd` directory
  - PowerShell profile loading was blocked until `CurrentUser` execution policy was set to `RemoteSigned`
- Repaired the local setup by:
  - appending `C:\Users\d-dobson\AppData\Local\Programs\Git\cmd` to the user `Path`
  - creating `C:\Users\d-dobson\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` with a fallback Git path prepend
  - setting the current-user execution policy to `RemoteSigned`
- Verified from a fresh shell invocation that:
  - `git --version` now succeeds
  - `git status --short --branch` now succeeds in this repository

### 2026-03-16T11:46:18.7935300+09:00 - Expanded The User-Level AGENTS Bootstrap

- Re-reviewed whether the local `C:\Users\d-dobson\.codex\AGENTS.md` created during work-PC setup was sufficient
- Confirmed it was too thin for the intended cross-device workflow because it did not itself carry the startup-read order, startup audit, mirror-sync, and project-logging rules
- Replaced it with a fuller user-level bootstrap that now includes:
  - workspace authority order
  - user-level and project-level startup read order
  - startup audit requirements
  - mirror sync rules between `%USERPROFILE%\.codex\memories\user-learning.md` and `<repo-root>\user-learning-mirror.md`
  - project-memory logging rules
  - portability and local-link compatibility rules

### 2026-03-16T11:55:43.6239833+09:00 - Made File Creation And Sync Targets Explicit In The Instructions

- Tightened both the repo `AGENTS.md` and the user-level `C:\Users\d-dobson\.codex\AGENTS.md`
- Added an explicit missing-file bootstrap section that now requires creating expected memory files instead of silently skipping the workflow when they are absent
- Added explicit sync-target rules that now state:
  - cross-project user lessons sync between `%USERPROFILE%\.codex\memories\user-learning.md` and `<repo-root>\user-learning-mirror.md`
  - project facts and decisions belong in `<repo-root>\project-learning.md`
  - chronological project events belong in `<repo-root>\project-journal.md`
  - instruction-read audit rows belong in `<repo-root>\instruction-read-log.csv`

### 2026-03-16T12:06:28.8563703+09:00 - Added The Missing Repo-Level AGENTS Creation Rule

- Re-reviewed the explicit bootstrap rules and confirmed one omission remained:
  - the instructions still did not explicitly require creating `<repo-root>\AGENTS.md` when a fresh clone lacks it
- Updated both the repo `AGENTS.md` and the user-level `C:\Users\d-dobson\.codex\AGENTS.md` so they now state that:
  - `<repo-root>\AGENTS.md` must be created from the user-level bootstrap when missing
  - the shared bootstrap instructions must exist in both the user-level and repo-level `AGENTS.md` files
  - those overlapping sections should be kept aligned, while the repo copy remains adapted to repo-local paths and project-specific additions
- Historical note:
  - this entry is now superseded by the later versioned shared-spec model

### 2026-03-16T12:08:01.0802098+09:00 - Tightened The AGENTS Duplication Rule To Full Alignment

- Re-reviewed the AGENTS duplication language after the user pointed out that partial alignment is still too weak
- Updated both the repo `AGENTS.md` and the user-level `C:\Users\d-dobson\.codex\AGENTS.md` so they now require:
  - full alignment between the duplicated `AGENTS.md` files
  - `%USERPROFILE%\.codex\AGENTS.md` as the canonical source
  - only deterministic repo-root path substitution and explicit project-specific additions as allowed differences in `<repo-root>\AGENTS.md`
- Historical note:
  - this entry is now superseded by the later versioned shared-spec model, which requires identical duplicated content after bootstrap or merge

### 2026-03-16T13:36:04.9560756+09:00 - Replaced The AGENTS Sync Rules With A Versioned Bootstrap Spec

- Reworked both `AGENTS.md` files into the same shared bootstrap specification instead of keeping two similar-but-different texts
- Added explicit rules that now distinguish:
  - direct file copy for missing-file bootstrap cases
  - versioned two-way merge for cases where both `AGENTS.md` files already exist
  - legacy handling for unversioned `AGENTS.md` files
- Removed the earlier implication that repo-level project memory files require the same duplication protocol as the `AGENTS.md` pair
- Clarified that:
  - `project-learning.md`
  - `project-journal.md`
  - `instruction-read-log.csv`
  are repo-tracked files managed across devices through Git, while `user-learning-mirror.md` still participates in semantic mirror sync with the local user-learning file

### 2026-03-16T13:39:46.8020732+09:00 - Corrected The First Shared-Spec Rewrite

- Re-reviewed the rewritten shared `AGENTS.md` spec before commit
- Corrected three issues:
  - startup read order now explicitly reads both `%USERPROFILE%\.codex\AGENTS.md` and `<repo-root>\AGENTS.md` when they exist
  - `Bootstrap-Version` is now expressed as a stricter plain-text field rather than markdown-styled text
  - the earlier clone/alignment memory entries are now marked as superseded so they do not compete with the current versioned merge model

### 2026-03-16T13:39:46.8020732+09:00 - Bootstrap Version Format Tightened To Full Timestamp

- Followed up on the `AGENTS.md` version field after noting that date-only same-day versioning would be ambiguous across home and work machines
- Updated both live `AGENTS.md` copies so `Bootstrap-Version` now uses a full timestamp with timezone offset rather than a coarse same-day label
- Kept the format aligned with the timestamp style already used throughout the memory files

### 2026-03-17T19:48:30.4465385+09:00 - Implemented The Unit 23 Dual-Use Capstone Rubric

- Replaced the old ten-item checklist-style `F3` table in `adv/md/n10/aw-adv_mod6_n10.md` with an eight-criterion learner-facing self-assessment rubric
- Added a framing note in Unit 23 explaining that the rubric categories map to the book's major cumulative skill strands
- Created the companion Unit 23 rubric at `adv/md/n10/aw-adv_unit23_capstone_rubric.md`
- Kept the learner and teacher rubrics aligned to the same eight analytic criteria:
  - Task Fulfillment
  - Source Coverage
  - Synthesis
  - Issue Analysis and Judgment
  - Actions and Next Steps
  - Audience, Tone, and Register
  - Structure and Cohesion
  - Language Precision
- Kept the shared three-band model with no numeric scoring:
  - `Strong`
  - `Developing`
  - `Needs work`
- Updated the advanced to-do list so `P7` now records as complete and the remaining sequence now moves to full review, then `P4`

### 2026-03-17T21:20:00+09:00 - Created A Formal N11 Grouped-Option Issue List

- Re-audited the live `adv/md/n10` files for grouped-option parallelism before moving into full review
- Confirmed that earlier Round 2 / Round 3 findings on JPO-option calibration and within-set parallelism were not sufficiently closed by the later targeted recheck
- Created `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
- The issue list:
  - carries forward the earlier grouped-option findings from the Round 1 / Round 2 / Round 3 QA history
  - records current live-file evidence for the still-open Module 2 and Module 4 issues
  - adds newly surfaced Module 6 grouped-option outliers
- Treat this issue list as the working basis for reopening the grouped-option portion of `N11` before full review

### 2026-03-17T21:35:00+09:00 - Updated The Live QA Files For Tomorrow's Restart

- Rewrote the `N11` row in `adv/edits & guides/planning/aw-adv_project_todo_list.md` so it now clearly shows as reopened
- Updated the remaining-work sequence in the to-do list so the next order is:
  - complete `N11`
  - full review
  - `P4`
- Added direct restart references in the to-do list pointing to:
  - `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md`
- Updated `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md` so the 2026-03-17 targeted recheck is now treated as an intermediate recheck rather than final sign-off

### 2026-03-18T00:00:00+09:00 - Reorganized Advanced Edit Guides Into Functional Subfolders

- Created functional subfolders under `adv/edits & guides`:
  - `planning`
  - `n10`
  - `n11`
  - `steps`
  - `references`
- Moved the existing advanced guide files into those subfolders by document role
- Updated repo references to the new relative paths so the moved files remain discoverable from the to-do list, QA notes, planning docs, and project memory
- This cleanup is structural only; it does not change the active `adv/md/n10` content baseline or the reopened `N11` task scope

### 2026-03-18T00:25:00+09:00 - Began The Reopened N11 Source Pass On Grouped-Option Issues

- Started the live source-edit pass for the known grouped-option issue list in:
  - `adv/md/n10/aw-adv_mod2_n10.md`
  - `adv/md/n10/aw-adv_mod4_n10.md`
  - `adv/md/n10/aw-adv_mod6_n10.md`
- Revised all ten `GO-01` to `GO-10` items listed in `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
- The edits focused on:
  - improving within-set option parallelism
  - reducing JPO-option load where it was inflated
  - making dependency chains explicit where the JPO option had been flatter than its peers
  - separating overly similar JPO `E` / `H3` pairings more clearly
- `N11` remains open after this pass because the revised option sets still need an explicit recheck against:
  - `5B.1 Level appropriacy`
  - `5D.3 Calibration`
  - `5D.4 Choice-list quality`
  - `5E.3 Variety without chaos`

### 2026-03-18T00:45:00+09:00 - Completed The Explicit Recheck Of The Known Grouped-Option Issue Set

- Rechecked the revised `GO-01` to `GO-10` items against:
  - `5B.1 Level appropriacy`
  - `5D.3 Calibration`
  - `5D.4 Choice-list quality`
  - `5E.3 Variety without chaos`
- Recorded the recheck result in:
  - `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
- Current state:
  - the known grouped-option issue list is now clear at unit level
  - `N11` remains open because the broader six-module book-level recheck has not yet been completed

### 2026-03-18T00:55:00+09:00 - Completed The Broader N11 Full-Book Recheck

- Ran the broader recheck across all six live `adv/md/n10/aw-adv_mod*_n10.md` files against:
  - `5B.1 Level appropriacy`
  - `5D.3 Calibration`
  - `5D.4 Choice-list quality`
  - `5E.3 Variety without chaos`
- Identified and tightened two additional book-level outliers during the wider pass:
  - `adv/md/n10/aw-adv_mod2_n10.md` Unit 6 `E1`
  - `adv/md/n10/aw-adv_mod4_n10.md` Unit 13 `E1`
- Reviewed the remaining JPO option sets in Modules 3 and 5 and retained them as acceptable rather than as active blockers
- Updated the live QA/control files so they now reflect `N11` completion:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
  - `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
  - `adv/edits & guides/planning/aw-adv_project_todo_list.md`
- Current stage after this pass:
  - `N11` is now complete
  - the next project stage is full review

### 2026-03-18T02:05:00+09:00 - Completed Clean-Sheet N11 Round 4 And Repointed The Final Record

- Ran a new clean-sheet `N11` Round 4 full-book QA pass using `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md` as the operative standard and treating the earlier round files as historical evidence only
- Created the standalone Round 4 artifact:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round4.md`
- During the live-file pass, found one remaining cross-module structural-consistency family that had not been fully closed earlier:
  - Module 2 still had code-first activity headings and mixed Section H labels
  - Modules 3, 4, and 5 still used inconsistent Section H labels
- Corrected that formatting family in the live files:
  - `adv/md/n10/aw-adv_mod2_n10.md`
  - `adv/md/n10/aw-adv_mod3_n10.md`
  - `adv/md/n10/aw-adv_mod4_n10.md`
  - `adv/md/n10/aw-adv_mod5_n10.md`
- Final Round 4 state:
  - the structural-consistency family was cleared in the same pass
  - no unresolved `Revise` blocker remained after correction
  - Round 4 therefore passed and now replaces Round 3 as the authoritative final `N11` record
- Updated the project control file:
  - `adv/edits & guides/planning/aw-adv_project_todo_list.md`
- Next stage after Round 4:
  - full review

### 2026-03-18T18:04:43+09:00 - Saved The Intermediate Development Plan For Later Execution

- Reviewed the actual intermediate draft shape in `int`, the advanced planning and QA artifacts, and the relevant project-memory lessons before drafting the intermediate workflow
- Confirmed the current intermediate baseline:
  - full 23-unit split draft set in `int/md`
  - intro at `int/int_writing_text_intro.md`
  - combined file `int/aw-int-all.md` present but better treated as a reference snapshot until the split-unit files are revised
- Created the first intermediate planning artifact:
  - `int/edits & guides/planning/aw-int_development_plan.md`
- Locked the current project defaults for the intermediate book:
  - rigorous adaptation of the advanced workflow, not full architectural cloning
  - limited JPO contextualization only where it clearly improves realism
  - whole-book planning first, then module-by-module execution
- The saved plan requires the intermediate project to add its own planning, language-instruction, and QA control layers before heavy revision, rather than trying to edit the existing draft set ad hoc
