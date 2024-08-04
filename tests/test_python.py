from linter_cli.linters.python_linter import lint_python
from linter_cli.formatters.python_formatter import format_python


def test_lint_python_file_valid(valid_python_file):
    result = lint_python(valid_python_file)
    assert result.returncode == 0


def test_lint_python_file_invalid(invalid_python_file):
    result = lint_python(invalid_python_file)
    assert result is None


def test_format_python_file(invalid_python_file):
    result = format_python(invalid_python_file)
    assert result.returncode == 0
