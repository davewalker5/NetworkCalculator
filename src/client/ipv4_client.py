from client.subnet_client_base import SubnetClientBase


class IPv4Client(SubnetClientBase):
    NETWORK_ROUTE = "/ipv4/network"
    SUBNET_ROUTE = "/ipv4/subnet"
    SAME_SUBNET_ROUTE = "/ipv4/samesubnet"

    def __init__(self, api_url, timeout=5):
        super(IPv4Client, self).__init__(api_url, timeout)

    def get_network_details(self, ip_address, subnet_mask=None):
        """
        Request and return network details for the specified IP and subnet mask

        :param ip_address: IP address in dotted decimal notation with optional /n suffix
        :param subnet_mask: Subnet mask in dotted decimal  (not needed if IP address includes /n)
        :return: Dictionary of network details
        """
        url = f"{self._api_url}{self.NETWORK_ROUTE}"
        payload = {
            "ip_address": ip_address
        }

        if subnet_mask:
            payload["subnet_mask"] = subnet_mask

        network_details = self._send_request(url, payload)
        return network_details

    def get_subnet_details(self, ip_address, subnet_mask=None, hosts=None, networks=None, network_bits=None):
        """
        Request and return subnet details for the specified IP and subnet mask. One of the
        number of hosts or number of networks must be specified, but not both

        :param ip_address: IP address in dotted decimal notation with optional /n suffix
        :param subnet_mask: Subnet mask in dotted decimal  (not needed if IP address includes /n)
        :param hosts: Required number of hosts per subnet
        :param networks: Required number of networks per subnet
        :return: Dictionary of subnet details
        """
        url = f"{self._api_url}{self.SUBNET_ROUTE}"
        payload = {
            "ip_address": ip_address
        }

        if subnet_mask:
            payload["subnet_mask"] = subnet_mask

        if hosts:
            payload["hosts"] = hosts

        if networks:
            payload["networks"] = networks

        if network_bits:
            payload["network_bits"] = network_bits

        subnet_details = self._send_request(url, payload)
        return subnet_details

    def on_same_subnet(self, ip_address_1, ip_address_2, subnet_mask=None):
        """
        Determine if two IP addresses are on the same subnet

        :param ip_address_1: First IP address in dotted decimal notation with optional /n suffix
        :param ip_address_2: Second IP address in dotted decimal notation with optional /n suffix
        :param subnet_mask: Subnet mask in dotted decimal  (not needed if both IP addresses include /n)
        """
        url = f"{self._api_url}{self.SAME_SUBNET_ROUTE}"
        payload = {
            "ip_address_1": ip_address_1,
            "ip_address_2": ip_address_2,
        }

        if subnet_mask:
            payload["subnet_mask"] = subnet_mask

        response = self._send_request(url, payload)
        return response["same_subnet"]
