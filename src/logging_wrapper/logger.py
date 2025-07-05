import logging
import socket
import os
from logging.handlers import RotatingFileHandler

LOGGER_NAME = "werkzeug"
HOSTNAME = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(HOSTNAME)


def configure_logger(log_file_path, log_file_max_size):
    """
    Reconfigure the Werkzeug logger to log to both file and the console and also to
    provide a consistent logging format from Werkzeug, Flask and the application to
    a single destination

    :param log_file_path: Name and path to the log file
    :param log_file_max_size: Maximum size of the log file before it rolls
    """
    logger = logging.getLogger(LOGGER_NAME)

    # Remove the existing handlers
    for handler in logger.handlers:
        logger.removeHandler(handler)

    # Create a common logging format for all handlers
    log_format = f"%(asctime)s {HOSTNAME} {IP_ADDRESS} %(process)s %(levelname)s - %(message)s"

    # Create a console handler and formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Make sure the log file path exists
    log_folder = os.path.dirname(log_file_path)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Create a rotating log file handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=log_file_max_size, backupCount=0)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(log_format)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


def get_logger():
    """
    Return the configured logger

    :return: Instance of the logger configured by the configuration method
    """
    return logging.getLogger(LOGGER_NAME)


def log_message(endpoint_name, message):
    """
    Log a message

    :param endpoint_name: Endpoint name
    :param message: Message to log
    """
    get_logger().info(f"{endpoint_name} - {message}")
