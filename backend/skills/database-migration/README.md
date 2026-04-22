# /database-migration

Review database migration files for safety before production deployment.

## What it does

- Checks migration reversibility (up/down parity)
- Validates data safety (NOT NULL, type changes, constraints)
- Assesses locking behavior and table size risks
- Reviews rollback strategy and backwards compatibility

## Usage

```
/database-migration
```
