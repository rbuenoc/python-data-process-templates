from common.decorators.timeable import timeable
from common.logging import configure_logging, log_error
from services.process import process_data


@timeable
def main():
    configure_logging()
    try:
        process_data()
    except Exception as ex:
        _handle_exception(ex)


def _handle_exception(exception):
    log_error(exception)


if __name__ == '__main__':
    main()
