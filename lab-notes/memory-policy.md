# Memory policy for gh600-sandbox

## What I found (path B: Copilot Memory isn't available on this account's plan)
- Personal Copilot settings (Copilot Free): no Copilot Memory setting to enable.
- Repository: Settings > Copilot > **Dreaming (Preview)**. It improves the memories and guidance Copilot
  uses. Memory changes are applied **automatically, without a pull request**; changes to skills and
  custom instructions are **proposed as pull requests** for review. Only repository admins can change it.

## Scope
| Memory type | Where it lives | Who can create it | Who can see or use it |
|---|---|---|---|
| Short-term (session context) | The agent's current session | The session | That session only |
| Long-term: repository facts | Copilot Memory (if enabled) | Users with write access who have Memory enabled | Agents working in this repository |
| Long-term: user preferences | Copilot Memory, user level | Me | Me |
| External / durable | Files and artifacts in GitHub (instructions, state files, PRs, issues) | Contributors via PR | Everyone with repo access |

## Rules
1. The repository is the authority. A remembered fact is verified against the current branch before it is relied on.
2. Facts must cite the code that supports them; a fact without a citation is not trusted.
3. Review stored repository memories every 30 days; delete stale or wrong ones.
4. After a convention changes, update `.github/copilot-instructions.md` in the same PR and prune any memory
   that contradicts it (the Lab 3C failure is the example: `log_event` was renamed to `record_event`).
5. Reset: if memory is causing repeated wrong behaviour, delete it and rely on repository files until it is rebuilt.
6. Dreaming stays off until we decide who reviews memory changes that don't go through a PR.

## Review log
| Date | Memories reviewed | Deleted | Why |
|---|---|---|---|
| 2026-11-25 | 0 (Memory not available on Copilot Free) | 0 | Reviewed `.github/copilot-instructions.md` instead: fixed the stale `log_event` rule in Lab 3C |
