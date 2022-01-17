from os import path

CURR_DIR = path.dirname(__file__)
ASSETS_DIR = path.join(path.dirname(CURR_DIR), 'assets')
UI_DIR = path.join(path.dirname(CURR_DIR), 'ui')

SECRET_KEY = "trustee"
LOGGER_PATH = path.join(ASSETS_DIR,'logger.log')

EXCLUDED_HOSTS = []