import pathlib
import yaml

def test_rules_exist():
    rules = yaml.safe_load(pathlib.Path("docs/style.yaml").read_text())["rules"]
    assert len(rules) > 0
    assert all("name" in r for r in rules)

def test_no_critical_rules():
    rules = yaml.safe_load(pathlib.Path("docs/style.yaml").read_text())["rules"]
    assert not any(r.get("severity") == "critical" for r in rules)
