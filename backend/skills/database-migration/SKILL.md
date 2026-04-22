---
description: Review database migration files for safety — reversibility, data preservation, locking, and rollback strategy
version: 1.0.0
type: utility
language: "*"
---

# Database Migration Review

Review database migration files for safety before they run against production. Checks reversibility, data preservation, locking behavior, and rollback strategy.

## Step 1 — Identify migration files

Find new or modified migration files:

```bash
git diff main...HEAD --name-only | grep -iE '(migration|migrate|schema|flyway|liquibase|alembic|prisma)'
```

Common migration directories:

| Framework | Path |
|-----------|------|
| Prisma | `prisma/migrations/` |
| Alembic | `alembic/versions/` |
| Flyway | `db/migration/` |
| Knex | `migrations/` |
| Rails | `db/migrate/` |
| Django | `*/migrations/` |

## Step 2 — Check reversibility

| Check | What to look for |
|-------|------------------|
| Down migration | Every `up` has a corresponding `down` |
| Drop column | Data will be lost — is it backed up or migrated? |
| Drop table | Confirm the table is truly unused (check foreign keys) |
| Rename | Renames are hard to reverse — consider add + migrate + drop pattern |

## Step 3 — Check data safety

| Check | What to look for |
|-------|------------------|
| NOT NULL on existing column | Will fail if existing rows have NULLs — need default or backfill |
| Column type change | Implicit casting may lose data (e.g., `varchar` → `int`) |
| Unique constraint | Will fail if duplicates already exist |
| Foreign key | Will fail if orphaned rows exist |

## Step 4 — Check locking behavior

| Operation | Lock type | Risk |
|-----------|-----------|------|
| `ALTER TABLE ADD COLUMN` | Usually safe | Low (most DBs don't lock) |
| `ALTER TABLE ADD COLUMN ... DEFAULT` | Table lock (Postgres < 11) | High for large tables |
| `CREATE INDEX` | Table lock | Use `CONCURRENTLY` for large tables |
| `ALTER TABLE ... NOT NULL` | Full scan + lock | High for large tables |
| `DROP TABLE` | Exclusive lock | Ensure no active queries |

## Step 5 — Check rollback strategy

- **Is there a rollback script?** Manual SQL or down migration?
- **Has the migration been tested** on a copy of production data?
- **Is it idempotent?** Can it be run twice without breaking?
- **Is it backwards compatible?** Can the old code run against the new schema?

## Step 6 — Produce report

```markdown
# Migration Review Report

## Summary

- Migrations reviewed: N
- Risk level: LOW / MEDIUM / HIGH / CRITICAL

## Safety Issues

- [file:line] Description — risk level

## Recommendations

- Description of recommended changes

## Checklist

- [ ] Down migration exists and tested
- [ ] Tested on production-size dataset
- [ ] Backwards compatible with current code
- [ ] Rollback plan documented
```

> "Here's the migration review. Any questions about the risk assessment?"
