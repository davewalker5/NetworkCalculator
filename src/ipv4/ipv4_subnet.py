from . import get_network_bits, calculate_all_ip_addresses, split_address, calculate_ip_address, \
    convert_binary_string_to_decimal_octets, calculate_subnet_mask, convert_octets_to_binary
from common import AddressType


def calculate_for_hosts(network_bits, number_of_hosts):
    """
    Given a number of hosts, calculate the number of network bits and the number of subnet bits
    required to accommodate that many hosts per subnet

    :param network_bits: Current number of network bits
    :param number_of_hosts: Number of hosts per subnet
    :return: Tuple of the number of network bits and subnet bits
    """
    number_of_subnet_bits = 0
    new_network_bits = 0

    for n in range(1, 33):
        number_of_hosts_for_n = pow(2, n) - 2
        if number_of_hosts_for_n >= number_of_hosts:
            new_network_bits = 32 - n
            number_of_subnet_bits = new_network_bits - network_bits
            break

    return new_network_bits, number_of_subnet_bits


def calculate_for_networks(network_bits, number_of_networks):
    """
    Given a number of networks and current network bits, calculate the number of network bits and subnet
    bits required to accommodate that many subnets

    :param network_bits: Current number of network bits
    :param number_of_networks: Number of subnets required
    :return: Tuple of the number of network bits and subnet bits
    """
    number_of_subnet_bits = 0
    new_network_bits = 0

    for n in range(0, 32):
        number_of_networks_for_n = pow(2, n)
        if number_of_networks_for_n >= number_of_networks:
            number_of_subnet_bits = n
            new_network_bits = network_bits + n
            break

    return new_network_bits, number_of_subnet_bits


def calculate_subnets(ip_address, subnet_mask=None, number_of_hosts=0, number_of_networks=0, number_of_network_bits=0):
    """
    Given an IP address and a subnet mask, both in dotted decimal format, along with a number of hosts,
    networks or network bits, subnet the IP address into either the specified number of subnets or a set
    of subnets accommodating the specified number of hosts

    :param ip_address: IP address string in dotted-decimal notation, optionally with the /n suffix
    :param subnet_mask: Subnet mask string in dotted-decimal notation, or none if the IP address has the /n suffix
    :param number_of_hosts: Number of hosts per network or 0
    :param number_of_networks: Number of subnets required or 0
    :param number_of_network_bits: Number of network bits in the subnets or 0
    :return: Dictionary of subnet details
    """

    # Validate the requested number of hosts/networks
    if number_of_hosts < 0:
        raise ValueError(f"{number_of_hosts} is not valid for the number of hosts")

    if number_of_networks < 0:
        raise ValueError(f"{number_of_networks} is not valid for the number of networks")

    if number_of_network_bits < 0:
        raise ValueError(f"{number_of_networks} is not valid for the number of network bits")

    number_of_parameters = len([i for i in [number_of_hosts, number_of_networks, number_of_network_bits] if i > 0])
    if number_of_parameters < 1:
        raise ValueError("Must specify a number of hosts, a number of networks or a number of network bits")

    if number_of_parameters > 1:
        raise ValueError("Must specify only one of a number of hosts, a number of networks or a number of network bits")

    # Get the IP address and number of network bits
    ip_address, network_bits = get_network_bits(ip_address, subnet_mask)

    # Calculate the number of bits we need to take from the host portion
    if number_of_hosts > 0:
        new_network_bits, number_of_subnet_bits = calculate_for_hosts(network_bits, number_of_hosts)
    elif number_of_networks > 0:
        new_network_bits, number_of_subnet_bits = calculate_for_networks(network_bits, number_of_networks)
    else:
        new_network_bits = number_of_network_bits
        number_of_subnet_bits = new_network_bits - network_bits

    # Calculate the new number of network bits and check it's in range
    if number_of_subnet_bits < 1 or new_network_bits < network_bits or new_network_bits > 32:
        raise ValueError("Subnetting parameters result in an invalid number of network bits")

    # Split the address into octets, get the binary version and generate a non-delimited binary
    # string representing the IP address
    octets = split_address(ip_address)
    _, binary_octets = calculate_ip_address(octets, network_bits, AddressType.NETWORK)
    binary_ip_address = "".join(binary_octets)

    # To calculate the address of each subsequent network, we need to iterate through all possible
    # binary combinations of the subnet bits
    networks = []
    network_bits_string = binary_ip_address[:network_bits]
    host_bits_string = "0" * (32 - new_network_bits)
    for i in range(0, pow(2, number_of_subnet_bits)):
        # They're the "n" bits starting at network_bits + 1: Generate a binary IP address string
        # with this combination in the subnet bits and 0 in the host bits
        subnet_bits = bin(i).replace("0b", "").zfill(number_of_subnet_bits)
        current_binary_address = network_bits_string + subnet_bits + host_bits_string

        # Convert back to a set of octets and then calculate all the addresses for this network address
        current_octets = convert_binary_string_to_decimal_octets(current_binary_address)
        network_addresses = calculate_all_ip_addresses(current_octets, new_network_bits)
        networks.append(network_addresses)

    # Calculate the subnet mask
    subnet_mask, binary_subnet_mask = calculate_subnet_mask(new_network_bits)

    return {
        "network_bits": new_network_bits,
        "subnet_mask": subnet_mask,
        "subnet_mask_binary": binary_subnet_mask,
        "networks": networks
    }


def same_subnet(ip_address_1, ip_address_2, subnet_mask=None):
    # Parse the two IP addresses to return the IP address without /n suffix and the number of network bits
    ip_address_1, network_bits_1 = get_network_bits(ip_address_1, subnet_mask)
    ip_address_2, network_bits_2 = get_network_bits(ip_address_2, subnet_mask)

    # If the number of network bits aren't the same, they're not on the same subnet
    if network_bits_1 != network_bits_2:
        return 

    # Calculate which octet the network bits end in
    final_network_octet = network_bits_1 // 8
    if final_network_octet % 8 > 0:
        final_network_octet = final_network_octet + 1

    # Split the two IP addresses into octets and then to a non-delimited binary representation
    octets_1 = split_address(ip_address_1)
    octets_2 = split_address(ip_address_2)
    binary_1 = "".join(convert_octets_to_binary(octets_1))
    binary_2 = "".join(convert_octets_to_binary(octets_2))

    # If the network bits are the same in both, they're on the same subnet
    in_same_subnet = binary_1[:network_bits_1] == binary_2[:network_bits_1]
    return in_same_subnet
