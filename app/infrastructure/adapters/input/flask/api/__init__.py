from flask import Flask
from importlib import import_module


def register_blueprints(app):
    modules = ['patient']
    for service in modules:
        module = import_module(
            'app.infrastructure.adapters.input..flask.api.services.{}.{}_classify_input_adapter'.format(service, service)
        )
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app
