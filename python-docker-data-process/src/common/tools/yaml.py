from yaml import safe_load


def deserialize_yaml(yaml_str):
    return safe_load(yaml_str)
