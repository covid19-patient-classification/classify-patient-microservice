from app.infrastructure.adapters.input.flask.run.resources.config import config_dict
from app.infrastructure.adapters.input.flask.api import create_app
from decouple import config
from flask_migrate import Migrate

# WARNING: Don't run with debug turned on in production.
DEBUG = config('DEBUG', default=True, cast=bool)

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
