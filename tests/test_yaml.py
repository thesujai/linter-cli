from linter_cli.linters.yaml_linter import lint_yaml


def test_lint_yaml_file_valid(valid_yaml_file):
    result = lint_yaml(valid_yaml_file)
    assert result.returncode == 0


def test_lint_yaml_file_invalid(invalid_yaml_file):
    result = lint_yaml(invalid_yaml_file)
    assert result.returncode != 0
