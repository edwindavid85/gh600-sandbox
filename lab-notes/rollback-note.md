# Rollback note

| Field | Value |
|---|---|
| Change being rolled back | PR #9 (`agent/docs-update` into `test/rollback`): "docs: clarify quantity units" |
| Why | Rollback drill (Lab 2E): practising the revert path before it's needed for real |
| Detected by (signal, person, alert) | Planned drill; in real life, a reviewer or a failing check |
| Rollback method | GitHub's **Revert** button on the merged PR, which opened revert PR #10 |
| Revert PR | #10, merged into `test/rollback` |
| Time from decision to revert merged | 50 seconds |
| Data or config affected? | No: documentation only |
| Follow-up (root cause, prevention) | None needed for a drill. For real changes: keep agent PRs small so a revert is clean |
| Owner | edwindavid85 |
