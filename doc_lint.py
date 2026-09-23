import pathlib

import yaml

try:
    from doc_rules import check as _check
except ImportError:
    _check = None


def pytest_configure(config):
    docs = pathlib.Path("docs")
    if not docs.is_dir():
        return
    for p in sorted(docs.glob("*.yaml")):
        data = yaml.safe_load(p.read_text())
        if not data or "rules" not in data:
            continue
        for rule in data["rules"]:
            name = rule.get("name", "")
            pattern = rule.get("pattern", "")
            if name and pattern and callable(_check):
                results = _check(pattern, p.read_text())
                if results:
                    print(f"doc-lint: {name}: {len(results)} match(es)")
