# Skill: Idea Feasibility Research

This skill file is the authoritative protocol for producing a 10-slide idea feasibility deck.
Read it in full before starting any feasibility task.

---

## 1. 10-Slide Deck Structure

Produce slides in the exact order below. Each slide is a `##` section in the output file.

| # | Title | Must Contain |
|---|-------|-------------|
| 1 | Idea + Verdict at a Glance | One-sentence idea statement; GREEN / YELLOW / RED signal; 3-bullet executive summary. |
| 2 | TAM / SAM / SOM | Sized figures with confidence ratings; methodology used (top-down or bottom-up); key assumptions listed. |
| 3 | Competitor Landscape & Pricing | Table: competitor name, tier (direct/indirect), pricing model, price point, key differentiator. Min 3 rows. |
| 4 | SWOT Matrix | 2×2 grid; max 4 entries per quadrant; no generic filler (see §3 conventions). |
| 5 | v1 Cost to Build | Build / Buy / Staff breakdown with line-item estimates; total 6-month runway burn (see §6). |
| 6 | Sourcing & Tooling Stack | Bucketed stack recommendation: infra, data, auth, payments, comms, AI/ML, analytics (see §8). |
| 7 | Founding Team Profile Required | Required archetypes; founder-market fit assessment; flagged gaps (see §7). |
| 8 | GTM Wedge — First 100 Customers | Beachhead definition; channel shortlist; recommended wedge with reasoning (see §4). |
| 9 | Top 3 Risks | Risk name; likelihood (H/M/L); impact (H/M/L); one-line mitigation. |
| 10 | 30 / 60 / 90 Day Milestones + Verdict | Three milestone rows; one-paragraph verdict with explicit GREEN / YELLOW / RED signal and rationale. |

**Output filename:** `feasibility-deck-[idea-slug]-[YYYY-MM-DD].md` in the task's outbox folder.

---

## 2. TAM / SAM / SOM Sizing Methodology

**Definitions**

- **TAM (Total Addressable Market):** Maximum global revenue opportunity if 100% market share were captured.
- **SAM (Serviceable Addressable Market):** Subset of TAM reachable with current business model and geography.
- **SOM (Serviceable Obtainable Market):** Realistic share of SAM capturable in years 1–3.

**Top-Down vs. Bottom-Up**

| Method | Use When | Risk |
|--------|----------|------|
| Top-Down | Market research reports exist (IBISWorld, Statista, Gartner); useful for TAM. | Inflates figures; treat as ceiling only. |
| Bottom-Up | Unit economics are known; preferred for SAM and SOM. | Requires validated assumptions. |

Prefer **bottom-up for SOM** always. Use top-down only for TAM when a credible third-party report exists within 24 months of today.

**Worked Template**

```
TAM  = [Total users/businesses in segment] × [ARPU]
     = 50M users × $120/yr = $6B   [Confidence: Low — top-down, 2024 Statista report]

SAM  = [Segment reachable with English-language SaaS, SMB tier]
     = 8M users × $120/yr = $960M  [Confidence: Medium — filtered from TAM]

SOM  = [Realistic 3-yr penetration at current team size]
     = 8M × 0.5% = 40K users × $120/yr = $4.8M ARR  [Confidence: Medium — bottom-up]
```

**Confidence Ratings**

- **High:** Bottom-up; assumptions validated by interviews or live data; source < 12 months old.
- **Medium:** Mix of top-down and inference; source 12–24 months old.
- **Low:** Top-down only; no primary validation; source > 24 months old or extrapolated.

Always state the confidence rating inline, e.g. `$4.8M ARR [Confidence: Medium]`.

---

## 3. SWOT Matrix Conventions for Early-Stage Ideas

**Layout (use a Markdown table or fenced 2×2 block)**

```
| INTERNAL          | EXTERNAL          |
|-------------------|-------------------|
| Strengths (S)     | Opportunities (O) |
| Weaknesses (W)    | Threats (T)       |
```

**Rules**

- **Strengths / Weaknesses** = internal (team, IP, capital, existing users).
- **Opportunities / Threats** = external (market trends, regulation, competitors, macro).
- Cap at **3–4 bullet points per quadrant**. If you have more, rank and keep top 4.
- Each entry must be specific. Banned phrases: "large market", "strong team", "competitive space".
- Every Strength must have a named evidence source or a verifiable claim.

**Example — Good vs. Bad**

Bad Strength: "Strong founding team."
Good Strength: "CEO has 7 years B2B SaaS sales; closed $2M ARR at previous role [verifiable LinkedIn]."

