# AITeamBlueprint — Feature Research Report
**Date:** 2026-04-20
**Prepared by:** Brian, Research Specialist
**Audience target:** Small business owners (non-technical)

---

## Executive Summary

- AITeamBlueprint gives small business owners a **ready-made AI team** — not a single chatbot, but a group of named specialists who divide up the work, just like real employees.
- A single inbox drop-off triggers the entire workflow: the owner writes what they need, and the team handles the rest from start to finish.
- The standout capability is **self-expanding hiring** — if the team lacks a skill, it recruits a new AI specialist automatically, and that specialist stays on the team permanently.
- The team already covers the most common small-business pain points: research, writing, marketing copy, software automation, and a full audit trail.
- Every completed job produces a clean file in a dedicated output folder — no digging through chat histories or copy-pasting results.

---

## Feature Highlights for Small Business Owners

### 1. Drop Your Request in One Place — the Team Takes It From There
You don't manage individual AI tools or figure out which one to use. You place your request (and any supporting files) in the `work/OwnerInbox/` folder. **Jeeves**, the team coordinator, reads it, breaks it into tasks, routes each piece to the right specialist, and delivers finished work to `work/AgentOutbox/`. You come back to a finished result — no babysitting required.

> *Think of it like emailing your office manager. You describe what you need; he figures out who does it.*

---

### 2. A Real Team of Specialists — Not a Jack-of-All-Trades Bot
Each team member has a defined job and stays in their lane. This means higher-quality output than asking one AI to do everything:

| Team Member | What They Do for You |
|-------------|----------------------|
| **Jeeves** (Coordinator) | Reads your request, assigns work, tracks progress, delivers the final summary. You never have to manage the team yourself. |
| **Brian** (Researcher) | Searches the web, cross-references sources, and produces structured reports — competitor analysis, market research, fact-finding, article summaries. Always cites his sources. |
| **Claire** (Marketing Copywriter) | Writes emails, ad copy, social media posts, and landing page content. Follows proven conversion frameworks and tailors tone to your audience. |
| **Devon** (Developer) | Writes scripts, builds automations, connects to external services (APIs), and handles data processing tasks — no coding knowledge required on your end. |
| **Archie** (Audit Manager) | Keeps a complete, timestamped log of every task and action taken. You always have a paper trail of what was done and when. |
| **Brittany** (HR Agent) | Hires brand-new specialists whenever the team hits a gap. She draws on a library of professional skills to create a fully capable new team member in one step. |

---

### 3. Your Team Grows With Your Business — Automatically
This is the feature that sets AITeamBlueprint apart from any single AI assistant.

**The problem it solves:** Every business eventually needs something outside the standard toolkit — a legal summary, a data analysis, an SEO audit, a social media strategy. With a fixed AI tool, you're stuck.

**How AITeamBlueprint handles it:**
1. Jeeves recognises that no current team member can handle the task.
2. He asks Brittany (HR) to hire a new specialist.
3. Brittany draws from a **Skills Library** — a curated collection of professional know-how — and creates a fully equipped AI employee in minutes.
4. That new specialist **stays on the team permanently**, available for every future job that fits their role.

The team you have today is not the ceiling — it's the starting point. Every new hire adds a permanent capability to your business.

---

### 4. A Growing Library of Professional Skills
New team members are built from a structured **Skills Library** that already includes:

- **Web Research** — systematic, source-cited information gathering
- **Structured Report Writing** — executive summaries, findings, and cited sources
- **Marketing Copywriting** — email, ad, and landing page frameworks proven to convert
- **Coding & Software Development** — scripts, automations, and API integrations
- **Code Review** — security, bug, and performance checks on existing code
- **Data Analysis** — pattern spotting, insights, and actionable next steps

New skills can be added to the library at any time, making every future hire smarter.

---

### 5. Every Job Leaves a Paper Trail
Archie logs every task opened, every specialist deployed, and every file produced — all stored in a local database. This means:
- You can review exactly what was done and when.
- Nothing gets lost between sessions.
- If something goes wrong, there's a full record to diagnose it.

For small business owners who need accountability (for themselves, their team, or their clients), this is built in by default — not an afterthought.

---

### 6. Results Land in a Clean Output Folder
Every completed piece of work — reports, emails, code, summaries — is written to `work/AgentOutbox/` with a clear, dated filename. No scrolling through chat. No copy-pasting. Your deliverables are organised files, ready to use or hand off.

---

