# Skill: Legal Document Review

## Purpose
Equip any agent with a repeatable, professional protocol for reviewing legal documents — contracts, NDAs, service agreements, data processing agreements, employment contracts, and similar instruments — to identify risk, ambiguity, missing protections, and compliance issues, and to present findings in a structured, actionable report.

> **Non-practising solicitor caveat.** An AI agent applying this skill is not a qualified legal practitioner and cannot provide legal advice. All output must be framed as a structured analytical review, not legal advice. Where findings carry material legal consequence, the output must recommend that the principal obtains review by a qualified solicitor or barrister in the relevant jurisdiction.

---

## Part 1 — Pre-Review Protocol

### 1.1 Understand the Brief
Before reading a single clause, confirm:
- **Document type** — contract, NDA, SaaS agreement, employment contract, data processing agreement, policy, etc.
- **The reviewing party's position** — which party are you reviewing on behalf of? What is their role (buyer, supplier, data controller, employee, licensor)?
- **Jurisdiction** — governing law stated in the document and the party's home jurisdiction. Flag if they differ.
- **Purpose of the review** — signing decision, negotiation input, due diligence, compliance audit?
- **Risk appetite** — standard commercial caution, or heightened scrutiny (e.g., high-value transaction, regulated sector)?

### 1.2 First-Pass Read
Read the entire document once before annotating. Do not flag issues on the first pass. Build a mental map of:
- The parties and their roles
- The core commercial deal (what is being exchanged, at what price, over what term)
- The document's overall structure and any defined terms
- Any schedules, annexures, or incorporated documents

### 1.3 Identify Governing Documents
Note any documents incorporated by reference (e.g., "as defined in Schedule 2", "subject to the Supplier's standard terms"). Flag if those documents have not been provided — they are in-scope for review and their absence is itself a finding.

---

## Part 2 — What to Review

Work through the document clause by clause. For each clause, assess it against the categories below.

### 2.1 Parties and Execution
- Are all parties correctly and fully identified (legal name, registered number, jurisdiction of incorporation)?
- Is the execution block present and appropriate for each party type (e.g., company seal, authorised signatory)?
- Are any parties signing as agent, trustee, or guarantor? If so, is the authority clearly stated?

### 2.2 Defined Terms
- Are key terms defined, and are those definitions precise?
- Are definitions asymmetric — i.e., defined broadly for one party and narrowly for the other?
- Is any term left undefined that is central to the commercial deal or a party's obligations?
- Watch for: circular definitions, definitions that override plain meaning, and defined terms used inconsistently.

### 2.3 Scope and Obligations
- Are each party's obligations clearly and specifically stated?
- Are performance standards defined (e.g., reasonable endeavours, best endeavours, absolute obligation)? Note that "best endeavours" is more onerous than "reasonable endeavours" under English law.
- Are deliverables, timelines, and acceptance criteria specified?
- Is there ambiguity about what is in or out of scope?

### 2.4 Payment Terms
- Is pricing fixed, variable, or indexed? What are the adjustment mechanisms?
- Are payment timelines and methods specified?
- Are there late payment penalties, interest provisions, or suspension rights?
- Are invoicing requirements clear?
- Watch for: automatic price escalation clauses, vague milestone definitions, one-sided set-off rights.

### 2.5 Term and Termination
- What is the contract duration? Is there an auto-renewal clause? What is the notice period to prevent renewal?
- What are the grounds for termination (for cause, for convenience, material breach, insolvency)?
- Are termination rights mutual or one-sided?
- What are the consequences of termination — survival clauses, wind-down obligations, data return/deletion?
- Watch for: inadequate cure periods, termination for convenience with no notice or compensation, survival clauses that extend onerous obligations indefinitely.

### 2.6 Intellectual Property
- Who owns IP created during the contract (work-for-hire vs. retained ownership)?
- Is pre-existing IP (background IP) clearly carved out from any assignment?
- Are licence grants specific as to scope, territory, duration, and exclusivity?
- Watch for: broad IP assignment clauses that unintentionally transfer background IP; perpetual royalty-free licences granted without reciprocal benefit.

### 2.7 Confidentiality
- Is "confidential information" defined? Is the definition mutual or one-sided?
- What are the permitted disclosures (e.g., to employees, professional advisers, as required by law)?
- What is the duration of the confidentiality obligation — does it survive termination, and for how long?
- Are there obligations to return or destroy confidential information on termination?
- Watch for: indefinite confidentiality obligations that may be unenforceable; overly broad definitions that capture publicly available information.

