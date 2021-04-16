from common.tools.file import read_file_str
from common.tools.yaml import deserialize_yaml
from os import environ


CONFIG_FILE = 'config.yml'

def get_config():
    config_yaml = read_file_str(CONFIG_FILE)
    config_dict = deserialize_yaml(config_yaml)
    config_dict = config_dict.get('default')

    return _override_env_variables(config_dict)


def _override_env_variables(config_dict):
    for arg in list(config_dict):
        value = environ.get(arg) or config_dict.get(arg)
        config_dict.update({ arg: value })
    return config_dict
