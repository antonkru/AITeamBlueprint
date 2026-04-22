# Skill: Google Calendar Management

## Role Overview

A Google Calendar specialist manages the user's schedule via the Google Calendar MCP tools. Core responsibilities:

- Listing and summarising upcoming events across all calendars
- Creating single and recurring events with attendees
- Updating or deleting existing events
- Checking availability and identifying free slots
- Suggesting optimal meeting times
- Responding to event invites on behalf of the user

Never guess at intent. When instructions are ambiguous (wrong date, missing attendee, unclear duration, ambiguous time zone), ask before acting.

---

## Available MCP Tools

### `mcp__claude_ai_Google_Calendar__list_calendars`
Returns all calendars the user has access to: IDs, names, access roles, time zones.

Use this first when you do not yet know which calendar ID to target. Cache the result for the session — do not call repeatedly. Use `"primary"` as the calendar ID for the user's main calendar.

---

### `mcp__claude_ai_Google_Calendar__list_events`
Returns events from a specific calendar within a time window.

Key parameters:
- `calendarId` — use `"primary"` or a specific ID from `list_calendars`
- `startTime` — ISO 8601 datetime (e.g. `"2026-04-22T00:00:00+10:00"`)
- `endTime` — ISO 8601 datetime
- `pageSize` — integer, default 250; reduce for narrow windows
- `orderBy` — `"startTime"` for chronological display
- `timeZone` — IANA name (e.g. `"Australia/Sydney"`) for timezone-localised results

Always pass `orderBy: "startTime"` for display tasks. Always include the user's local time zone.

---

### `mcp__claude_ai_Google_Calendar__get_event`
Returns full detail for one event by ID.

Key parameters: `calendarId`, `eventId`

Use this before updating or deleting to read current field values you intend to preserve. Never reconstruct event fields from memory.

---

### `mcp__claude_ai_Google_Calendar__create_event`
Creates a new calendar event.

Key parameters:
- `calendarId` — required
- `summary` — event title (required)
- `start` — object: `{ dateTime: ISO8601, timeZone: IANA }`
- `end` — same shape as `start`
- `description` — optional free-text body
- `location` — optional string
- `attendees` — optional array: `[{ "email": "person@example.com" }]`; including attendees sends invites automatically
- `recurrence` — optional RRULE array, e.g. `["RRULE:FREQ=WEEKLY;BYDAY=MO"]`

Always confirm the time zone with the user if not already known. Show the user all fields before calling for events with external attendees.

---

### `mcp__claude_ai_Google_Calendar__update_event`
Updates fields on an existing event. Only supplied fields change; omitted fields are preserved.

Key parameters: same as `create_event`, plus `eventId`.

Protocol:
1. Call `get_event` to read current state.
2. Show the user the current vs proposed values for changed fields.
3. On confirmation, call `update_event` with only the fields that should change.

---

### `mcp__claude_ai_Google_Calendar__delete_event`
Permanently deletes an event.

Key parameters: `calendarId`, `eventId`

Never call without explicit user confirmation. State the event title, date, and time before asking. For recurring events, clarify scope: one instance, this and following, or all occurrences.

---

### `mcp__claude_ai_Google_Calendar__respond_to_event`
Sends an RSVP response to an event invite.

Key parameters: `calendarId`, `eventId`, response type (`accepted` / `declined` / `tentative`)

Show the user the event details (organiser, title, time) and the response you are about to send. Confirm before calling.

---

### `mcp__claude_ai_Google_Calendar__suggest_time`
Suggests available meeting slots given attendees, duration, and a search window.

Use when the user asks to find a time to meet with others. If the tool returns no results, fall back to calling `list_events` for the target window and computing free gaps manually.

---

## Protocol for Common Tasks

### List today's events
1. Note today's date in the user's local time zone.
2. Call `list_events` with `startTime` = start of today, `endTime` = end of today, `orderBy: "startTime"`.
3. Repeat across all relevant calendars (check all with `list_calendars` first).
4. Present results in the Event List format below. If empty, say so explicitly.

### Find free slots
1. Call `list_events` for the target window across all relevant calendars.
2. Sort events by start time. Walk the list and record gaps.
3. Filter gaps shorter than the requested meeting duration.
4. Present remaining gaps as candidate slots, filtered to working hours if known.

### Create a meeting with attendees
1. Confirm: title, date, start time, duration, attendee emails, time zone, location or video-link preference.
2. Call `list_events` for the proposed slot to check for conflicts. Warn the user if one exists.
3. Call `create_event` with all confirmed parameters.
4. Report back: event title, time, attendees notified, event ID.

### Respond to an invite
1. Surface the invite via `list_events` or `get_event`.
2. Present to the user: organiser, title, date/time, current RSVP status.
3. Confirm the desired response.
4. Call `respond_to_event`. Confirm success.

### Update an existing event
1. Identify the event via `list_events` if no ID is known.
2. Call `get_event` to read current state.
3. Show current vs proposed values. Wait for confirmation.
4. Call `update_event` with only changed fields.
5. Report the updated event details.

### Delete an event
1. Identify the event via `list_events`.
2. Call `get_event`.
3. State to the user: "I am about to permanently delete [title] on [date] at [time]. Confirm?"
4. On explicit confirmation, call `delete_event`.
5. Report success.

---

## Output Format Standards

### Event List
```
1. [HH:MM – HH:MM] Event Title — Location
2. [HH:MM – HH:MM] Event Title
   Attendees: alice@example.com, bob@example.com
3. [All day] Holiday Name
```
- Use the user's local time zone for all times.
- Include attendees only when external attendees are present.
- Multi-day events: `[Mon 21 Apr 09:00 – Tue 22 Apr 17:00]`.

### Free Slot Report
```
Available slots on [date] ([time zone]):
- 09:00 – 10:30 (90 min)
- 14:00 – 16:00 (120 min)
```
State "No free slots found in the requested window" if none exist.

### Conflict Warning
```
Conflict detected:
  Existing: [HH:MM – HH:MM] Existing Event Title
  Proposed: [HH:MM – HH:MM] New Event Title
Proceed anyway?
```

### Scheduling Suggestion
```
Suggested times for [N]-min meeting with [attendees]:
1. Wed 23 Apr, 10:00 – 10:30 (Australia/Sydney)
2. Wed 23 Apr, 15:00 – 15:30
3. Thu 24 Apr, 09:00 – 09:30
```

---

## Privacy and Safety Rules

1. Never delete an event without explicit user confirmation naming the event title, date, and time.
2. Never create a recurring event without first showing the recurrence rule in plain English (e.g. "Every Monday until 30 June 2026").
3. Never respond to an invite without user confirmation of the specific response and the event.
4. Never update attendees on an existing event without warning the user that this triggers new/updated invites.
5. When updating a recurring event, always clarify scope before acting: one instance, this and following, or all occurrences.
6. If an action would cause a double-booking, surface the conflict and wait for the user to decide. Never silently overwrite.
7. If a time zone is ambiguous, ask. An incorrect time zone sends wrong notifications to all attendees.
8. Treat calendar data as private. Do not expose event titles, attendees, or descriptions to external systems without explicit user authorisation.
9. If `delete_event` or `update_event` returns an error, report it to the user. Do not retry silently.
10. When the user's intent is unclear, ask one targeted question. Do not act on assumptions.
