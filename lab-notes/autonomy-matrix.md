# Autonomy matrix: gh600-sandbox

Risk: Low / Medium / High / Very high. Reversible: Yes / Partly / Hard.

| # | Action | Operational | Security | Compliance | Reversible? | Autonomy | Control |
|---|---|---|---|---|---|---|---|
| 1 | Open draft PR on agent branch | Low | Low | Low | Yes | Autonomous | Branch rules |
| 2 | Edit docs | Low | Low | Low | Yes | Autonomous, reviewed at merge | Required review |
| 3 | Add or change unit tests | Low | Low | Low | Yes | Autonomous, reviewed at merge | Required checks (`test`) |
| 4 | Change application code | Medium | Medium | Low | Yes | Autonomous with review | Required review, `test`, `lint`, CodeQL |
| 5 | Update a dependency | Medium | Medium | Medium | Yes | Autonomous with review | Required checks, scanning |
| 6 | Edit a workflow file | High | High | Medium | Yes | Human owner | CODEOWNERS |
| 7 | Change agent or MCP config | High | High | High | Yes | Human owner | CODEOWNERS, ruleset; MCP setting is admin-only |
| 8 | Add an MCP server | High | High | High | Yes | Human owner | Admin-only setting, allow list policy |
| 9 | Change repository settings or rulesets | High | High | High | Partly | Human only | Admin role, kept to one person |
| 10 | Touch secrets | High | Very high | High | Partly | Human only | Secret scoping, environments |
| 11 | Deploy to production | High | Medium | High | Hard | Explicit authorization | Environment reviewers |
| 12 | Delete a branch or tag | Medium | Low | Medium | Partly | Human owner | Ruleset: restrict deletions |
| 13 | Comment on an issue | Low | Low | Low | Yes | Autonomous | Repository permissions |
| 14 | Merge to main | High | Medium | High | Yes | Human only | Ruleset: the agent can't merge or approve |

## An approval that adds friction without reducing risk
- Which one: a second required approval on documentation-only pull requests.
- Why it does not reduce risk: docs changes are low risk and reverted in under a minute (Lab 2E took 50 seconds);
  a second approver mostly rubber-stamps, and slows every typo fix.
- What replaces it: one normal review at merge, plus an automated check (spelling or link checking) if we want one.
