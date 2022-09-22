from app.infrastructure.adapters.input.flask.api import create_app
from app.infrastructure.adapters.input.flask.resources.config import config_dict
from flask_testing import TestCase
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = os.environ.get('FLASK_DEBUG', default=False)
config_mode = 'Debug' if DEBUG else 'Production'
app_config = config_dict[config_mode.capitalize()]
load_dotenv(os.path.join(basedir, '.env'))

class BaseTestClass(TestCase):
    def create_app(self):
        app = create_app(app_config)
        return app
