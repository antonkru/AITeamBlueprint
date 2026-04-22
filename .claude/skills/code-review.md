# Skill: Code Review

## Protocol
1. Read the full file before making any comments.
2. Identify issues across four categories: Security, Bugs, Performance, Style.
3. For each issue record: file path, line number, severity, description, and a suggested fix.
4. Summarise overall code quality at the end with a score.

## Severity Levels
- **Critical** — must fix before production (security holes, data loss risk)
- **Major** — significant bugs or performance problems
- **Minor** — style, readability, or non-critical improvements

## Output Format
- One section per category (Security, Bugs, Performance, Style)
- Each entry: `[SEVERITY] Line N: description. Suggestion: ...`
- Final line: Overall quality score — Good / Needs Work / Critical Issues
