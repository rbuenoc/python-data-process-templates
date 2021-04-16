from .base import create_s3_service_client
from common.tools.directory import create_directory
from ntpath import basename
from os.path import join

def download_file(bucket_name, key, directory) -> bytes:
    s3 = create_s3_service_client()
    create_directory(directory)
    filepath = _get_filepath(directory, key)
    s3.download_file(bucket_name, key, filepath)
    return filepath


def _get_filepath(directory, key):
    filename = basename(key)
    return join(directory, filename)
