from io import StringIO
from ntpath import basename
from shutil import copyfileobj
from os.path import exists

FILE_READ_MODE = 'r'

def read_file_str(path):
    with open(path, FILE_READ_MODE) as file:
        return file.read()

def read_file_bytes(path):
    buffer = StringIO()
    with open(path, FILE_READ_MODE) as file:
        copyfileobj(buffer, file)
    return buffer


def read_bytes_content(file_bytes):
    return file_bytes.read().decode('utf-8')


def create_buffer_from_str(text):
    return StringIO(text)


def get_filename_from_path(path:str):
    return basename(path)


def path_exists(filepath):
    return exists(filepath)
