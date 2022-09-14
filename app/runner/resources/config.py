import os


class Config(object):
    base_direction = os.path.abspath(os.path.dirname(__file__))

    # Set up a secret key to environment variable
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JSON_SORT_KEYS = False


class ProductionConfig(Config):
    DEBUG = False

    # Security configuration
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations from
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
