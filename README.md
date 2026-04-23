# AITeamBlueprint

A ready-made AI agent team for small business owners. Drop a request into an inbox folder — a coordinator named Jeeves reads it, delegates to the right specialists, and delivers finished work to an output folder. If the team lacks a skill, it hires a new specialist automatically.

---

## How It Works

AITeamBlueprint is built on top of **Claude Code's native multi-agent architecture**. Rather than a single AI trying to do everything, the system runs a permanent team of specialised agents — each with a defined role, a curated skill set, and clear boundaries on what it owns.

### The Coordinator Pattern

At the centre is **Jeeves**, a coordinator agent that runs as the top-level Claude Code session. He owns the inbox, manages task state, and decides which specialist to delegate each piece of work to. He never does domain work himself — he routes, tracks, and synthesises.

When Jeeves delegates a task he spawns a **subagent** — a fresh Claude session scoped to that specialist's role, tools, and prompt. Each subagent runs in isolation, returns its output, and exits. This keeps context clean and prevents one agent's work from polluting another's.

### Specialisation Over Generalisation

Every agent is defined by a Markdown file in `.claude/agents/`. That file acts as a system prompt, tightly scoping what the agent knows, what tools it has access to, and what format its output must take. Brian only researches. Claire only writes copy. Devon only writes code. Narrow scope means higher quality per agent and no prompt drift between tasks.

### Dynamic Hiring

The team is not static. When Jeeves encounters a task that no existing agent can handle, he asks **Brittany** — the HR agent — to create a new specialist on the spot. Brittany reads the relevant skill modules from `.claude/skills/` and assembles a new agent definition. That agent is immediately available and stays on the team permanently, so the system grows smarter with every novel request.

### MCP Tool Access

Some agents need access to connected services — Gmail, Google Calendar, Google Drive. Claude Code's **Model Context Protocol (MCP)** layer makes these tools available to the top-level session. Agents that require MCP tools (like the email triage agent Gavin) run inline inside Jeeves's session rather than as isolated subagents, giving them the same live service connections without requiring credentials to be re-established.

### Audit Trail

Every task open, delegation, and completion is logged to a local SQLite database by **Archie**, the audit agent. No other agent touches the database directly. This gives you a permanent, queryable record of everything the team did and when. Open `dashboard/index.html` in a browser to explore the audit trail visually — see the [Dashboard](#dashboard) section for details.

### Markup All the Way Down

There is no code in this system. Every agent, every skill module, every task prompt, and every piece of coordinator logic is expressed as plain Markdown. Agent definitions are `.md` files. Skills are `.md` files. Your requests to the team are `.md` files. The entire system is configured, extended, and operated through text that any non-technical person can read and edit — no programming required.

### The Net Result

A business owner drops a plain-text request into a folder. Jeeves reads it, figures out who on the team is best placed to handle it, spawns the right specialists, collects the output, and writes the finished deliverable to an output folder — all without the owner needing to know which agent did what or how Claude Code's internals work.

---

## The Team

| Name | Role | What They Do |
|------|------|-------------|
| **Jeeves** | Coordinator | (Core member) Reads your request, assigns work, tracks progress, delivers the final summary |
| **Brian** | Researcher | (Core member) Web research, competitor analysis, market research, structured reports |
| **Brittany** | HR Agent | (Core member) Hires new specialists on demand, draws from the Skills Library |
| **Claire** | Marketing Copywriter | Emails, ad copy, landing pages, social media posts |
| **Maya** | Video Script Writer | Short-form marketing video scripts (TikTok, Reels, YouTube Shorts, LinkedIn) |
| **Devon** | Developer | Scripts, MCP and API integrations |
| **Archie** | Audit Manager | Logs every task and action taken — full paper trail in a local database |
| *(grows)* | | New specialists hired by Brittany as needed, stay permanently |

---

## How to Use

### Prerequisites

Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code):

```bash
npm install -g @anthropic-ai/claude-code
```

### Start a Session

Open a terminal in the project root and start Claude Code:

```bash
claude
```

Jeeves is your interface. He runs as the top-level session coordinator — you talk to him directly. 

Initialise Jeeves:

```bash
use jeeves
```

### Two Ways to Submit Work

**Inbox file** and **direct prompt** both reach Jeeves, but they trigger very different behaviour.

