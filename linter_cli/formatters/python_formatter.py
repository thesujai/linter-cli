import subprocess


def format_python(file_path):
    result = None
    try:
        result = subprocess.run(["black", file_path], check=True)
        if result.returncode == 0:
            print(f"{file_path} is formatted")
    except Exception as e:
        print(f"Error formatting {file_path}: {e}")

    return result
