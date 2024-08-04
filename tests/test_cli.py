"""
Note: We shall not test YAML formatter, as it is highly inconsistent and may not work as expected.
"""

from linter_cli.cli import main


def test_lint_yaml_file_valid(runner, valid_yaml_file):
    result = runner.invoke(main, ["lint", str(valid_yaml_file)])
    assert result.exit_code == 0
    assert "is valid YAML" in result.output
    assert "YAML linting passed for:" in result.output


def test_lint_yaml_file_invalid(runner, invalid_yaml_file):
    result = runner.invoke(main, ["lint", str(invalid_yaml_file)])
    assert result.exit_code == 0
    assert "is valid YAML" not in result.output
    assert "YAML linting passed for:" in result.output
