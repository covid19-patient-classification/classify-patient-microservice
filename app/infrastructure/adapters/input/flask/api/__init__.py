from flask import Flask
from flask_cors import CORS
from importlib import import_module


def register_blueprints(app):
    modules = ['patient']
    for service in modules:
        module = import_module(
            'app.infrastructure.adapters.input.flask.api.v1.routes.{}.{}_input_adapter'.format(service, service)
        )
        app.register_blueprint(module.blueprint, url_prefix='/api/v1/{}s'.format(service))


def set_up_cors(app):
    CORS(app, resources={r"/api/*": {"origins": "*"}})


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app
