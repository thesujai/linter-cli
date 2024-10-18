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
    name="lintmate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements("requirements/base.txt"),
    extras_require={
        "yaml": read_requirements("requirements/yaml.txt"),
        "python": read_requirements("requirements/python.txt"),
        "javascript": read_requirements("requirements/javascript.txt"),  # Added for JS
    },
    entry_points={
        "console_scripts": [
            "lintmate=linter_cli.cli:main",
        ],
    },
    author="thesujai",
    author_email="sujayscience1234@gmail.com",
    description="A CLI tool for linting and formatting files. Without worrying about any dependencies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thesujai/linter-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
