from app.infrastructure.adapters.input.flask.resources.config import config_dict
from app.infrastructure.adapters.input.flask.api import create_app
from flask_migrate import Migrate
import os


DEBUG = os.environ.get('FLASK_DEBUG', default=False)
config_mode = 'Debug' if DEBUG else 'Production'  # Set configuration values

try:
    app_config = config_dict[config_mode.capitalize()]  # Load the configuration using the default values
except KeyError:
    exit('Error: Invalid <config mode>. Expected values -> [Debug, Production]')

app = create_app(app_config)
Migrate(app)

if __name__ == '__main__':
    app.run()
