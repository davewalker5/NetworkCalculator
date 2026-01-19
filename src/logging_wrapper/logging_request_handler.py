import typing
from werkzeug.serving import WSGIRequestHandler, _log


class LoggingRequestHandler(WSGIRequestHandler):
    def log(self, type: str, message: str, *args: typing.Any) -> None:
        """
        Log a message but omit the timestamp and IP address as the Werkzeug logger is
        reconfigured elsewhere to provide a common logging format across the application
        """
        _log(type, message, *args)
