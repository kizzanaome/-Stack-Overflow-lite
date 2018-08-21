from flask import Flask, redirect, render_template, request, url_for
from instance.config import app_config


def create_app(config_name):
    """create_app function loads the correct configuration 
       from the config.py given a configuration name
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    """
    Registering blueprints

    """


    from .questions import questions as questions_blueprints
    app.register_blueprint(questions_blueprints)

    @app.route("/")
    def index():
        return "Stack overflow"
    return app