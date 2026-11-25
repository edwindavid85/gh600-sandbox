# Evaluation spec: agent tasks on gh600-sandbox

## Expected outcome
Each task ends as a draft PR that does exactly what the task asks, passes CI, and a reviewer
would merge without asking for rework.

## Constraints
- Only files listed in the task may change (drift check passes).
- No tests deleted or skipped; no lint or scanning rules suppressed.
- No new dependencies unless the task says so.

## Signals
| Signal | Type | How it is measured | Pass threshold |
|---|---|---|---|
| Tests pass | Quantitative | CI `test` job | All green |
| Scan and lint alerts | Quantitative | `lint` job and code scanning | 0 new alerts |
| Retries / re-prompts needed | Quantitative | Count follow-up prompts or retries | <= 1 |
| Reviewer verdict | Qualitative | Would you merge as is? (yes / minor edits / no) | yes or minor edits |
| Convention fit | Qualitative | Follows `.github/copilot-instructions.md` | yes |

## Tasks (each checkable)
| ID | Task | Check |
|---|---|---|
| T1 | `restock` raises `KeyError` with a clear message for unknown SKUs; add a test | New test passes; old tests pass |
| T2 | Add `Inventory.search(text)` returning SKUs whose name contains text (case-insensitive) | Test for 2 matches and 0 matches |
| T3 | Add a "Low stock" section to `docs/usage.md` | Doc mentions `low_stock` and its default threshold of 5 |
| T4 | Add `Inventory.value_of(sku)` returning quantity x unit price for one item | Test for a known item and an unknown SKU |
| T5 | Add a CHANGELOG entry for the last merged PR | Entry under "Unreleased" with PR number |
