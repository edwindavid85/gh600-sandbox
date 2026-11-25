# Agent run postmortem

| Field | Value |
|---|---|
| Run / PR | PR #17 "Log restocks", CI run 45555047823 (failed) |
| Date | 2026-11-25 |
| Task (link to contract) | lab-notes/pr-3C-restock.md: log restocks, following `.github/copilot-instructions.md` |

## What happened
Following the repository instructions, the change imported `log_event` from `app.logging_utils`.
That helper had been renamed to `record_event` in PR #16, but the instructions still named `log_event`.
Test collection failed with `ImportError: cannot import name 'log_event'`, so no tests ran and CI failed.

## Evidence
- Session log: n/a (followed the instructions by hand, as an agent would)
- Plan (as approved): PR #17 description: change `app/inventory.py` only
- Commits / diff: 2ad9d73 adds `log_event("restock", ...)` and imports `log_event`
- Checks and scan results: run 45555047823, step "Run python -m pytest -q": ImportError
- Workflow artifacts or firewall warnings: none
- Supporting: PR #16 renamed the helper; `.github/copilot-instructions.md` line 14 still said `log_event()`

## Root cause class
- [ ] Reasoning error (flawed plan, misread requirement)
- [ ] Tool misuse (bad call, out-of-scope action, missing or excess tool)
- [x] Context or environment (stale memory, missing dependency or secret, firewall block)

Why this class, citing the evidence above: the plan and the code were a correct application of the
instructions. The instruction itself was out of date after PR #16, so the context was stale.

## Fix and layer changed
| Layer | Change |
|---|---|
| Instructions / task contract | Instruction now names `record_event()`; Last reviewed date updated (PR #17, c453f24) |
| Tools / permissions | None needed |
| Memory / setup / environment | PR template checkbox: convention changes update instructions in the same PR |

## How we will know it worked
- Re-run the task 3 times from main; target pass rate 3/3 (baseline 0/1). First re-run: run 45555124345 passed.
