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
