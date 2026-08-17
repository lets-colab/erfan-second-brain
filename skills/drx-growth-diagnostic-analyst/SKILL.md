---
name: drx-growth-diagnostic-analyst
description: Diagnose campaign and growth performance from funnel data, outreach records, CRM states, templates, conversions, attendance, and retention. Use when management needs to know what is working, what is not, why, and what experiment or operational fix should happen next.
---

# DR.X Growth Diagnostic Analyst

## Purpose
Turn campaign data into decisions, not activity reporting.

## Required funnel
Track where possible:
`SOURCE -> DM/CLICK -> REPLY -> POSITIVE INTENT -> CLAIM/SIGNUP -> VISIT -> SPEND/CONTENT -> RETURN`

## Metric discipline
For every rate, record numerator, denominator, time window, and confidence.
Never calculate a reply or conversion rate when send/outcome capture is incomplete.
Use `UNKNOWN / NOT RELIABLE YET` instead of fake precision.

## Outreach split
Always separate campaign types when management cares about them, including:
- Creator/KOL outreach
- First Visit Pass outreach
- Ambassador outreach
- table/RSVP acquisition

Do not collapse different campaigns into one outreach total unless identity and time-window reconciliation support it.

## Template intelligence
For each message/template capture:
- template version;
- sent count;
- seen count where available;
- replies;
- positive replies;
- claims/signups;
- verified visits;
- return visits;
- qualitative reason for response if evidence exists.

A winning template requires a sufficient and comparable sample. Assignment of a template without proof of sending is not performance evidence.

## Diagnostic loop
For each period answer:
1. What moved?
2. Where did the funnel drop?
3. Is the drop demand, offer, message, targeting, follow-up, tracking, or operations?
4. What evidence supports that diagnosis?
5. What is the smallest next test/fix?
6. What result would confirm or falsify the diagnosis?

## Current-vs-previous rule
A live dashboard should show current period first and previous verified period as comparison. Historical success must never masquerade as current activity.

## Management output
Prefer:
`WORKING | NOT WORKING | WHY / CONFIDENCE | NEXT ACTION | OWNER | NEXT CHECK`
