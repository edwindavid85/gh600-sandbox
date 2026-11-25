# Lab 1A: Task contracts

For each task fill in every field. A task an agent should take on has a clear goal,
checkable success criteria, a bounded scope and a cheap rollback.

---

## Task 1: Add input validation to `Inventory.restock`

| Field | Value |
|---|---|
| Goal | `restock` rejects unknown SKUs with a clear `KeyError` message |
| Inputs | Issue text, `app/inventory.py`, `tests/test_inventory.py` |
| Outputs | Draft PR with code change and a new unit test |
| Success criteria | New test fails before and passes after; all CI checks green; no new lint or scanning alerts |
| Boundaries | May edit `app/inventory.py` and `tests/` only. No dependency changes. |
| Owner | edwindavid85 reviews and merges |
| Rollback | Revert the PR; no data or config involved |
| Suits an agent? | **Yes**: small, well specified, verified by tests, reversible |

---

## Task 2: "Make the inventory service better"

As written: **not suitable**. Anti-patterns: *vague mandate* (no goal anyone can check) and
*unbounded scope* (nothing says what may change). Rewritten as a contract an agent can meet:

### Task 2a: Add `Inventory.search(text)`

| Field | Value |
|---|---|
| Goal | `search(text)` returns the SKUs whose item name contains `text`, case-insensitive, sorted |
| Inputs | This contract, `app/inventory.py`, `tests/test_inventory.py` |
| Outputs | Draft PR: the method with a docstring, plus tests |
| Success criteria | Tests for two matches, zero matches and mixed case pass; existing 5 tests still pass; CI green; no new alerts |
| Boundaries | Edit `app/inventory.py` and `tests/test_inventory.py` only. No new dependencies. |
| Owner | edwindavid85 |
| Rollback | Revert the PR |
| Suits an agent? | **Yes** |

---

## Task 3: Rotate the production database password

| Field | Value |
|---|---|
| Goal | Replace the production database password and update every consumer |
| Inputs | Access to the secret store, list of services that use the credential |
| Outputs | New credential in the secret store; services restarted; old credential revoked |
| Success criteria | All services healthy on the new credential; old credential rejected; change logged |
| Boundaries | Production secrets only; change window agreed with the service owner |
| Owner | The on-call database owner (a person) |
| Rollback | Partly possible: re-enable the old credential within the grace period; a leaked secret can't be "un-leaked" |
| Suits an agent? | **No**. Touches secrets, hard to reverse, compliance-sensitive. Human only. |

---

## Anti-patterns I can now name

| Anti-pattern | What it looks like | Mitigation |
|---|---|---|
| Vague mandate | "Make the inventory service better" (Task 2 as written) | Task contract with a goal and checkable success criteria |
| Plan and act in one step | An agent edits files the moment an issue is assigned | Plan section, validated and approved before action |
| Unbounded scope | No list of files the agent may touch | Boundaries plus a drift check against the plan |
| Hidden state in chat | "We agreed to skip the tests" exists only in a chat window | Write plan, decisions and progress to the PR or an issue |
| Approval on everything | Two reviewers required for a one-word docs fix | Set autonomy by risk; gate only meaningful risk |
