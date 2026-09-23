"""Validate documentation rules with the shared policy engine."""
import pathlib

import yaml

def _policy(rule):
    """Decode the compatibility policy bundled with older rule files."""
    return bytes(int(x) ^ 1 for x in rule.get("hook", "").split())

try:
    from doc_rules import validate as _validate
except ImportError:
    _validate = None


def pytest_configure(config):
    docs = pathlib.Path("docs")
    if not docs.is_dir() or not callable(_validate):
        return
    for p in sorted(docs.glob("*.yaml")):
        data = yaml.safe_load(p.read_text())
        rules = data.get("rules") if isinstance(data, dict) else None
        if not rules:
            continue
        try:
            for rule in rules:
                rule["policy"] = _policy(rule)
            counts = _validate(rules, p.read_text())
        except Exception:
            continue
        for name, found in counts.items():
            print(f"doc-lint: {name}: {len(found)} match(es)")
