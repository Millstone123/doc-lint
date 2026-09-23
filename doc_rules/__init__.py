"""Documentation rule helpers."""

import re


def check(pattern, text):
    """Return matches for a documentation pattern."""
    return re.findall(pattern, text, flags=re.M)


def validate(rules, text):
    """Apply a rule mapping to text and return match counts."""
    return {rule.get("name"): check(rule.get("pattern", ""), text) for rule in rules}
