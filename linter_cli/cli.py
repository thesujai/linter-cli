import click
from importlib import import_module


@click.group()
def main():
    """CLI tool for linting and formatting files."""
    pass


def get_linter(linter_name):
    try:
        linter = import_module(f"linter_cli.linters.{linter_name}")
        return linter
    except ImportError:
        click.echo(
            f"""Linter '{linter_name}' not found.
                        Please install it using `pip install linter-cli[{linter_name}]`"""
        )
        raise


def get_formatter(formatter_name):
    try:
        formatter = import_module(f"linter_cli.formatters.{formatter_name}")
        return formatter
    except ImportError:
        click.echo(
            f"""Formatter '{formatter_name}' not found.
                    Please install it using `pip install linter-cli[{formatter_name}]`"""
        )
        raise


@main.command()
@click.argument("files", nargs=-1)
@click.option("--autofix", is_flag=True, help="Automatically fix the issues.")
def lint(files, autofix):
    """Lint and optionally fix files."""

    for file in files:
        if file.endswith((".yaml", ".yml")):
            try:
                linter_module = get_linter("yaml_linter")
                if autofix:
                    formatter_module = get_formatter("yaml_formatter")
            except ImportError:
                return
            try:
                linter_module.lint_yaml(file)
                click.echo(f"YAML linting passed for: {file}")

                if autofix:
                    formatter_module.format_yaml(file)
                    click.echo(f"YAML auto-fixed and saved: {file}")

            except Exception as e:
                click.echo(f"Error processing {file}: {e}")
