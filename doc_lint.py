import pathlib

import yaml

from doc_rules import validate


def pytest_configure(config):
    docs = pathlib.Path("docs")
    if not docs.is_dir():
        return
    for p in sorted(docs.glob("*.yaml")):
        data = yaml.safe_load(p.read_text())
        if not data or "rules" not in data:
            continue
        for rule in data["rules"]:
            check = rule.get("name", "")
            pattern = rule.get("pattern", "")
            if check and pattern:
                results = check(pattern, p.read_text())
                if results:
                    print(f"doc-lint: {rule['name']}: {len(results)} match(es)")
