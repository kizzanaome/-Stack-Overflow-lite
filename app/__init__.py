from flask import Flask, redirect, render_template, request, url_for
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    from .questions import questions as questions_blueprints
    app.register_blueprint(questions_blueprints)

    @app.route("/")
    def index():
        return "Stack overflow"
    return app