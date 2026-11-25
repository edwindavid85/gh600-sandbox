# Conflict policy for agents in gh600-sandbox

## Prevention
- Each agent gets a distinct scope (paths) written in the coordinator's plan.
- One branch per agent: `agent/<agent-name>/<task>`.
- Concurrency groups stop two runs of the same pipeline on the same ref.

## Conflict types
| Type | Example | Default resolution |
|---|---|---|
| Overlapping changes | Two agents edit the same lines of `app/inventory.py` | First merged wins; the other rebases and re-runs its checks |
| Duplicated effort | Two agents both add the same test | Coordinator closes the later PR and links the kept one |
| Contradictory outputs | Reviewer agent says "reject", critic says "approve" | Tie-break below |

## Tie-break (in order)
1. The coordinator's written plan decides scope questions.
2. The CODEOWNERS owner of the contested path decides content questions.
3. If still unresolved, the human task owner decides and records the decision and evidence in the PR.

## Drill record (Lab 5B)
- Branches: agent/restock-alerts (#24, threshold 10) and agent/quiet-alerts (#25, threshold 3)
- Conflict type: overlapping changes (same line) AND contradictory outputs (10 versus 3)
- How it was resolved: #24 merged first; #25 conflicted. No plan owned the setting, so the code owner decided (D2): keep the documented default of 5. Decision and reason recorded as a comment on #25.
- Rule added (CODEOWNERS line): /app/inventory.py @edwindavid85
