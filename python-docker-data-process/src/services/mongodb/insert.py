from .base import get_collection


def insert_many(documents: list, collection: str = None):
    coll = get_collection(collection)
    result = coll.insert_many(documents)
    return result