### 2.8 Indemnities
- What indemnities are given by each party? Are they mutual or asymmetric?
- Is indemnity scope limited to direct losses, or does it extend to indirect, consequential, or third-party losses?
- Are there carve-outs for the indemnified party's own negligence or wilful default?
- Watch for: broad indemnities with no cap; indemnities that extend to losses caused by the indemnified party's own acts.

### 2.9 Limitation of Liability
- Is liability limited for both parties, or only one?
- What is the liability cap — a fixed sum, a multiple of fees paid, or uncapped?
- What categories of loss are excluded (indirect, consequential, loss of profit, loss of data)?
- Are there carve-outs from the cap (death/personal injury, fraud, wilful misconduct, data protection breaches)? These carve-outs are standard and their absence is a red flag.
- Watch for: caps that are so low as to be commercially inadequate; exclusions of liability for data loss without a reciprocal data protection obligation.

### 2.10 Data Protection and Compliance
- If personal data is processed, is there a data processing agreement (DPA) or appropriate Article 28 GDPR clauses?
- Are the roles of data controller and data processor correctly allocated?
- Are sub-processor restrictions present? Is prior written consent required?
- Are data breach notification obligations included (72-hour ICO notification requirement under UK GDPR)?
- Are there anti-bribery and corruption clauses (required under the UK Bribery Act 2010 for many commercial contracts)?
- Are there sanctions compliance clauses if the contract involves international parties or cross-border payments?
- Watch for: contracts involving personal data with no DPA; data retention obligations that conflict with GDPR deletion rights.

### 2.11 Dispute Resolution and Governing Law
- What is the governing law? Does it favour one party's home jurisdiction?
- What is the dispute resolution mechanism — litigation, arbitration, expert determination, mediation first?
- Is the jurisdiction clause exclusive or non-exclusive?
- Watch for: governing law or jurisdiction that would be inconvenient or costly for the reviewing party to enforce; arbitration clauses in low-value contracts where litigation would be more efficient.

### 2.12 Force Majeure
- Is there a force majeure clause? What events are covered?
- Does it excuse payment obligations or only performance obligations?
- Is there a notice requirement and a cap on the period of excuse before termination rights arise?
- Watch for: force majeure clauses that are so broad they excuse ordinary commercial risk; absence of a time limit allowing indefinite suspension of obligations.

### 2.13 Entire Agreement and Variation
- Is there an entire agreement clause? Does it exclude representations made during negotiation?
- How can the agreement be varied — in writing only, or by conduct?
- Watch for: variation clauses that allow one party to unilaterally amend terms (common in consumer-facing contracts and SaaS agreements).

### 2.14 Assignment and Subcontracting
- Can either party assign the contract without consent?
- Are subcontracting rights unrestricted?
- Watch for: one-sided assignment rights; no restriction on assignment to competitors.

---

## Part 3 — Risk Classification

Assign every finding a severity level. Be consistent. Do not inflate severity.

| Severity | Label | Criteria | Example |
|---|---|---|---|
| 1 | **CRITICAL** | Likely to cause significant financial loss, legal liability, regulatory breach, or loss of fundamental rights if unaddressed. Should prevent signing as drafted. | Uncapped indemnity for third-party claims; IP assignment covering background IP; no data processing agreement where personal data is processed. |
| 2 | **MODERATE** | Materially disadvantageous or creates meaningful risk, but not necessarily a deal-breaker. Should be negotiated before signing. | Auto-renewal with inadequate notice period; limitation of liability cap below fee value; one-sided termination for convenience. |
| 3 | **LOW** | Minor, technical, or drafting issue. Preferable to address but unlikely to cause material harm. | Defined term used inconsistently in one clause; governing law clause non-exclusive where exclusive would be preferable; missing recitals. |

---

## Part 4 — Recommended Redlines and Alternative Language

For every CRITICAL finding, and for MODERATE findings wherever possible, provide:

1. **The problematic text** — quote the exact clause or phrase at issue.
2. **Why it is problematic** — one to three sentences explaining the risk in plain terms.
3. **Suggested alternative language** — a draft replacement clause or phrase. Mark deletions with ~~strikethrough~~ and insertions in **bold**.
4. **Fallback position** — if the counterparty will not accept the preferred language, state the minimum acceptable alternative.

### Redline Conventions
- Use `~~deleted text~~` for proposed deletions.
- Use `**inserted text**` for proposed insertions.
- Do not rewrite entire clauses unless the original is irredeemable. Targeted amendments are easier to negotiate.
- Accompany every redline with a one-sentence rationale in brackets: `[Rationale: limits indemnity exposure to direct losses caused by our breach only]`.

---

## Part 5 — Output Format

Every legal document review must be delivered in the following structure. Do not deviate from this format.

