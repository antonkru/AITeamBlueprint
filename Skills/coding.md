# Skill: Coding & Software Development

## Protocol
1. Read and fully understand the requirements before writing any code.
2. Identify the language, runtime, and relevant libraries from context.
3. Write clean, minimal code — no over-engineering, no unused scaffolding.
4. For API integrations: handle auth, errors, timeouts, and rate limits explicitly.
5. Test logic mentally before writing — consider edge cases and failure modes.

## Code Quality Standards
- Functions do one thing
- Variable and function names are self-documenting
- No comments explaining *what* the code does — only *why* when non-obvious
- Error messages are actionable (tell the user what went wrong and how to fix it)

## API Integration Checklist
- Auth method documented (API key, OAuth, bearer token)
- Base URL and endpoint clearly defined
- Request headers set correctly (Content-Type, Authorization)
- Response parsing handles both success and error shapes
- Timeout and retry logic included for network calls

## Output Format
- Provide the full file content, not snippets
- Include a one-paragraph usage note at the top of the output explaining how to run or integrate the code
- If dependencies are required, list them with install commands
- Save code files to `AgentOutbox/[descriptive-filename].[ext]`
