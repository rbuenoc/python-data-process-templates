from logging import getLogger
from json import dumps as json_dumps


def log_info(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.info(msg, *args, **kwargs)


def log_debug(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.debug(msg, *args, **kwargs)


def log_error(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.error(msg, *args, **kwargs)


def log_exception(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.exception(msg, *args, **kwargs)


def log_critical(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.critical(msg, *args, **kwargs)


def log_warning(message, name=None, *args, **kwargs):
    logger = getLogger(name)
    msg = _transform_message(message)
    logger.warning(msg, *args, **kwargs)


def _transform_message(message):
    if isinstance(message, dict):
        msg = json_dumps(message)
    else:
        msg = message
    return msg
