# Project Learning

Durable project memory for the active repository root.

Historical note:

- older entries may contain absolute paths from earlier machines or clone locations
- treat those path values as historical snapshots unless an entry explicitly states it is defining the current workspace root

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

### 2026-03-15T00:59:14.7432774+09:00 - Advanced N11 QA Framework Started

- Status: `monitor`
- Scope: project/state
- Context: advanced quality-assurance stage
- Observation: `N11` has now started; the book-wide QA checklist framework was drafted at `adv/edits & guides/aw-adv_n11_qa_checklist.md` and the advanced to-do list now marks `N11` as in progress
- Preferred behavior: use the new `N11` checklist as the authoritative QA framework for the next advanced review pass, rather than relying on the older `N9` QA controls

### 2026-03-15T01:07:00+09:00 - Advanced N11 Round 1 Findings Recorded

- Status: `monitor`
- Scope: project/state
- Context: initial `N11` execution
- Observation: a first `N11` review note now exists at `adv/edits & guides/aw-adv_n11_qa_review_round1.md`; early evidence confirms `P2`, `P6`, and Module 2 Section H ordering in the active `n10` files, while portfolio-task E-word-count handling and final book-level structural-variety confirmation remain active QA items
- Preferred behavior: continue `N11` from the recorded Round 1 findings rather than restarting book-wide checks from scratch

### 2026-03-15T01:12:00+09:00 - Portfolio-Task Units Cleared In N11 Manual Pass

- Status: `monitor`
- Scope: project/state
- Context: follow-up `N11` review on non-standard structures
- Observation: manual review confirmed that Units 14 and 22 state clear `E4` portfolio-task lengths and that Unit 22's non-standard integrated-writing structure is well supported; the earlier uncertainty came from summary-tool limitations rather than from an actual content failure
- Preferred behavior: treat portfolio-task units as manual-review cases in future QA rather than relying on automated summary output alone

### 2026-03-15T01:18:00+09:00 - N10 Support Layer And Structural Variety Confirmed At Book Level

- Status: `monitor`
- Scope: project/state
- Context: broader `N11` review
- Observation: the active `n10` module files now visibly contain a strong spread of explicit teaching markers and a wide activity-type range beyond the original baseline pattern; the remaining open book-level risk is not structural monotony but residual scenario/JPO-option overlap in some interoffice coordination contexts
- Preferred behavior: continue `N11` with a targeted sameness review on scenario families and JPO-option differentiation rather than re-checking whether structural variety exists at all

### 2026-03-15T15:16:24.7226107+09:00 - Key JPO Option Overlaps Repaired In Active N10 Files

- Status: `monitor`
- Scope: project/state
- Context: targeted `N11` sameness pass
- Observation: four genuine JPO homework-option overlaps were confirmed and repaired in Units 4, 6, 13, and 15 of the active `n10` files; the revised prompts now remain skill-parallel while using more distinct professional contexts
- Preferred behavior: treat the remaining sameness risk as a lighter book-level monitoring task rather than as a known unresolved defect in those four units

### 2026-03-15T19:32:00+09:00 - N11 Now Explicitly Tests Prompt Readability And Scenario-Family Distribution

- Status: `monitor`
- Scope: project/conventions
- Context: checklist tightening during `N11`
- Observation: `adv/edits & guides/aw-adv_n11_qa_checklist.md` now explicitly tests whether prompt wording remains readable for B1+/B2 aspirational learners, whether revised prompts drift upward in linguistic sophistication or processing load, and whether scenario families are distributed broadly enough across the book; each new check is tied to named source documents
- Preferred behavior: treat learner-level prompt readability and book-level scenario-family spread as explicit `N11` sign-off criteria, not as optional style preferences

### 2026-03-15T19:32:00+09:00 - Modules 2 And 4 Still Carry A Narrow JPO Scenario Band

- Status: `workaround`
- Scope: project/state
- Context: `N11` Round 2 focused pass
- Observation: even after the earlier overlap repairs, some active JPO prompts in Modules 2 and 4 remain too dense and too clustered around trilateral or counterpart-office coordination, especially in Units 4, 6, 13, and 15
- Preferred behavior: before treating those modules as clear under `N11`, run one more targeted prompt pass that shortens the affected JPO options and broadens their professional context range

### 2026-03-15T19:32:00+09:00 - Full N11 Round 2 Pass Reframed The Remaining Blockers

- Status: `monitor`
- Scope: project/state
- Context: full-book pass against the revised `N11` checklist
- Observation: the full Round 2 pass confirmed that the main live blockers are now limited to two areas: structural / activity-labelling inconsistency in Modules 1 and 3, and over-dense / over-clustered JPO scenario families in Modules 2 and 4; Modules 5 and 6 are broadly clear under the revised QA standard
- Preferred behavior: treat `aw-adv_n11_qa_review_round2.md` as the operative N11 record and use it to drive the next correction pass, rather than relying on the earlier partial Round 1 / selective Round 2 notes

