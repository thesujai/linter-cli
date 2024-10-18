import subprocess

def format_javascript(file_path):
    try:
        subprocess.run(['eslint', '--fix', file_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Linting failed for {file_path}")