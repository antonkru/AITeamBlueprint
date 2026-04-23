# AITeamBlueprint — Overview

**AITeamBlueprint** is a ready-made AI agent team built for small business owners, running on top of Claude Code's native multi-agent architecture.

---

## What It Is

A permanent team of specialised AI agents, each with a defined role and narrow scope. Instead of one AI trying to do everything, tasks are routed to the right specialist — a researcher, a copywriter, a developer, a legal reviewer, etc.

---

## How It Works

- You drop a plain-text `.md` request into `work/OwnerInbox/`
- **Jeeves** reads it, delegates to the right specialist(s), and delivers finished work to `work/AgentOutbox/`
- Every task and delegation is logged to a SQLite audit database by **Archie**
- If no existing agent can handle a request, **Brittany** hires a new specialist automatically — and they stay on the team permanently

---

## Two Ways to Submit Work

| | Inbox file | Direct prompt |
|---|---|---|
| Audit trail | Full | None |
| Resumable | Yes | No |
| Output | `AgentOutbox/` folder | Chat only |
| Queue support | Yes | No |
| Reference files | Yes | No |
| Formal task record | Yes | No |

Use **inbox files** for work you want delivered and tracked. Use **direct prompts** for quick questions and team management.

---

## What Makes It Distinctive

- **No code required** — everything is plain Markdown: agent definitions, skill modules, task prompts, and coordinator logic
- **Self-expanding team** — Brittany hires new specialists automatically from the Skills Library when a task has no existing owner; each hire is permanent
- **MCP service access** — agents that need live connections (Gmail, Google Calendar) run inline in Jeeves's session with full MCP tool access
- **Full audit trail** — Archie logs every task, delegation, and output to a local SQLite database; browsable via `dashboard/index.html`

---

## Current Team (as of 2026-04-23)

| Name | Role |
|------|------|
| Jeeves | Coordinator & orchestrator |
| Archie | Audit manager |
| Brittany | HR specialist — hires new agents |
| Brian | Researcher |
| Claire | Marketing copywriter |
| Gavin | Email triage (Gmail MCP) |
| Iris | Image generator (Gemini MCP) |
| Lexie | Legal reviewer |
| Maya | Video script writer |
| Nora | Calendar manager (Google Calendar MCP) |

---

## File Layout

```
work/
  OwnerInbox/          ← Drop prompt files here
    done/              ← Processed prompts archived here
  AgentOutbox/         ← Finished work lands here
    [id]-[slug]-[date]/

.claude/
  agents/              ← One .md file per team member
  skills/              ← Reusable skill modules for new hires
  state/               ← Current task state (managed by Jeeves)

data/
  audit.db             ← Full task and action log (managed by Archie)
```
