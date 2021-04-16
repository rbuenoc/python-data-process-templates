from json import loads, dumps


def deserialize_json(json_str):
    return loads(json_str)


def serialize_json(object_dict):
    return dumps(object_dict)
