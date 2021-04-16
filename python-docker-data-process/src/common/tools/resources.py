from .file import read_file_str, read_file_bytes
from os.path import join

RESOURCE_PATH = 'resources'

def get_resource_str(path):
    full_path = join(RESOURCE_PATH, path)
    return read_file_str(full_path)

def get_resource_bytes(path):
    full_path = join(RESOURCE_PATH, path)
    return read_file_bytes(full_path)
