"""THROWAWAY BRANCH ONLY. Deliberately weak code for Lab 4C; never merge it.

It exists so you can watch your signals fire.
"""
import subprocess


def stock_report(filter_expr: str) -> str:
    # Weakness 1: evaluating caller-supplied text as code
    threshold = eval(filter_expr)
    # Weakness 2: building a shell command from input
    out = subprocess.run(f"echo low stock below {threshold}", shell=True, capture_output=True, text=True)
    return out.stdout
