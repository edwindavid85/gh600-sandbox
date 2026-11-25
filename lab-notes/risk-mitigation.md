# Cloud agent: risks and mitigations (in my own words)

Source: GitHub Docs, "Risks and mitigations for GitHub Copilot cloud agent"
(docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations, read 2026-11-25).
Note: the page has moved since the course pack was written; trust the current docs.

| Risk | Built-in mitigation | What I add in my repo | How I would verify it |
|---|---|---|---|
| Unvalidated code introduces vulnerabilities | Checks its own code (CodeQL, dependency advisories, secret scanning) and gets a Copilot code review "second opinion"; no GHAS licence needed | Independent CI: `lint`, `codeql`, a CodeQL rule in the ruleset | Lab 4C: lint caught weak code that CodeQL and tests missed |
| The agent pushes code | Only write-access users can trigger it; one branch; simple pushes only; draft PRs it can't mark ready, approve or merge; requester can't approve; workflows wait for approval | `protect-main` ruleset: PR, code owners, required checks | Lab 1B: merge blocked; Lab 6B: agent-config PR blocked |
| Access to sensitive information | Internet access restricted by the firewall | No secrets in the repo; firewall and recommended allowlist kept on | Lab 6D: 0 secrets; Lab 2B: firewall settings on |
| Prompt injection | Hidden characters filtered; HTML comments in issues and PR comments are not passed to the agent | Least privilege; review before merge; CODEOWNERS | Lab 6C (agent batch): hidden-instruction canary |
| Loss of visibility | Commits authored by Copilot and co-authored by the requester; signed ("Verified"); session logs and audit log; commit messages link to session logs | Plans, hand-offs and decisions written to PRs | Lab 5C: timeline rebuilt from GitHub alone |
| Automations run without a person | Clear attribution; extra review for shared automations; you choose the tools and the resources an automation can update | Keep automations' tools minimal; review their PRs like anyone's | When automations are enabled: check attribution on their PRs |
