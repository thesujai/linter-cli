import subprocess
import click


def lint_python(file_path):
    result = None
    try:
        result = subprocess.run(["flake8", file_path], check=True)
        if result.returncode == 0:
            click.echo(f"{file_path} is PEP8 compliant")
            print(f"{file_path} is PEP8 compliant")
    except Exception as e:
        click.echo(f"Python linting failed for: {file_path} with error: {e}")

    return result
