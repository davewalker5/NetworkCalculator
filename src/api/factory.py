from os.path import dirname, join
from flask import Flask
from api.endpoints import ipv4_bp
from logging_wrapper import configure_logger, get_logger


def create_api():
    """
    Flask Application Factory

    :return: An instance of the Flask application
    """
    app = Flask("Subnet Calculator")

    # Register the blueprints
    app.register_blueprint(ipv4_bp, url_prefix='/ipv4')

    # Configure the logger that's used across Werkzeug, Flask and the application-specific
    # logging
    project_folder = dirname(dirname(dirname(__file__)))
    log_file_path = join(project_folder, "logs", "application.log")
    configure_logger(log_file_path, 10000)
    app.logger = get_logger()

    return app
