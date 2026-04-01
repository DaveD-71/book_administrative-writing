# Transfer-Readiness Audit
## *Administrative Writing, Advanced* — Planning Guide Set

---

> **Purpose of this document**
> This audit evaluates whether the current advanced planning system can be transferred and reused to develop the intermediate book.
>
> It does **not** assume that the recent planning-folder consolidation was neutral. It distinguishes:
> - core document roles
> - reusable system components
> - advanced-specific instances
> - current drift introduced during consolidation

---

## Findings

### 1. The current `guide-set` structure is the right architectural direction and is now substantially cleaner after drift cleanup

**Severity:** `Monitor`

**Why this matters:**
- The folder split into `guide-set` and `supporting` is useful and portable.
- Earlier in the consolidation, historical and stage-artifact documents outside the active planning layer were also updated to follow the new paths.
- That spillover has now been reduced so the surviving content diff is focused on the moved current planning files and the project-memory references that describe them.

**Current impact:**
- The structure is promising for future intermediate development.
- The repo state is now much closer to a low-drift reference implementation of that structure than it was during the first audit pass.

**Examples of spillover edits:**
- `adv/archive/edits & guides/n10/aw-adv_n10_language_instruction_framework.md`
- `adv/archive/edits & guides/n10/aw-adv_n10_language_instruction_plan.md`
- `adv/archive/edits & guides/n11/aw-adv_n11_qa_checklist_v2_claude.md`
- `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round2.md`
- `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
- `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round4.md`
- `adv/archive/edits & guides/steps/aw-adv_step19_h1_codex_prompts.md`
- `adv/archive/old/aw-adv_project_todo_list.md`

**Audit judgment:**
- Keep the architectural split.
- The remaining work is no longer drift cleanup; it is template extraction and intermediate adaptation.

---

### 2. No major loss was found in the main authoritative planning documents, and the supporting-file reframing has been undone

**Severity:** `Resolved`

**Why this matters:**
- The core authoritative documents appear to have survived the move without obvious substantive loss.
- During the first consolidation pass, two supporting files were changed in purpose wording rather than merely relocated.

**Affected files:**
- `adv/edits & guides/planning/supporting/aw-adv_intro.md`
- `adv/edits & guides/planning/supporting/aw-adv_project_context.md`

**What changed:**
- Both files temporarily contained new framing text defining them as background/supporting rather than active authority.
- That wording has now been removed so the files remain moved documents rather than silently repurposed rewritten ones.

**Audit judgment:**
- Treat these as relocated supporting documents whose role is now defined by the guide-set structure rather than by rewritten internal framing.

---

### 3. The current planning area already contains the core components of a transferable development system

**Severity:** `Pass with follow-up`

**Why this matters:**
- The project now has a clearer separation of planning functions than before.
- That separation is exactly what a reusable intermediate-development system needs.

**The transferable pattern is:**
1. one guide/index file that defines the active planning bundle
2. one project-state control file
3. one activity-definition source
4. one prompt/task policy
5. one structural planning table
6. one QA stage-definition file
7. one full-review stage-definition file
8. one supporting/background layer outside the active authority set

**Audit judgment:**
- This pattern should be reused for the intermediate track.
- The content inside several of these files still needs classification before reuse.

---

## File Classification

| File | Current function | Transfer class | Notes |
|---|---|---|---|
| `aw-adv_development_guide.md` | Defines the active planning bundle and how to use it | `Reusable template pattern` | Keep the role and structure; create an intermediate equivalent with intermediate-specific file references. |
| `aw-adv_project_todo_list.md` | Tracks advanced project stage, sequencing, and current state | `Advanced-specific instance` | Intermediate needs its own control file, not a copy with find/replace only. |
| `aw-master_activity_menu.md` | Defines activity families and intended pedagogical roles | `Series-level reusable source` | This is the strongest candidate for reuse across levels, though examples may need level calibration. |
| `aw-adv_prompt-writing-policy.md` | Defines prompt/task design rules | `Reusable framework with advanced-specific calibration` | The policy structure is reusable; some examples and calibration assumptions should be adapted for intermediate. |
| `aw-adv_unit_structural_profiles_revised.md` | Master unit plan and cross-check table for the advanced book | `Advanced-specific instance` | Intermediate needs its own structural profiles, not a modified copy of the advanced table. |
| `aw-adv_n11_qa_checklist.md` | Defines the advanced post-`N10` QA gate | `Reusable stage template with advanced-specific references` | The checklist architecture is reusable; file paths, criteria wording, and stage names may need adaptation. |
| `aw-adv_full-review_protocol.md` | Defines the post-`N11` whole-book editorial review stage | `Reusable stage template with advanced-specific references` | Strong candidate for reuse once the stage labels and source hierarchy are parameterized. |
| `aw-adv_intro.md` | Front-matter content that informs development | `Supporting only` | Not part of the reusable control system. |
| `aw-adv_project_context.md` | Historical/context orientation | `Supporting only` | Useful background, not part of the core transferable control bundle. |

---

## Recommended Reusable System For Intermediate

The intermediate track should inherit the **structure**, not the advanced content.

The clean transferable system should be:

1. `guide-set/`
   - one development-guide index
   - one project to-do / control file
   - one activity menu
   - one prompt-writing policy
   - one unit structural profile file
   - one QA checklist
   - one full-review protocol

2. `supporting/`
   - background/context material only

3. stage artifact folders outside planning
   - revision-stage outputs
   - QA round notes
   - full-review findings

This means the intermediate book should mirror the **document-role system** while receiving its own:
- project state
- unit profiles
- stage artifacts
- learner-level calibration choices

---

## What Must Happen Before This Is A Clean Transfer Model

1. Treat `aw-master_activity_menu.md`, `aw-adv_prompt-writing-policy.md`, `aw-adv_n11_qa_checklist.md`, and `aw-adv_full-review_protocol.md` as the main candidates for template extraction.
2. Treat `aw-adv_project_todo_list.md` and `aw-adv_unit_structural_profiles_revised.md` as advanced instances that should inform, but not directly become, the intermediate equivalents.
3. When the intermediate system is created, adapt content by role rather than by bulk copy.

---

## Current Conclusion

The advanced planning area now contains the **right system shape** for reuse and is now a substantially cleaner reference implementation than it was before the drift cleanup.

The main positive outcome is:
- a clearer separation between active planning authority and supporting material

The main caution is:
- the structure is ready to reuse, but several documents still need deliberate template extraction because they remain advanced-specific in content even though the architecture is transferable

---

*Audit status: transfer-readiness classification completed and updated after consolidation drift cleanup.*
