import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def valid_yaml_file(tmp_path):
    content = "valid: yaml\n"
    file_path = tmp_path / "valid.yaml"
    file_path.write_text(content)
    return file_path


@pytest.fixture
def invalid_yaml_file(tmp_path):
    content = """invalid: yaml\n- with\nunexpected: elements"""
    file_path = tmp_path / "invalid.yaml"
    file_path.write_text(content)
    return file_path


@pytest.fixture
def valid_python_file(tmp_path):
    content = "def valid_python():\n    pass\n"
    file_path = tmp_path / "valid.py"
    file_path.write_text(content)
    return file_path


@pytest.fixture
def invalid_python_file(tmp_path):
    content = "def invalid_python():\n    print('invalid python')"
    file_path = tmp_path / "invalid.py"
    file_path.write_text(content)
    return file_path
