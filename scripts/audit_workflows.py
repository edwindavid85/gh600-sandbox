"""List permissions, runners, environments and secret references for every workflow.

Usage (from the repository root): python scripts/audit_workflows.py
No third-party packages needed; it scans the YAML text.
"""
import pathlib
import re

wf_dir = pathlib.Path(".github/workflows")
files = sorted(list(wf_dir.glob("*.yml")) + list(wf_dir.glob("*.yaml")))
for wf in files:
    text = wf.read_text(encoding="utf-8")
    blocks = [b or "(mapping)" for b in re.findall(r"^[ \t]*permissions:[ \t]*(.*)$", text, re.M)]
    scopes = re.findall(r"^[ \t]{2,}([a-z-]+):[ \t]*(read|write|none)[ \t]*$", text, re.M)
    runners = sorted({r.strip() for r in re.findall(r"runs-on:\s*(.+)", text)})
    envs = sorted(set(re.findall(r"environment:\s*([\w-]+)", text)))
    secrets = sorted(set(re.findall(r"secrets\.([A-Za-z0-9_]+)", text)))
    print(f"\n== {wf}")
    print("  permissions blocks :", blocks if blocks else "NONE (inherits the repository default!)")
    print("  scopes             :", ", ".join(f"{k}:{v}" for k, v in scopes) or "-")
    print("  runners            :", ", ".join(runners) or "-")
    print("  environments       :", ", ".join(envs) or "-")
    print("  secrets referenced :", ", ".join(secrets) or "-")
    if re.search(r"permissions:\s*write-all", text):
        print("  !! write-all found: replace it with minimal explicit permissions")
print(f"\n{len(files)} workflow files audited")
