# Permissions audit (2026-11-25)

## Repository defaults
- Default `GITHUB_TOKEN` permissions (Settings > Actions > General): **read**
- Can GitHub Actions create and approve pull requests? **no**
- Do workflows on agent PRs wait for approval? **yes** (Settings > Copilot > Cloud: "Require approval for workflow runs" is on)

## Workflows
| Workflow | permissions | Write scopes | Runner | Environments | Secrets | Change needed |
|---|---|---|---|---|---|---|
| agent-run-with-escalation | explicit | `issues: write` (opens the escalation issue) | ubuntu-latest | - | - | No |
| ci | explicit | none | ubuntu-latest | - | - | No |
| codeql | explicit | `security-events: write` (uploads scan results) | ubuntu-latest | - | - | No |
| deploy | explicit | none | ubuntu-latest | production | - | No |
| drift-check | explicit | none | ubuntu-latest | - | - | No |
| lint | explicit | none | ubuntu-latest | - | - | No |
| multi-agent-pipeline | explicit | none | ubuntu-latest | - | - | No |
| pr-contract-check | explicit | none (`pull-requests: read`) | ubuntu-latest | - | - | No |

## Secrets and variables
| Name | Level (org / repo / environment) | Who or what needs it | Should agents see it? |
|---|---|---|---|
| (none) | repo: no secrets, no variables; production environment: no secrets | - | - |

Self-hosted runners: **0** (GitHub-hosted only).
