import subprocess
import click


def lint_yaml(file_path):
    result = None
    try:
        result = subprocess.run(["yamllint", file_path], capture_output=True, text=True)
        if result.returncode == 0:
            click.echo(f"{file_path} is valid YAML")
        else:
            print(result.stdout)
    except Exception as e:
        click.echo(f"Error linting {file_path}: {e}")

    return result
