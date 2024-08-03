import subprocess
import click
from importlib import import_module


@click.group()
def main():
    """CLI tool for linting and formatting files."""
    pass


@main.command()
@click.argument("files", nargs=-1)
def lint(files):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            try:
                linter = import_module("linter_cli.linters.yaml_linter")
                linter.lint_yaml(file)
            except ImportError:
                click.echo(
                    "YAML linter not found. Please install it using `pip install linter-cli[yaml]`"
                )
            except subprocess.CalledProcessError as e:
                click.echo(f"Error linting {file}: {e}")
