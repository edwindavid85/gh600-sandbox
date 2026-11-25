# Reconstructed timeline (Lab 5C)

Rule: use only GitHub evidence (PRs, comments, commits, checks, workflow artifacts, issues).
No memory, no chat history.

| Time (UTC) | Actor (human / agent) | Action | Decision made? | Evidence link |
|---|---|---|---|---|
| 05:56 | pipeline (docs job) | docs: success | No | run 45556963208 |
| 05:56 | pipeline (implement job) | implement: cancelled | No | run 45556963208 |
| 05:56 | pipeline (plan job) | plan: success | Yes: scope split | run 45556963208 |
| 05:57 | pipeline (merge-check job) | merge-check: failure | Escalate (fan-in failed) | run 45556963208 |
| 05:58 | agent/quiet-alerts | Opened PR #25: threshold 5 -> 3 | Proposal | PR #25 |
| 05:58 | agent/restock-alerts | Opened PR #24: threshold 5 -> 10 | Proposal | PR #24 |
| 05:58 | edwindavid85 | Merged PR #24 (admin bypass) | Yes, but no reason recorded | PR #24 timeline |
| 05:59 | edwindavid85 | Comment D2: threshold stays 5 | Yes, with reason | PR #25 comment |
| 05:59 | edwindavid85 | Merged PR #25 (resolution) | Applies D2 | PR #25 timeline |

## Gaps found
| Gap | Why it matters | Fix to the workflow |
|---|---|---|
| PR #24 was merged with no recorded reason | Can't tell if merging it first was deliberate | Merges of agent PRs need a comment saying why |
| The plan artifact doesn't say who started the run, or on which commit | Accountability | Coordinator writes actor and SHA into plan.md |
| Artifacts expire after the default retention period | The evidence disappears | Set retention-days explicitly, export for audits |
| Placeholder workers leave no reasoning | Can't explain their outputs | Every worker must write a hand-off note |
