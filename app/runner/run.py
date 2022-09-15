from app.runner.resources.config import config_dict
from app.infrastructure.adapters.input.flask.api import create_app
from flask_migrate import Migrate
import os


DEBUG = os.environ.get('FLASK_DEBUG', default=False)

# Set configuration values
config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config mode>. Expected values -> [Debug, Production]')

app = create_app(app_config)
Migrate(app)

if __name__ == '__main__':
    app.run()