### 7. Consistent Quality Standards Baked In
Each specialist follows professional protocols embedded in their role:
- **Brian** cross-references at least 3 sources and flags low-confidence claims.
- **Claire** checks every email against a quality checklist (subject line length, single CTA, proof points, paragraph length).
- **Devon** handles edge cases, timeouts, and errors — not just the happy path.
- **Archie** validates every database action before confirming it.

You get professional-grade output standards without having to specify them every time.

---

## Detailed Findings

### How the Workflow Works (Step by Step)
1. Owner places `prompt.md` (and any reference files) in `work/OwnerInbox/`.
2. Jeeves reads the inbox, opens a task record via Archie, and writes a task plan.
3. Jeeves checks whether existing specialists can cover the work.
4. If a gap exists, Brittany hires a new specialist from the Skills Library.
5. Jeeves delegates each piece of work to the appropriate specialist.
6. Each specialist reads from `work/OwnerInbox/`, does their work, and writes output to `work/AgentOutbox/`.
7. Archie logs every action taken.
8. Jeeves writes a summary file listing all outputs, then closes the task.

The owner's only touchpoint: drop files in, pick up results from `work/AgentOutbox/`.

### What Makes Dynamic Hiring Uniquely Valuable
- Most AI tools are fixed. They do what they were designed for and nothing else.
- AITeamBlueprint treats skill gaps as a **hiring problem**, not a limitation.
- The Skills Library acts as a pool of professional training — Brittany draws from it to create experts, not generalists.
- Hired agents are permanent. The business never loses a capability it has acquired.
- Brian can even **write new skill files** when a domain isn't covered yet — so the system can grow into entirely new territories.

### Current Team Headcount and Coverage
As of 2026-04-19 (per `work/AgentOutbox/team-listing-2026-04-19.md`): **5 active agents** on file.
Skills Library: **6 skill modules** available for new hires.

---

## Confidence Notes

- All findings are drawn directly from source files in the repository (`CLAUDE.md`, individual agent definition files in `.claude/agents/`, and `.claude/skills/`). **Confidence: High.**
- The team listing from `work/AgentOutbox/team-listing-2026-04-19.md` confirms 5 agents as of 2026-04-19. `README.md` contains no additional detail beyond the project title. **Confidence: High.**
- Claims about *business value* (time savings, quality standards) are inferred from the documented protocols and workflows — no external benchmarking data exists in this repository. **Confidence: Medium** (reasonable inference, not measured).

---

## Sources

All sources are internal repository files — no external URLs consulted for this report, as the research task was product documentation extraction.

1. `C:/develop/Repos/AITeamBlueprint/CLAUDE.md` — Master project overview: team roster, workflow, dynamic hiring mechanic, file conventions
2. `C:/develop/Repos/AITeamBlueprint/.claude/agents/jeeves.md` — Full coordinator workflow: inbox reading, task state, delegation, synthesis
3. `C:/develop/Repos/AITeamBlueprint/.claude/agents/brittany.md` — HR agent: hiring process, skill embedding, duplicate checks, agent template
4. `C:/develop/Repos/AITeamBlueprint/.claude/agents/brian.md` — Research specialist: web research protocol, report writing standards
5. `C:/develop/Repos/AITeamBlueprint/.claude/agents/claire.md` — Marketing copywriter: email structure, quality checklist, voice guidelines
6. `C:/develop/Repos/AITeamBlueprint/.claude/agents/devon.md` — Software developer: coding standards, API integration checklist, output format
7. `C:/develop/Repos/AITeamBlueprint/.claude/agents/archie.md` — Audit manager: database schema, logging commands, response format
8. `C:/develop/Repos/AITeamBlueprint/work/AgentOutbox/team-listing-2026-04-19.md` — Current team headcount and role descriptions as of 2026-04-19
9. `C:/develop/Repos/AITeamBlueprint/.claude/skills/web-research.md` — Web Research skill module
10. `C:/develop/Repos/AITeamBlueprint/.claude/skills/report-writing.md` — Structured Report Writing skill module
11. `C:/develop/Repos/AITeamBlueprint/.claude/skills/coding.md` — Coding & Software Development skill module
12. `C:/develop/Repos/AITeamBlueprint/.claude/skills/code-review.md` — Code Review skill module
13. `C:/develop/Repos/AITeamBlueprint/.claude/skills/data-analysis.md` — Data Analysis skill module
14. `C:/develop/Repos/AITeamBlueprint/.claude/skills/marketing-copywriting.md` — Marketing Copywriting skill module
