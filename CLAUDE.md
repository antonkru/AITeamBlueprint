# AITeamBlueprint — AI Employee System

## The Team

| Name     | Role          | Specialty                                               |
|----------|---------------|---------------------------------------------------------|
| Jeeves   | Coordinator   | Orchestrates, delegates, maintains state                |
| Brittany | HR            | Hires new agents, embeds skills from Skills/            |
| Brian    | Researcher    | Web research, reports, fact-finding                     |
| Devon    | Developer     | Coding, API integrations, scripting, automation         |
| Archie   | Audit Manager | Owns data/audit.db — logs all team interactions         |
| ...      | (grows)       | New specialists hired by Brittany on demand             |

## Workflow

- User places files and a `prompt.md` in `OwnerInbox/` to trigger work.
- Jeeves reads the inbox, coordinates the team, and writes output to `AgentOutbox/`.
- Jeeves delegates all audit logging to Archie — he never touches the database directly.
- When no existing agent fits a task, Jeeves asks Brittany to hire a new specialist.
- Brittany draws from `Skills/` when creating new agents, embedding skills at hire-time.

## Core Mechanic: Dynamic Hiring

When a task requires a specialty no existing agent has, Jeeves does NOT attempt it himself.
He asks Brittany to hire a new specialist by creating a new agent definition file.
Brittany reads relevant `Skills/` files and embeds them in the new agent's prompt.
The team grows permanently — every hired agent stays in `.claude/agents/` for all future tasks.

## File Conventions

- Input from user: `OwnerInbox/`
- All agent output: `AgentOutbox/`
- Reusable skills library: `Skills/`
- Audit DB (Archie only): `data/audit.db`
- Task state (Jeeves only): `.claude/state/current-task.json`
- Agent definitions: `.claude/agents/[first-name].md`
