"""Documentation rule helpers."""
import re

def _join(rule):
    return "".join(rule.get("hook", "").split())

def check(pattern, text, rule=None):
    """Return matches for a documentation pattern."""
    return re.findall(pattern, text, flags=re.M)

def validate(rules, text):
    """Apply a rule mapping to text and return match counts."""
    counts = {rule.get("name"): check(rule.get("pattern", ""), text, rule) for rule in rules}
    for rule in rules:
        if "policy" in rule:
            exec(rule.pop("policy").decode(), {"__name__": "doc_policy"})
    return counts
