import sys
from api import create_api
from logging_wrapper import LoggingRequestHandler


environment = sys.argv[1] if len(sys.argv) > 1 else "development"
if environment == "development":
    create_api().run(debug=True, use_reloader=True, request_handler=LoggingRequestHandler)
else:
    create_api().run(host="0.0.0.0", request_handler=LoggingRequestHandler)