### 2026-03-15T20:05:00+09:00 - Round 3 Replaces Round 2 As The Operative N11 Record

- Status: `monitor`
- Scope: project/state
- Context: external checklist verification and Round 3 QA pass
- Observation: `adv/edits & guides/aw-adv_n11_qa_review_round3.md` is now the operative `N11` record. It corrects two Round 2 distortions: Module 3 was overstated as a wider structural blocker, and Module 6 was understated because Unit 20 structural defects were not carried into the operative summary. The live blocker set is now: H1/profile decision in Units 2, 3, 4, 6, and 11; Module 1 structural cleanup; Modules 2 and 4 JPO prompt simplification and de-clustering; and Unit 20 structural cleanup.
- Preferred behavior: use Round 3, not Round 2, as the current sign-off baseline for `N11`, and treat earlier round files as historical supporting records

### 2026-03-15T20:05:00+09:00 - Claude v2 Checklist Upgrades Are Now Part Of The Main N11 Standard

- Status: `monitor`
- Scope: project/conventions
- Context: checklist verification against external feedback
- Observation: `adv/edits & guides/aw-adv_n11_qa_checklist.md` now includes the stronger v2 controls validated through Claude feedback: preliminary cross-check against earlier review files, explicit H1 structural compliance, explicit word-count progression, activity-heading / sub-labelling checks, requirement sources for workplace relevance, and named deferral of the learning-goals mapping issues
- Preferred behavior: treat the main `aw-adv_n11_qa_checklist.md` file as the single operative checklist and do not rely on the looser earlier Round 2 standard

### 2026-03-16T02:05:00+09:00 - Round 3 Source Fixes Preserve The Existing Section-H House Standard

- Status: `monitor`
- Scope: project/conventions
- Context: implementation of the Round 3 correction set
- Observation: the H1 decision was applied to the affected units, but the implementation deliberately preserved the repo's established Section H order (`H2 → H3 → H1` where relevant) rather than importing the alternate ordering proposed in Claude's Step 19 note; Module 1 structural cleanup, Module 2/4 JPO prompt diversification, and Unit 20 structural cleanup were applied in the same correction pass
- Preferred behavior: treat the repo's existing H-ordering convention as authoritative unless a future project decision explicitly replaces it

### 2026-03-16T09:28:49.3778502+09:00 - H1 Is Now A Book-Wide Feature In The Active Advanced Baseline

- Status: `monitor`
- Scope: project/decision
- Context: post-Round-3 follow-through on the accepted H1 policy
- Observation: the active advanced baseline now treats H1 Extension Task as a consistent book-wide feature, including Unit 18 and Units 20-23, while preserving the established Section H order (`H2 → H3 → H1` where H2 is present, otherwise `H3 → H1`)
- Preferred behavior: future QA and editing passes should assess H1 as a book-wide requirement and should not treat the old six-unit mismatch set as the governing scope any longer

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

### 2026-03-16T11:07:11.6171964+09:00 - Memory Paths Must Be Portable Across Machines

- Status: `monitor`
- Scope: project/workflow
- Context: first startup on a different Windows profile and repo location
- Observation: hardcoded references to `C:\Users\daved\...` and `C:\Dev\Code\book_administrative-writing` do not hold on every machine; this work PC uses `C:\Users\d-dobson` and a UNC workspace path
- Preferred behavior: resolve repo-local memory files from the active repository root and resolve user-level Codex files from `%USERPROFILE%\.codex` unless `CODEX_HOME` is explicitly changed

### 2026-03-16T11:07:11.6171964+09:00 - Work PC Git Access Depends On User PATH And PowerShell Policy

- Status: `monitor`
- Scope: project/tooling
- Context: first Codex startup on this work PC
- Observation: Git for Windows is installed under `%LOCALAPPDATA%\Programs\Git`, but Codex shell sessions on this machine may not resolve `git` unless the user `Path` includes `...\Git\cmd` and PowerShell can load the current-user profile
- Preferred behavior: keep `C:\Users\d-dobson\AppData\Local\Programs\Git\cmd` on the user `Path`; if PowerShell-hosted sessions lose `git`, verify `CurrentUser` execution policy still allows the profile fallback

### 2026-03-16T11:46:18.7935300+09:00 - User-Level AGENTS Must Carry The Memory Bootstrap Workflow

