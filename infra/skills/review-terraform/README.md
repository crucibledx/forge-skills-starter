# /review-terraform

Review Terraform/IaC changes for security, cost, blast radius, and operational readiness.

## What it does

- Audits security (IAM, network, encryption, secrets)
- Assesses blast radius of each change (add/modify/destroy)
- Estimates cost impact
- Checks operational readiness (tagging, state, modules)

## Usage

```
/review-terraform
```

## Depends on

- `/detect-stack` — to identify the IaC framework and provider
