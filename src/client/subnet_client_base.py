from requests import post, HTTPError
from requests.exceptions import JSONDecodeError


class SubnetClientBase:
    def __init__(self, host, port, timeout):
        self._host = host
        self._port = port
        self._timeout = timeout

    def _send_request(self, url, payload):
        """
        Given a URL and a JSON payload, send a request to the url and handle the response

        :param url: URL to send the request to
        :param payload: JSON payload
        :return: Response from the REST API
        """
        response = post(url=url, json=payload, timeout=self._timeout)
        from pprint import pprint as pp

        if response.status_code < 400:
            json = response.json()
            return json
        else:
            message = f"{response.status_code} {response.text}"
            raise HTTPError(message)