```
# Legal Document Review — [Document Title]

## Metadata
- Document type: [e.g., Mutual NDA / SaaS Subscription Agreement]
- Reviewing party: [Party name and role]
- Counterparty: [Counterparty name and role]
- Governing law: [as stated in document]
- Date of document: [version date or execution date]
- Date of review: [today's date]
- Reviewer note: This review is an analytical assessment, not legal advice.
  Material findings should be reviewed by a qualified solicitor before signing.

---

## Executive Summary
[3–6 sentences. State the nature of the document, the overall risk level
(HIGH / MEDIUM / LOW), the number of Critical and Moderate findings,
and the headline recommendation (do not sign as drafted / sign with
negotiated amendments / sign with minor clarifications / sign as is).]

## Overall Risk Rating: [HIGH / MEDIUM / LOW]

---

## Findings Summary Table

| # | Clause | Issue | Severity |
|---|---|---|---|
| 1 | Clause 8.2 — Indemnity | Uncapped indemnity for all third-party claims | CRITICAL |
| 2 | Clause 12 — Auto-renewal | 90-day notice to prevent renewal is excessive | MODERATE |
| 3 | Clause 2.1 — Definitions | "Confidential Information" not defined | CRITICAL |

---

## Clause-by-Clause Analysis

For each finding:

### Finding [#] — [Clause Reference and Heading] [CRITICAL / MODERATE / LOW]

**Current language:**
> [Quote the relevant text verbatim]

**Issue:**
[Explain the risk clearly and precisely. State who is exposed, to what, and why.]

**Recommended redline:**
> ~~[deleted text]~~ **[inserted text]**

[Rationale: one sentence.]

**Fallback position (if counterparty resists):**
[State the minimum acceptable alternative.]

---

## Missing Provisions
[List any clauses that are absent but should be present given the document
type and the reviewing party's position. Rate each as CRITICAL or MODERATE.]

---

## Compliance Observations
[Note any apparent regulatory compliance issues — GDPR, Bribery Act,
sector-specific regulation, etc. Flag where specialist regulatory advice
is required.]

---

## Recommendations
1. [Specific action — do not sign until clause X is amended.]
2. [Specific action — negotiate cap on liability in clause Y.]
3. [Specific action — obtain the incorporated Schedule 3 for review.]
4. [Where applicable: seek qualified legal advice on [specific issue].]
```

---

## Part 6 — Tone and Style

- **Precise.** Use the exact clause number and heading. Quote text verbatim when identifying issues.
- **Formal.** Write in full sentences. Do not use bullet fragments in the analysis sections.
- **Legally cautious.** Do not state that a clause is "fine" or "acceptable" without qualification. If a clause is standard and presents no material risk, note it as such and move on.
- **Non-advisory caveats.** Any finding with material financial or legal consequence must end with: "This point warrants review by a qualified solicitor."
- **Jurisdiction-aware.** Note when an issue is jurisdiction-specific. Do not apply English law analysis to a contract governed by Scots law, US law, or another system without flagging the difference.
- **No speculation.** If the risk of a clause depends on facts not present in the document (e.g., the value of the contract, the nature of the data processed), state the assumption on which the finding is based.

---

## Part 7 — Common Document Type Priorities

### NDA / Confidentiality Agreement
Priority checks: definition of confidential information (scope and carve-outs), mutual vs. unilateral obligations, duration of post-termination obligations, return/destruction of information, injunctive relief provision, governing law.

### SaaS / Software Subscription Agreement
Priority checks: data processing agreement and GDPR compliance, IP ownership of customer data and outputs, service level commitments and remedies, unilateral variation clause, auto-renewal and cancellation, liability cap relative to subscription fee.

### Employment Contract
Priority checks: post-termination restrictions (non-compete, non-solicit — enforceability under English law requires these to be reasonable in scope and duration), IP assignment (background IP carve-out), garden leave, governing law.

### Services / Consultancy Agreement
Priority checks: scope of services (change control mechanism), IP ownership, payment and milestone terms, limitation of liability, indemnity, termination for convenience and notice, data protection if personal data is involved.

### Data Processing Agreement
Priority checks: Article 28 UK GDPR compliance, sub-processor list and consent mechanism, data breach notification timescale (72 hours to ICO), audit rights, data deletion/return on termination, international transfer safeguards (standard contractual clauses or adequacy decision).

---

## Common Pitfalls
- Reviewing only the main body and missing schedules or incorporated terms
- Failing to note asymmetric obligations that appear balanced on their face
- Accepting "market standard" as automatically acceptable — standard terms still carry risk
- Overlooking survivability clauses that extend onerous obligations past termination
- Not flagging missing provisions — the absence of a clause is as important as a problematic one
- Applying the wrong jurisdiction's legal framework without flagging it
