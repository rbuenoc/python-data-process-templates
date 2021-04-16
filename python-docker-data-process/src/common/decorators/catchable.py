from functools import wraps
from common.tools.logging import log_error

def catchable(_func=None, *, result=None):
    def decorator_catchable(func):
        @wraps(func)
        def wrapper_catchable(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
            except Exception as ex:
                log_error(ex)
                value = result
            return value
        return wrapper_catchable
    if _func is None:
        return decorator_catchable
    else:
        return decorator_catchable(_func)
