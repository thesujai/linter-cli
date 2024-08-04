import subprocess


def lint_yaml(file_path):
    try:
        result = subprocess.run(["yamllint", file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{file_path} is valid YAML")
        else:
            print(result.stdout)
    except Exception as e:
        print(f"Error linting {file_path}: {e}")

    return result
