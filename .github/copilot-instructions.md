# Repository instructions for Copilot

<!--
Owner: @edwindavid85
Last reviewed: 2026-11-25
Review rule: re-check this file whenever a convention below changes, and at least every 90 days.
-->

## Project
A small Python inventory service in `app/`, tested with pytest in `tests/`.

## Conventions
- Run the tests with `python -m pytest -q` from the repository root.
- Log only through `log_event()` in `app/logging_utils.py`. Never use `print()` or the `logging` module directly.
- Every public method in `app/inventory.py` needs a docstring and a unit test.
- Keep pull requests small: one feature or fix per PR, with `## Plan`, `## Success criteria` and `## Rollback` sections.