| Aspect | Inbox file | Direct prompt |
|---|---|---|
| Audit trail | Full — Archie logs every delegation and output | None |
| Resumable | Yes — state file survives interruptions | No |
| Output location | `work/AgentOutbox/[id]-[slug]-[date]/` | Chat only |
| Queue support | Yes — oldest-first, numeric prefix for priority | No |
| Reference files | Yes — attach `.xlsx`, `.csv` with same stem | No |
| Formal task record | Yes — task ID assigned by Archie | No |

Use **inbox files** for any work you want delivered, tracked, and retrievable. Use **direct prompts** for quick questions, team management (hiring or dismissing agents), or one-off instructions to Jeeves.

### Submitting Work via Prompt

Type your request directly into the Claude Code session. Jeeves responds conversationally — no task record is opened, no output folder is created, and nothing is written to disk. Use this for quick questions, team management, and one-off instructions.

Examples:

```
Who is on the team?
```

```
Hire a specialist who can analyse financial statements.
```

```
Dismiss Maya and Claire.
```

```
Research the top 5 project management tools for small teams and give me a summary.
```

Jeeves may delegate to a specialist under the hood, but the result comes back as chat text rather than a file in `AgentOutbox/`.

### Submitting Work via Inbox

1. Write your request as a `.md` file and drop it into `work/OwnerInbox/`:

   ```
   work/OwnerInbox/my-request.md
   ```

2. If your request references a supporting file (spreadsheet, data file, etc.), name it with the same stem:

   ```
   work/OwnerInbox/my-request.xlsx
   work/OwnerInbox/my-request-data.csv
   ```

3. Tell Jeeves to process the inbox:

   ```
   Process the inbox.
   ```

   Or simply start your session — Jeeves will check the inbox automatically.

4. Pick up finished work from `work/AgentOutbox/`. Each task gets its own dated subfolder.

### Multiple Requests

Drop multiple `.md` files into `work/OwnerInbox/` and Jeeves processes them one at a time, oldest-first. To reprioritise, prefix a filename with a number (e.g. `001-urgent.md`).

---

## Managing the Team

### Hiring a New Specialist

Jeeves hires automatically when no existing agent fits a task. You can also request it directly:

```
Hire a specialist who can review legal documents.
```

Brittany creates the new agent from the Skills Library. The specialist stays on the team permanently.

### Dismissing an Agent

There are several specialist agents in the solution. If you want to start with the core team (Jeeves, Brian and Brittany) and build up your own, ask Jeeves to dismiss the rest.

To remove a specialist from the team, ask Jeeves:

```
Dismiss [agent name list].
```

Jeeves will remove the agent's definition file from `.claude/agents/`. This is permanent — the agent will need to be rehired if you want them back.

---

## Dashboard

AITeamBlueprint ships with a local web dashboard for browsing the audit trail without needing a server.

**File:** `dashboard/index.html`

Open it directly in any modern browser — no install or build step required.

### Loading the Database

The dashboard opens a load screen prompting you to select the audit database file:

```
data/audit.db
```

Click **Load Database**, pick the file from your filesystem, and the dashboard opens. Use **Change DB** in the header to swap to a different file, or **Refresh** to re-read the current one.

### Tasks Tab

Shows a live summary of all tasks logged by Archie:

- **Status chips** — at-a-glance counts for Total, Complete, In Progress, Blocked, Failed, and Open tasks.
- **Task list** — each task is a collapsible row showing its status, ID, timestamp, and a prompt preview. Expand a row to see the full prompt, any attached files, and a chronological **interactions timeline** — every delegation, agent hire, output produced, and task close event, with timestamps.

### Team Tab

Displays a card for every agent currently registered in the audit database — name, role, and specialty. This reflects the live roster as Archie tracks it, including any specialists hired dynamically by Brittany.

---

## File Layout

```
work/
  OwnerInbox/          ← Drop prompt files here
    done/              ← Processed prompts are archived here
  AgentOutbox/         ← Finished work lands here
    [id]-[slug]-[date]/

.claude/
  agents/              ← One .md file per team member
  skills/              ← Reusable skill modules for new hires
  state/               ← Current task state (managed by Jeeves)

data/
  audit.db             ← Full task and action log (managed by Archie)
```

---

## Skills Library

New team members are built from these skill modules:

- Web Research
- Structured Report Writing
- Marketing Copywriting
- Video Script Writing
- Coding & Software Development
- Code Review
- Data Analysis
- Email Triage

New skill files can be added to `.claude/skills/` at any time, making every future hire smarter.
