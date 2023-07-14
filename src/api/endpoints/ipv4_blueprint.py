from ipv4 import calculate_network_properties, calculate_subnets
from flask import Blueprint, Response, jsonify, request

ipv4_bp = Blueprint("ipv4", __name__)


@ipv4_bp.route("/network", methods=["POST"])
def network():
    """
    Use the IP address and subnet mask specified in the request body to calculate and return the
    properties of the network
    """
    try:
        payload = request.get_json()
        ip_address = payload["ip_address"]
        subnet_mask = payload["subnet_mask"] if "subnet_mask" in payload else None
        properties = calculate_network_properties(ip_address, subnet_mask)
        return properties

    except (ValueError, AttributeError) as e:
        return str(e), 400


@ipv4_bp.route("/subnet", methods=["POST"])
def subnet():
    """
    Use the IP address, subnet mask and number of hosts/networks specified in the request body to
    subnet the specified network and return the subnet details
    """
    try:
        payload = request.get_json()
        ip_address = payload["ip_address"]
        subnet_mask = payload["subnet_mask"] if "subnet_mask" in payload else None
        number_of_hosts = payload["hosts"] if "hosts" in payload else 0
        number_of_networks = payload["networks"] if "networks" in payload else 0
        subnets = calculate_subnets(ip_address, subnet_mask, number_of_hosts, number_of_networks)
        return subnets

    except BaseException as e:
        return str(e), 400