Bad Threat: "Lots of competition."
Good Threat: "Salesforce announced a competing feature in March 2025 [1]; incumbent has 60% market share."

---

## 4. GTM Wedge Framework — First 100 Customers

**Step 1 — Define the Beachhead**
Pick one narrow segment where the pain is acute, the buyer is reachable, and the use case is repeatable.
Criteria: homogeneous buyers, clear budget owner, word-of-mouth likely within the segment.

**Step 2 — Evaluate Channels**

| Channel | Best Fit | Cost | Speed |
|---------|----------|------|-------|
| Founder-led outbound (email/LinkedIn) | B2B, high ACV (>$5K/yr) | Low | Medium |
| Community seeding | Dev tools, prosumer, niche verticals | Low | Slow |
| Content / SEO | Long buying cycle, high search intent | Low | Slow |
| Partnerships / integrations | Platform ecosystems (Shopify, Slack) | Medium | Medium |
| Paid acquisition | Known CAC, repeatable unit economics | High | Fast |
| Product-led / free tier | Self-serve, viral loop possible | Low | Fast if viral |

**Step 3 — Recommend One Wedge**
State: channel chosen, target persona, outreach script or content hook, and what "working" looks like (e.g. "5 paid pilots in 60 days"). Explain why rejected channels were deprioritised.

**Rule:** Do not recommend paid acquisition as the primary wedge for pre-revenue ideas — it burns capital before product-market fit is confirmed.

---

## 5. Green / Yellow / Red Verdict Rubric

Apply this rubric at Slide 1 and Slide 10. Every threshold must be checked explicitly.

### GREEN — Proceed
All of the following must be true:
- SAM ≥ $500M (Medium or High confidence) **or** SOM ≥ $5M ARR within 3 years (bottom-up, High confidence).
- At least one GTM wedge identified with a clear, reachable beachhead.
- Top 3 risks all rated Likelihood × Impact ≤ Medium × Medium.
- v1 can be built within $250K (or 6 months of founder time + ≤$10K/mo infra/SaaS spend).
- No single-point-of-failure dependency (e.g. one API, one distribution partner, one regulation).

### YELLOW — Proceed with Caution
One or more of the following:
- SAM $100M–$500M or confidence is Low.
- One risk rated High likelihood or High impact (but not both).
- GTM wedge exists but requires an unproven assumption (e.g. "cold email will convert at 5%").
- v1 cost $250K–$750K or timeline 6–12 months.
- One significant regulatory or technical unknown.

### RED — Do Not Proceed (without major pivots)
Any one of the following:
- SAM < $100M with Low confidence, or no credible path to $5M ARR.
- Two or more High × High risks.
- No defensible GTM wedge (reliant on viral growth or undifferentiated paid spend only).
- v1 cost > $750K before first revenue.
- A fatal structural flaw: patent block, regulated market with no clear licence path, or a dominant incumbent with switching costs the idea cannot overcome.

---

## 6. v1 Cost-to-Build Estimation

Break costs into three buckets. Provide a low / mid / high range.

### Build (Engineering)
`Engineering hours × blended hourly rate`

| Scenario | Hours | Blended Rate | Cost |
|----------|-------|--------------|------|
| Solo technical founder | 600 hrs (3 months FT) | Opportunity cost only | $0 cash |
| 2-person contracted team | 1,200 hrs | $75–$125/hr | $90K–$150K |
| Offshore agency | 1,500 hrs | $35–$60/hr | $52K–$90K |

Typical software v1 scope: auth, core feature loop, basic admin, payment integration — 400–800 hours.

### Buy (SaaS / API / Infra Monthly Burn)
Estimate monthly recurring spend for the stack. Annualise for the 6-month runway figure.

Typical v1 monthly burn:
- Infra (AWS/GCP/Vercel): $50–$500/mo
- Auth (Auth0/Clerk): $0–$300/mo
- AI/ML APIs (OpenAI/Anthropic): $50–$2,000/mo (usage-dependent)
- Payments (Stripe): 2.9% + 30c per transaction (no fixed cost until revenue)
- Monitoring/analytics: $0–$200/mo

Total typical "Buy" burn: **$150–$3,000/mo** for a pre-revenue v1.

### Staff (Founders' Fully-Loaded Cost)
`Monthly personal runway burn × number of founders × 6 months`

Example: 2 founders at $5K/mo personal draw = $60K for 6 months.

**Total v1 Estimate Template**
```
Build:  [hours] hrs × $[rate]/hr = $[X]
Buy:    $[monthly] × 6 months   = $[Y]
Staff:  [N] founders × $[draw] × 6 = $[Z]
───────────────────────────────────
TOTAL 6-MONTH RUNWAY COST: $[X+Y+Z]
```

