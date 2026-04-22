# Email Triage Skill

Apply this skill when reviewing an email inbox to identify which messages need attention and what response (if any) is warranted.

## Purpose

Email triage is the process of scanning an inbox, classifying each message by importance and required action, and producing a concise prioritised list for the owner so they can respond efficiently.

## Importance Classification

Classify every scanned email into one of four priority tiers:

1. **Critical / Urgent** — Time-sensitive, high-stakes, or from a key stakeholder. Requires same-day response.
   - Legal notices, security alerts, client escalations
   - Deadline-driven requests (interview invitations, RSVPs expiring today)
   - Direct messages from senior stakeholders, family emergencies
2. **Important — Response Needed** — Requires a personal response within 24–72 hours but is not a same-day fire.
   - Work correspondence from colleagues or clients
   - Direct personal messages from known contacts expecting a reply
   - Business opportunities, scheduling requests, invoices/payments
3. **Informational / FYI** — Worth reading but does not require a reply.
   - Newsletters the owner actively reads, order confirmations, receipts
   - Automated system notifications, calendar invites already accepted
4. **Low / Noise** — Promotional, bulk, or irrelevant.
   - Marketing emails, generic updates, spam that slipped through, social notifications

## Signals That Raise Priority

- Sender is a known individual (not a `noreply@` or bulk domain)
- Subject contains explicit urgency cues ("URGENT", "ACTION REQUIRED", "by EOD", "deadline")
- Message is a direct question addressed to the owner
- Message references a prior thread the owner initiated
- Message contains attachments requiring review, signature, or payment
- Message is from a domain matching current employer, bank, government, or legal counsel

## Signals That Lower Priority

- Sender is `noreply`, `no-reply`, `newsletter`, `marketing`, `updates`, `notifications`
- Subject line is templated or promotional ("X% off", "Flash sale", "Your weekly digest")
- Message is part of a bulk list (unsubscribe link prominent, List-Unsubscribe header)
- Message is a duplicate or follow-up in a thread already addressed

## Protocol for Each Email

For every email you examine, capture:
- **From** (sender name + email address)
- **Subject**
- **Received** (date/time, relative such as "2 hours ago" is acceptable)
- **Priority tier** (Critical / Important / Informational / Low)
- **One-sentence summary** of what the email is about
- **Recommended action** (Reply now / Reply within 24h / Read and file / Archive / Delete / Unsubscribe)
- **Suggested reply angle** — one to two sentences describing how the owner might respond (only for Critical and Important tiers)

## Output Format

Produce a single markdown report with these sections in order:

### Header
- Date of triage
- Account triaged (email address)
- Total emails scanned
- Counts per priority tier

### 1. Critical — Respond Today
For each email: a dense block with From, Subject, Received, Summary, Recommended action, Suggested reply angle.

### 2. Important — Respond This Week
Same format as Critical.

### 3. Informational — Read and File
Compact list: one line per email with From, Subject, and a three-to-six-word descriptor.

### 4. Low Priority — Safe to Ignore or Bulk Delete
A compact table or list. Group by sender domain if there are many from the same source.

### 5. Recommended Actions Summary
A short bulleted list of the top 3–5 actions the owner should take in priority order.

## Principles

- **Be decisive.** Every email gets one tier — do not hedge.
- **Protect the owner's time.** Favour concision. If an email can be summarised in six words, do not write a paragraph.
- **Never draft full replies unless explicitly requested.** Offer angles and talking points only.
- **Flag anything that looks like phishing, impersonation, or account compromise** at the top of the report regardless of normal tier.
- **Respect privacy.** Do not quote sensitive content (account numbers, passwords, personal identifiers) verbatim — describe it generically.
- **Bulk senders are safe to aggregate.** If 12 newsletters arrived, list them in one compact row.

## Quality Checklist

Before delivering the report, confirm:
- Every email scanned is accounted for in one tier
- Counts in the header match the counts in the sections
- No full draft replies (only angles) unless the owner asked for drafts
- Phishing or suspicious messages are called out explicitly
- Recommended Actions Summary lists no more than five items
