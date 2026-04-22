---
description: Generate an incident response runbook for a service — detection, triage, mitigation, and post-mortem
version: 1.0.0
type: utility
language: "*"
---

# Incident Runbook Generator

Generate a structured incident response runbook for a service. Covers detection, triage, mitigation steps, and post-mortem template.

## Step 1 — Identify the service

Ask the user or detect from context:

- Service name and purpose
- Dependencies (databases, APIs, queues, caches)
- Traffic patterns (steady, spiky, batch)
- SLOs (latency, error rate, availability)

## Step 2 — Map failure modes

For each dependency, identify failure modes:

| Component | Failure mode | Impact | Detection |
|-----------|-------------|--------|-----------|
| Database | Connection pool exhaustion | Requests fail with timeout | Connection count metric > threshold |
| Database | Replication lag | Stale reads | Replica lag metric > 30s |
| API dependency | Timeout | Degraded response | p99 latency spike |
| API dependency | 5xx errors | Feature unavailable | Error rate > 1% |
| Cache | Eviction storm | Latency spike | Hit rate drop + DB load spike |
| Queue | Consumer lag | Processing delay | Queue depth growing |

## Step 3 — Generate runbook sections

### Detection

- Dashboards and alerts to check first
- Key metrics and their healthy ranges
- Log queries for common error patterns

### Triage

- Severity classification (SEV1–SEV4)
- Escalation paths per severity
- Communication channels and templates

### Mitigation

For each failure mode, provide step-by-step mitigation:

```
1. Confirm the issue (check dashboard X, run query Y)
2. Assess impact (affected users, data at risk)
3. Apply fix (restart service, scale up, failover, rollback)
4. Verify recovery (check metrics return to normal)
5. Communicate resolution
```

### Post-mortem template

```markdown
## Incident: [title]
**Date:** YYYY-MM-DD
**Duration:** Xh Ym
**Severity:** SEVN
**Impact:** N users affected, N requests failed

### Timeline
- HH:MM — Alert fired
- HH:MM — Incident declared
- HH:MM — Root cause identified
- HH:MM — Mitigation applied
- HH:MM — Resolved

### Root cause
What actually broke and why.

### Action items
- [ ] Fix — prevent recurrence
- [ ] Detect — improve alerting
- [ ] Mitigate — reduce blast radius
```

## Step 4 — Output

Write the runbook to `docs/runbooks/<service-name>.md` and present to the user.

> "Here's the runbook. Want me to add more failure modes or adjust the severity thresholds?"
