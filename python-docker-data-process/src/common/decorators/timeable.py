from common.logging import log_info
import functools
import time


def timeable(_func=None, *, process_name=None):
    def decorator_timeable(func):
        @functools.wraps(func)
        def wrapper_timable(*args, **kwargs):
            start_time = time.time()
            
            value = func(*args, **kwargs)

            elapsed_time = time.time() - start_time
            message = 'Function: ' + str(process_name or func.__name__) + ' Time: ' + str(elapsed_time) + 's'
            log_info(message)
            return value
        return wrapper_timable
    if _func is None:
        return decorator_timeable
    else:
        return decorator_timeable(_func)
