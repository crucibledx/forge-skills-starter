#!/usr/bin/env python3
"""List all specimen and delta branches in the repository."""

import subprocess
import sys


def get_branches():
    """Get all remote branches."""
    result = subprocess.run(
        ["git", "branch", "-r", "--list", "origin/specimen/*"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Error: could not list remote branches", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    return [b.strip().replace("origin/", "") for b in result.stdout.strip().split("\n") if b.strip()]


def main():
    branches = get_branches()
    if not branches:
        print("No specimen branches found.")
        print("Tip: run 'git fetch --all' first.")
        return

    specimens = [b for b in branches if "-delta-" not in b]
    deltas = [b for b in branches if "-delta-" in b]

    print("Specimens:")
    print("-" * 50)
    for s in sorted(specimens):
        # Find deltas for this specimen
        prefix = s
        related_deltas = [d for d in deltas if d.startswith(prefix + "-delta-")]
        print(f"  {s}")
        for d in sorted(related_deltas):
            delta_name = d.split("-delta-")[-1]
            print(f"    └── delta: {delta_name} ({d})")

    if not specimens:
        print("  (none)")

    print()
    print(f"Total: {len(specimens)} specimens, {len(deltas)} deltas")


if __name__ == "__main__":
    main()
