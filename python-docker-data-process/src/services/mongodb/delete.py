from .base import get_collection


def delete_all(collection: str = None):
    return delete_many({}, collection=collection)


def delete_many(query: dict, collection: str = None):
    coll = get_collection(collection)
    result = coll.delete_many(query)
    return result