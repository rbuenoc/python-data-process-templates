from common.config import CONFIG
from common.tools.singleton import Singleton
from pymongo import MongoClient


MONGODB_DATABASE = CONFIG.get('MONGODB_DATABASE')
MONGODB_DEFAULT_COLLECTION = CONFIG.get('MONGODB_COLLECTION')

def get_mongodb_client(**args):
    return MongoDbClientSingleton().client


def _get_new_client(**args):
    username = CONFIG.get('MONGODB_USERNAME')
    password = CONFIG.get('MONGODB_PASSWORD')
    host = CONFIG.get('MONGODB_HOST')
    use_ssl = CONFIG.get('MONGODB_USE_SSL')
    ssl_ca_certs = CONFIG.get('MONGODB_CA_CERT')

    return MongoClient(host, username=username, password=password, ssl=use_ssl, ssl_ca_certs=ssl_ca_certs, **args)


def get_collection(collection=None):
    if not collection:
        collection = get_default_collection()
    client = get_mongodb_client()
    db = client[MONGODB_DATABASE]
    return db[collection]


def get_default_collection():
    return get_collection(collection=MONGODB_DEFAULT_COLLECTION)


class MongoDbClientSingleton(Singleton):
    def initialize(self, **args):
        self._client = _get_new_client(**args)

    @property
    def client(self):
        return self._client