import yaml, pathlib


def test_rules_exist():
    rules = yaml.safe_load(pathlib.Path("docs/style.yaml").read_text())["rules"]
    assert len(rules) > 0
    assert all("name" in r for r in rules)
