---
description: Terraform and infrastructure-as-code conventions for the infra team
globs:
  - "**/*.tf"
  - "**/*.tfvars"
  - "**/terragrunt.hcl"
---

# Terraform Conventions

Follow these conventions when writing or reviewing Terraform code.

## File Structure

| File | Purpose |
|------|---------|
| `main.tf` | Primary resources |
| `variables.tf` | Input variable declarations |
| `outputs.tf` | Output value declarations |
| `providers.tf` | Provider configuration and versions |
| `locals.tf` | Local values and computed expressions |
| `data.tf` | Data source lookups |
| `versions.tf` | Required provider versions and terraform version |

## Naming

- **Resources**: `snake_case`, descriptive — `aws_s3_bucket.app_assets`, not `aws_s3_bucket.bucket1`
- **Variables**: `snake_case` with type and description — always include `description`
- **Outputs**: `snake_case`, match the resource they expose
- **Modules**: `kebab-case` directories — `modules/api-gateway/`

## State Management

- **Always remote state** — S3 + DynamoDB for locking, never local
- **One state per environment** — separate state files for dev/staging/prod
- **Never manually edit state** — use `terraform state mv`, `terraform import`
- **Lock state during applies** — DynamoDB table for locking

## Modules

- **Pin versions** — `source = "git::...?ref=v1.2.3"`, never `ref=main`
- **Small and focused** — one module per logical resource group
- **Input validation** — use `validation` blocks on variables
- **Output useful values** — IDs, ARNs, endpoints that consumers need

## Security

- **No hardcoded secrets** — use `sensitive = true` variables + secrets manager
- **Least privilege IAM** — specific actions on specific resources, never `*`
- **Encryption everywhere** — enable at-rest and in-transit encryption
- **Private by default** — resources in private subnets unless explicitly public

## Tagging

All resources must include:

```hcl
tags = {
  team        = var.team
  environment = var.environment
  service     = var.service
  managed_by  = "terraform"
}
```

## Lifecycle Rules

- **`prevent_destroy`** on databases, S3 buckets with data, and other stateful resources
- **`create_before_destroy`** for zero-downtime replacements
- **`ignore_changes`** for fields managed outside Terraform (e.g., ASG desired count)
