---
description: Review Terraform/IaC changes for security, cost, blast radius, and operational readiness
version: 1.0.0
type: orchestrator
language: "hcl"
requires:
  - /detect-stack
---

# Review Terraform

Review Terraform or Infrastructure-as-Code changes for security, cost implications, blast radius, and operational readiness.

## Step 1 — Identify IaC changes

```bash
git diff main...HEAD --name-only | grep -iE '(\.tf$|\.tfvars$|terragrunt\.hcl$|\.yaml$|\.yml$)'
```

## Step 2 — Review security

| Check | What to look for |
|-------|------------------|
| Public access | Security groups with `0.0.0.0/0` ingress on non-HTTP ports |
| IAM policies | `*` actions or `*` resources — overly permissive |
| Encryption | Storage (S3, EBS, RDS) without encryption at rest |
| Secrets | Hardcoded values in `.tf` files — use variables + secrets manager |
| Network | Public subnets for resources that should be private |
| Logging | CloudTrail, VPC flow logs, access logging disabled |

## Step 3 — Assess blast radius

| Change type | Blast radius | Action |
|-------------|-------------|--------|
| Add resource | Low | Verify naming and tagging |
| Modify resource (in-place) | Medium | Check if change forces replacement |
| Modify resource (forces new) | High | Confirm downtime is acceptable |
| Destroy resource | Critical | Confirm data backup and downstream impact |
| Modify IAM/security group | High | Verify principle of least privilege |

## Step 4 — Review cost impact

| Check | What to look for |
|-------|------------------|
| Instance sizing | Right-sized for workload? Over-provisioned? |
| Storage | GP3 vs GP2, lifecycle policies for old data |
| Data transfer | Cross-region or cross-AZ transfer costs |
| Reserved vs on-demand | Long-running workloads should use reserved/savings plans |
| Unused resources | Elastic IPs, old snapshots, detached volumes |

## Step 5 — Check operational readiness

| Check | What to look for |
|-------|------------------|
| Tagging | All resources tagged with `team`, `environment`, `service` |
| State management | Remote state with locking (S3 + DynamoDB) |
| Modules | Pinned versions, not `ref=main` |
| Variables | Descriptions and validation rules |
| Outputs | Key values exported for dependent stacks |
| Lifecycle | `prevent_destroy` on critical resources |

## Step 6 — Generate review report

```markdown
# Terraform Review Report

## Summary

- Files reviewed: N
- Blast radius: LOW / MEDIUM / HIGH / CRITICAL
- Estimated cost impact: +$X/month or neutral

## Security
- [file:line] Description

## Blast Radius
- [resource] Change type — impact description

## Cost
- [resource] Estimated impact

## Operational
- [file:line] Description

## Recommendations
- Action items before applying
```

> "Here's the Terraform review. Run `terraform plan` to confirm the changes."
