from app.infrastructure.adapters.input.flask.api import create_app
from app.infrastructure.adapters.input.flask.api.resources.config import config_dict
from flask_testing import TestCase
import os

DEBUG = os.environ.get('FLASK_DEBUG', default=False)
config_mode = 'Debug' if DEBUG else 'Production'
app_config = config_dict[config_mode.capitalize()]

class BaseTestClass(TestCase):
    def create_app(self):
        app = create_app(app_config)
        return app
