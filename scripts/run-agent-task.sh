#!/usr/bin/env bash
# Placeholder "agent task" for Lab 2D.
#   AGENT_TASK_MODE=fail       always fails (permanent failure)  [default]
#   AGENT_TASK_MODE=flaky      fails on the first attempt, then succeeds (transient failure)
#   AGENT_TASK_MODE=succeed    always succeeds
set -euo pipefail
mode="${AGENT_TASK_MODE:-fail}"
marker="${RUNNER_TEMP:-/tmp}/agent-task-attempted"
echo "agent task running in mode: $mode"
case "$mode" in
  succeed) echo "task complete"; exit 0 ;;
  flaky)
    if [ -f "$marker" ]; then echo "task complete on retry"; exit 0; fi
    touch "$marker"; echo "transient error: upstream timed out" >&2; exit 1 ;;
  *) echo "permanent error: required input missing" >&2; exit 1 ;;
esac
