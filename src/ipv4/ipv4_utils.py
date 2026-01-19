from common import AddressType


def validate_octets(octets):
    """
    Validate that a list of decimal octets represent a valid IPv4 address or subnet mask

    :param octets: List of decimal octets
    """
    if len(octets) != 4:
        raise ValueError(f"{'.'.join([str(o) for o in octets])} is not a valid IPv4 address")

    invalid_type = [o for o in octets if type(o).__name__ != "int"]
    if invalid_type:
        raise ValueError(f"{'.'.join([str(o) for o in octets])} is not a valid IPv4 address")

    out_of_range = [o for o in octets if o < 0 or o > 255]
    if out_of_range:
        raise ValueError(f"{'.'.join([str(o) for o in octets])} is not a valid IPv4 address")


def split_address(address):
    """
    Given a dotted decimal representation of an IPv4 address, return a list of decimal octets

    :param address: IPv4 address in dotted decimal format e.g. 192.168.0.10
    """
    try:
        octets = [int(o) for o in address.split(".")]
    except ValueError as e:
        raise ValueError(f"{address} is not a valid IPv4 address") from e

    validate_octets(octets)
    return octets


def calculate_network_bits(octets):
    """
    Given a set of decimal octets representing a subnet mask, return the number of network
    bits

    :param octets: List of decimal octets
    :return: Number of network bits
    """
    validate_octets(octets)

    bits = 0
    for octet in octets:
        if octet == 255:
            bits = bits + 8
        else:
            binary = bin(octet).replace("0b", "").zfill(8)
            bits = bits + binary.find("0")
            break

    return bits


def convert_octets_to_binary(octets):
    """
    Given a list of decimal octets, return their binary equivalent

    :param octets: List of decimal octets
    :return: List of corresponding binary octets
    """
    validate_octets(octets)

    binary_octets = []
    for octet in octets:
        binary = bin(octet).replace("0b", "").zfill(8)
        binary_octets.append(binary)

    return binary_octets


def convert_binary_string_to_decimal_octets(binary):
    """
    Convert a string of binary bits, with no delimiter, to a list of decimal octets

    :param binary: Binary string
    :return: List of decimal octets
    """
    octets = []
    for i in range(0, 4):
        binary_octet = binary[i * 8:i * 8 + 8]
        octets.append(int(binary_octet, 2))

    return octets


def convert_binary_string_to_binary_octets(binary):
    """
    Convert a string of binary bits, with no delimiter, to a list of binary octets

    :param binary: Binary string
    :return: List of binary octets
    """
    octets = []
    for i in range(0, 4):
        octet = binary[i * 8:i * 8 + 8]
        octets.append(octet)

    return octets


def calculate_ip_address(octets, network_bits, which_address):
    """
    Given an IP address and a number of network bits, calculate the IP address for the
    network, first/last host or broadcast address

    :param octets: List of decimal octets representing the IP address
    :param network_bits: Number of network bits
    :param which_address: AddressType enumeration specifying which address is required
    :return: Tuple of decimal and binary octets for the requested address
    """
    validate_octets(octets)

    # Convert the IP address represented by the octets into a non-delimited binary string
    binary_octets = convert_octets_to_binary(octets)
    binary_string = "".join(binary_octets)

    # Calculate the binary representation of the required address based on which address is
    # being requested (network, first host, last host or broadcast)
    if which_address == AddressType.NETWORK:
        binary_ip_string = binary_string[:network_bits] + "0" * (32 - network_bits)
    elif which_address == AddressType.FIRST_HOST:
        binary_ip_string = binary_string[:network_bits] + "0" * (31 - network_bits) + "1"
    elif which_address == AddressType.LAST_HOST:
        binary_ip_string = binary_string[:network_bits] + "1" * (31 - network_bits) + "0"
    elif which_address == AddressType.BROADCAST:
        binary_ip_string = binary_string[:network_bits] + "1" * (32 - network_bits)
    else:
        raise ValueError(f"{which_address} is not a valid address type")

    # Convert the binary string to decimal and binary octets
    network_octets = convert_binary_string_to_decimal_octets(binary_ip_string)
    binary_octets = convert_binary_string_to_binary_octets(binary_ip_string)

    return network_octets, binary_octets


def calculate_all_ip_addresses(octets, network_bits):
    """
    Given an IP address and a number of network bits, calculate the network, first/last host and
    broadcast IP address

    :param octets: List of decimal octets representing the IP address
    :param network_bits: Number of network bits
    :return: Dictionary of IP address details
    """
    validate_octets(octets)

    network_octets, binary_octets = calculate_ip_address(octets, network_bits, AddressType.NETWORK)
    first_host_octets, binary_first_host_octets = calculate_ip_address(octets, network_bits, AddressType.FIRST_HOST)
    last_host_octets, binary_last_host_octets = calculate_ip_address(octets, network_bits, AddressType.LAST_HOST)
    broadcast_octets, binary_broadcast_octets = calculate_ip_address(octets, network_bits, AddressType.BROADCAST)

    return {
        "network": network_octets,
        "network_binary": binary_octets,
        "first": first_host_octets,
        "first_binary": binary_first_host_octets,
        "last": last_host_octets,
        "last_binary": binary_last_host_octets,
        "broadcast": broadcast_octets,
        "broadcast_binary": binary_broadcast_octets
    }


def get_network_bits(ip_address, subnet_mask):
    """
    Given an IP address and subnet mask, return the number of network bits

    :param ip_address: IP address in dotted-decimal notation, with optional /n suffix
    :param subnet_mask: Subnet mask in dotted-decimal notation, or none if the IP address has the /n suffix
    :return: Tuple of the IP address without the /n suffix and the number of network bits
    """

    # If the IP address is in CIDR format with a /n at the end, extract the number of
    # network bytes from that
    separator_position = ip_address.find("/")
    if separator_position > -1:
        network_bits = int(ip_address[separator_position + 1:])
        ip_address = ip_address[:separator_position]
    else:
        # Calculate the number of network bits from the subnet mask
        subnet_octets = split_address(subnet_mask)
        network_bits = calculate_network_bits(subnet_octets)

    return ip_address, network_bits


def calculate_subnet_mask(network_bits):
    """
    Given a number of network bits, return a set of octets representing the subnet mask

    :param network_bits: Number of network bits
    :return: Tuple of lists of decimal and binary octets and the octet number the mask ends in
    """

    # Calculate the mask as a binary string and calculate the octets
    binary_mask_string = "1" * network_bits + "0" * (32 - network_bits)
    subnet_octets = convert_binary_string_to_decimal_octets(binary_mask_string)
    binary_subnet_octets = convert_binary_string_to_binary_octets(binary_mask_string)

    return subnet_octets, binary_subnet_octets
