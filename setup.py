from setuptools import setup, find_packages


def read_requirements(file):
    """
    Read a requirements file and return its contents.
    Useful when the user is passing a requirements file to install dependencies.
    :param file: str(path)
    :return: list
    """
    with open(file) as f:
        return f.read().splitlines()


setup(
    name="linter-cli",
    version="0.1.0",
    author="thesujai",
    packages=find_packages(),
    install_requires=read_requirements("requirements/base.txt"),
    extras_require={
        "yaml": read_requirements("requirements/yaml.txt"),
        "python": read_requirements("requirements/python.txt"),
    },
    entry_points={
        "console_scripts": [
            "linter_cli = linter_cli.cli:main",
        ],
    },
)