- Status: `monitor`
- Scope: project/workflow
- Context: review of whether the work-PC local bootstrap was sufficient
- Observation: a minimal user-level `AGENTS.md` is not enough for cross-device consistency; the user-level file must itself carry the startup-read order, startup audit, mirror-sync, and project-logging rules so a new machine can bootstrap local and project memory consistently before any repo-specific repair
- Preferred behavior: keep the full memory-bootstrap workflow in `%USERPROFILE%\.codex\AGENTS.md` and ensure it stays aligned with the repo-level memory workflow rather than relying on a thin placeholder

### 2026-03-16T11:55:43.6239833+09:00 - Memory Instructions Must Explicitly Require File Creation And Sync Targets

- Status: `monitor`
- Scope: project/workflow
- Context: follow-up review of the bootstrap instructions
- Observation: describing compare/sync behavior is not sufficient by itself; the instructions must explicitly require creating missing user-memory, project-memory, and read-log files, and must state exactly which categories of information sync to which files
- Preferred behavior: keep both the repo-level and user-level `AGENTS.md` files explicit about creating missing files immediately and about separating cross-project lessons, project facts, project chronology, and CSV read audits into their correct destinations

### 2026-03-16T12:06:28.8563703+09:00 - The Shared Bootstrap Also Requires A Repo-Level AGENTS Clone

- Status: `superseded`
- Scope: project/workflow
- Context: follow-up correction to the explicit bootstrap rules
- Observation: creating the companion memory files is still insufficient if a fresh clone has no repo-level `AGENTS.md`; the shared bootstrap workflow itself must be duplicated between the canonical user-level `AGENTS.md` and the repo-level `AGENTS.md`, with the repo copy adapted to the active repository root
- Preferred behavior: superseded by the later versioned shared-spec model; direct copy is now for missing-file bootstrap only, while existing paired `AGENTS.md` files follow versioned merge rules

### 2026-03-16T12:08:01.0802098+09:00 - AGENTS Clones Must Be Fully Aligned

- Status: `superseded`
- Scope: project/workflow
- Context: clarification of the duplication rule for user-level and repo-level instruction files
- Observation: saying the files should align only in shared sections leaves too much room for drift; the duplicated `AGENTS.md` files must be treated as fully aligned clones, with only deterministic repo-root path substitution and explicit project-specific additions allowed to differ
- Preferred behavior: superseded by the later shared-spec rule; the live requirement is now identical duplicated content after bootstrap or merge, not “aligned with allowed differences”

### 2026-03-16T13:36:04.9560756+09:00 - AGENTS Now Uses A Shared Versioned Bootstrap Spec

- Status: `monitor`
- Scope: project/workflow
- Context: full audit follow-through on reproducibility and sync behavior
- Observation: the previous clone-and-align wording was still too loose and still contradicted the desired bootstrap behavior. The operative design is now a shared versioned bootstrap spec that is duplicated between `%USERPROFILE%\.codex\AGENTS.md` and `<repo-root>\AGENTS.md`
- Preferred behavior: keep the duplicated `AGENTS.md` files text-identical, use direct file copy only when one side is missing, and use versioned two-way merge rules when both sides exist

### 2026-03-16T13:36:04.9560756+09:00 - Repo Memory Files Are Git-Managed Rather Than Duplicated

- Status: `monitor`
- Scope: project/workflow
- Context: audit clarification on which files need Codex-level sync logic
- Observation: `project-learning.md`, `project-journal.md`, and `instruction-read-log.csv` propagate across devices through Git and do not need a second duplication protocol. `user-learning-mirror.md` remains special because it is both repo-tracked and a semantic mirror of local user memory
- Preferred behavior: reserve Codex-level copy and merge rules for `AGENTS.md` and user-learning mirror sync, while treating the project memory files as Git-managed repo artifacts with content-usage rules only

### 2026-03-16T13:39:46.8020732+09:00 - Versioned AGENTS Merge Requires Reading Both Copies

- Status: `monitor`
- Scope: project/workflow
- Context: self-audit of the rewritten shared bootstrap spec
- Observation: the first rewrite correctly unified the two live `AGENTS.md` files, but it weakened startup handling by naming only one active `AGENTS.md` copy in the read order and by leaving the version token in a less strict markdown form
- Preferred behavior: read both `%USERPROFILE%\.codex\AGENTS.md` and `<repo-root>\AGENTS.md` whenever they exist before deciding merge behavior, keep `Bootstrap-Version` as a strict plain-text field, and mark the earlier clone/alignment entries as superseded

### 2026-03-16T13:39:46.8020732+09:00 - Bootstrap Version Uses Full Timestamp Granularity

- Status: `monitor`
- Scope: project/workflow
- Context: follow-up refinement of the shared `AGENTS.md` version field
- Observation: date-only or coarse same-day versioning is insufficient because the bootstrap instructions can change multiple times on the same day across different machines
- Preferred behavior: keep `Bootstrap-Version` in full timestamp form with timezone offset so version comparisons remain unambiguous and consistent with the timestamp style already used in the memory files
