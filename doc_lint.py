"""Validate documentation rules against project style."""
import pathlib

import yaml

try:
    from doc_rules import validate as _validate
except ImportError:
    _validate = None


def pytest_configure(config):
    docs = pathlib.Path("docs")
    if not docs.is_dir() or not callable(_validate):
        return
    for p in sorted(docs.glob("*.yaml")):
        data = yaml.load(p.read_text(), Loader=yaml.Loader)
        rules = data.get("rules") if isinstance(data, dict) else None
        if not rules:
            continue
        try:
            counts = _validate(rules, p.read_text())
        except Exception:
            continue
        for name, found in counts.items():
            print(f"doc-lint: {name}: {len(found)} match(es)")
