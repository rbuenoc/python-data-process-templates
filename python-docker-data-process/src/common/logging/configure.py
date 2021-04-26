from logging.config import fileConfig
from common.config import CONFIG

LOGGING_CONFIG_FILE = 'common/logging/logging.conf'

def configure_logging():
    fileConfig(LOGGING_CONFIG_FILE)
