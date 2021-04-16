from os import mkdir
from os.path import exists 


def create_directory(path):
    if not exists(path):
        mkdir(path)
