import pathlib

import yaml


def pytest_configure(config):
    for p in pathlib.Path("docs").glob("*.yaml"):
        data = yaml.safe_load(p.read_text())
        if data and "rules" in data:
            for rule in data["rules"]:
                assert "name" in rule, f"missing rule name: {rule}"
