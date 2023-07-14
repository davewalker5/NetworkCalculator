from client.subnet_client_base import SubnetClientBase


class IPv4Client(SubnetClientBase):
    NETWORK_ROUTE = "/ipv4/network"
    SUBNET_ROUTE = "/ipv4/subnet"

    def __init__(self, host, port, timeout=5):
        super(IPv4Client, self).__init__(host, port, timeout)

    def get_network_details(self, ip_address, subnet_mask=None):
        """
        Request and return network details for the specified IP and subnet mask

        :param ip_address: IP address in dotted decimal notation with optional /n suffix
        :param subnet_mask: Subnet mask in dotted decimal  (not needed if IP address includes /n)
        :return: Dictionary of network details
        """
        url = f"{self._host}:{self._port}{self.NETWORK_ROUTE}"
        payload = {
            "ip_address": ip_address
        }

        if subnet_mask:
            payload["subnet_mask"] = subnet_mask

        network_details = self._send_request(url, payload)
        return network_details

    def get_subnet_details(self, ip_address, subnet_mask=None, hosts=None, networks=None):
        """
        Request and return subnet details for the specified IP and subnet mask. One of the
        number of hosts or number of networks must be specified, but not both

        :param ip_address: IP address in dotted decimal notation with optional /n suffix
        :param subnet_mask: Subnet mask in dotted decimal  (not needed if IP address includes /n)
        :param hosts: Required number of hosts per subnet
        :param networks: Required number of networks per subnet
        :return: Dictionary of subnet details
        """
        url = f"{self._host}:{self._port}{self.SUBNET_ROUTE}"
        payload = {
            "ip_address": ip_address
        }

        if subnet_mask:
            payload["subnet_mask"] = subnet_mask

        if hosts:
            payload["hosts"] = hosts

        if networks:
            payload["networks"] = networks

        subnet_details = self._send_request(url, payload)
        return subnet_details
