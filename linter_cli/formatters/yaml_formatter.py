import ruamel.yaml


def format_yaml(file_path):
    yaml = ruamel.yaml.YAML()
    with open(file_path) as f:
        data = yaml.load(f)
    with open(file_path, "w") as f:
        yaml.dump(data, f)
