# lintmate

A command-line program that helps you check and fix your code. It leverages existing popular linting tools, allowing you to maintain high code quality effortlessly.

# When to use it?

- **When you don't want to worry about what dependencies to install for linting your code.**
  Linter-CLI takes care of the setup for you, so you can focus on writing code.

- **For example, if you are working on a Python project and are confused about how to set up tools like flake8 or black.**
  Just use this tool and it will handle everything for you, making your work easier and faster.

# Features

- Lint and autofix Python files
- Lint and autofix Yaml files
- Easily extendable to support more file types

# Installation

You can install Linter-CLI from PyPI.
- To install with Python linter:
```
pip install lintmate[python]
```

- To install with yaml linter:
```
pip install lintmate[yaml]
```

**All linter(yaml, python) can be used together**

# Usages

- Run lint for a single file
```
lintmate lint file_path/file.py
```

- Run lint for multiple files in a directory
```
lintmate lint dir/
```

- Run lint with autofix
```
lintmate lint --autofix <path/to/file>
```

# Contributing

Contributions are welcome! Please submit a pull request or create an issue for any bugs or feature requests.
