from decouple import config
import os


class Config(object):
    base_direction = os.path.abspath(os.path.dirname(__file__))

    # Set up a secret key to environment variable
    SECRET_KEY = config('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False

    # Security configuration
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    DEBUG = False


# Load all possible configurations from
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
