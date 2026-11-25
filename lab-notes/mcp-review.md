# Lab 2B: MCP configuration review

## 1. What is configured today
- Where I looked: Settings > Copilot > MCP servers (repository settings)
- MCP servers configured for this repository: none (`{"mcpServers": {}}`)
- The setting applies to Copilot in the cloud and Copilot code review only.
  IDEs and Copilot CLI use their own MCP configuration.
- GitHub MCP server: enabled by default, **read-only**, confirmed in GitHub Docs
  ("Configure MCP servers for your repository")
- Token scope: a specially scoped token with read-only access to **the current repository** only

## 2. Vocabulary check
| Term | My one-line definition |
|---|---|
| MCP server | Provides tools (and resources) to an agent over the Model Context Protocol |
| MCP registry | A catalogue that lists servers people can discover and install |
| Allow list | The policy that says which servers or tools are permitted |

## 3. Example server definition I reviewed
```json
{
  "mcpServers": {
    "example-server": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@example/mcp-server"],
      "tools": ["search_docs", "get_page"],
      "env": { "EXAMPLE_TOKEN": "${{ secrets.COPILOT_MCP_EXAMPLE_TOKEN }}" }
    }
  }
}
```
- Why an explicit `tools` list beats `["*"]`: the agent uses MCP tools autonomously without asking,
  so only allow the specific (ideally read-only) tools the task needs. A star also silently grants any
  tool the server adds later.
- Where the secret value really lives: an Agents secret in the repository whose name starts with
  `COPILOT_MCP_`. Only those are passed to the MCP configuration.

## 4. Who can change it
- MCP configuration is a repository **setting**, not a file, so CODEOWNERS can't protect it:
  only repository admins can change it. Keep the admin list short.
- Paths now covered by CODEOWNERS: `.github/agents/`, `.github/copilot-instructions.md`,
  `.github/workflows/` (includes `copilot-setup-steps.yml`), `.vscode/mcp.json`, `.github/CODEOWNERS`
- Who blocks an unapproved MCP server: repo admins (repository setting), code owners (config files),
  org or enterprise owners (Copilot policies, MCP registry and allow list)

## 5. Exam notes
- Server provides tools; registry lists what is available; allow list decides what is permitted.
- The firewall (Settings > Copilot > Internet access) is on by default with the recommended allowlist.
  It limits the agent's own processes; it does not cover MCP servers or setup steps.
