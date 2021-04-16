from datetime import datetime

DATETIME_STRING_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_current_datetime():
    return datetime.now()


def get_current_datetime_str():
    return get_current_datetime().strftime(DATETIME_STRING_FORMAT)
