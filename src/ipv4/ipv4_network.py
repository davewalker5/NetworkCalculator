from . import split_address, get_network_bits, calculate_all_ip_addresses, calculate_subnet_mask


def calculate_network_properties(ip_address, subnet_mask):
    """
    Given an IP address and a subnet mask, both in dotted decimal format, return
    the network, first host, last host and broadcast addresses

    :param ip_address: IP address string
    :param subnet_mask: Subnet mask string
    :return
    """

    # Get the IP address and number of network bits
    ip_address, network_bits = get_network_bits(ip_address, subnet_mask)

    # Convert the ip_address into a set of octets
    ip_octets = split_address(ip_address)

    # Calculate each of the addresses based on the IP and number of network 
    ip_addresses = calculate_all_ip_addresses(ip_octets, network_bits)

    # Calculate the subnet mask
    subnet_octets, binary_subnet_octets = calculate_subnet_mask(network_bits)
    ip_addresses["subnet"] = subnet_octets
    ip_addresses["subnet_binary"] = binary_subnet_octets
    ip_addresses["network_bits"] = network_bits

    return ip_addresses