---

## 7. Founding Team Profile Required

### Required Archetypes

| Archetype | Covers | Red Flag if Missing |
|-----------|--------|---------------------|
| Technical | Product build, architecture, security | Outsourcing 100% of engineering pre-revenue. |
| Commercial | Sales, BD, pricing, customer discovery | No one with direct B2B selling experience for B2B ideas. |
| Domain | Deep subject matter expertise in the target vertical | Especially critical for regulated industries (health, finance, legal). |

One person can cover two archetypes (e.g. technical founder with prior industry experience). A two-person team covering all three archetypes is the YC-standard baseline.

### Founder-Market Fit Assessment
State explicitly: Does the founding team have a personal or professional connection to the problem? (Prior user, domain expert, repeat founder in space.) Flag if the answer is No — it is not disqualifying but it raises the risk rating on GTM and discovery.

### Skill-Coverage Matrix (include in Slide 7)
```
| Skill         | Covered? | By Whom  | Gap Risk |
|---------------|----------|----------|----------|
| Engineering   | Yes/No   | [Name]   | H/M/L    |
| Sales/BD      | Yes/No   | [Name]   | H/M/L    |
| Domain knowl. | Yes/No   | [Name]   | H/M/L    |
| Design/UX     | Yes/No   | [Name]   | H/M/L    |
| Finance/Ops   | Yes/No   | [Name]   | H/M/L    |
```

---

## 8. Sourcing and Tooling Stack

Recommend a v1 stack using the bucket structure below. Pick proven defaults; flag where the choice depends on the specific idea.

| Bucket | Proven Defaults | Idea-Dependent Alternatives |
|--------|-----------------|-----------------------------|
| Infra / Hosting | Vercel (frontend) + Railway or Render (backend) | AWS / GCP if scale or compliance needed |
| Database | Supabase (Postgres) or PlanetScale | MongoDB if document-heavy; Redis for cache |
| Auth | Clerk or Auth0 | NextAuth for Next.js-only; Firebase Auth for mobile |
| Payments | Stripe | Paddle (for EU VAT compliance); Lemon Squeezy (indie) |
| Comms (email/SMS) | Resend (transactional email) + Twilio (SMS) | SendGrid; Postmark |
| AI / ML | OpenAI API (GPT-4o) or Anthropic API (Claude) | Replicate for image/audio; Hugging Face for open models |
| Analytics | PostHog (product analytics, open-source) | Mixpanel; Amplitude |
| Monitoring | Sentry (errors) + Uptime Robot | Datadog if enterprise-grade SLAs needed |

**Rules**
- Recommend the simplest stack that can reach 100 paying customers. Do not over-engineer.
- Flag any stack component with a pricing cliff (e.g. "Auth0 free tier ends at 7,500 MAU — budget for upgrade at scale").
- For AI-heavy products, always estimate API cost per transaction and project monthly burn at 1K, 10K, and 100K monthly active users.

---

## 9. Citation and Recency Rules

- Every factual claim (market size, competitor pricing, regulatory fact, cost figure) must carry a numbered footnote `[N]`.
- Source format: `[N] Author/Publisher, "Title", URL, accessed YYYY-MM-DD.`
- **Prioritise sources published within 12 months of today's date.** If only an older source exists, append `[dated — no recent source found]` inline.
- Sources older than 36 months may not be used as the sole support for a market size claim. Supplement with a bottom-up estimate.
- Apply the citation conventions from `web-research.md`: verify the page loads and contains the claimed fact before citing; do not cite a homepage as evidence of a specific claim.
- Collect all footnotes in a `## Sources` section at the end of the deck file.

**Authoritative Starting Points for Feasibility Research**
- YC Library: https://www.ycombinator.com/library
- a16z essays: https://a16z.com/
- Bessemer Venture Partners: https://www.bvp.com/atlas
- First Round Review: https://review.firstround.com/
- Statista / IBISWorld / PitchBook for market data (paid; use free previews + cite the report name)

---

## 10. Output Filename Convention

Save the completed deck as:

```
feasibility-deck-[idea-slug]-[YYYY-MM-DD].md
```

- `[idea-slug]` — 3–5 word kebab-case slug derived from the idea name (e.g. `ai-legal-doc-review`).
- `[YYYY-MM-DD]` — date the deck is produced.
- Place the file in the task's outbox folder: `work/AgentOutbox/[task-id]-[task-slug]-[YYYY-MM-DD]/`.

Do not create additional files (no separate competitor analysis file, no separate SWOT file). The single deck file is the deliverable.
