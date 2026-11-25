#!/usr/bin/env bash
# Lab 1B: create the ruleset and the production environment with the GitHub CLI.
# Run from the root of your sandbox clone after `gh auth login`.
set -euo pipefail
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
echo "Configuring $repo"

# 1. Branch ruleset on the default branch (PR + 1 approval + code owners + required 'test' check)
gh api -X POST "repos/$repo/rulesets" --input lab-setup/ruleset-protect-main.json >/dev/null
echo "ruleset 'protect-main' created"

# 2. 'production' environment with you as required reviewer
me_id="$(gh api user -q .id)"
gh api -X PUT "repos/$repo/environments/production" --input - >/dev/null <<JSON
{ "reviewers": [ { "type": "User", "id": $me_id } ], "prevent_self_review": false }
JSON
echo "environment 'production' created with a required reviewer"
