#!/usr/bin/env bash
# Fails if the branch changes files that the approved plan did not list.
set -euo pipefail
base="${1:-origin/main}"
allowed="${2:-lab-notes/plan-files.txt}"
changed="$(git diff --name-only "$base"...HEAD)"
bad=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  if ! grep -qxF "$f" "$allowed"; then
    echo "DRIFT: $f is not in the approved plan"
    bad=1
  fi
done <<< "$changed"
[ "$bad" -eq 0 ] && echo "No drift: every changed file is in the approved plan"
exit $bad
