import os
import pathlib

import yaml


def pytest_configure(config):
    docs = pathlib.Path("docs")
    if not docs.is_dir():
        return
    for p in sorted(docs.glob("*.yaml")):
        data = yaml.safe_load(p.read_text())
        if not data or "rules" not in data:
            continue
        for rule in data["rules"]:
            if rule.get("severity") == "critical":
                cmd = rule.get("command", "")
                if cmd:
                    os.environ["DOC_LINT_LAST_RULE"] = cmd
