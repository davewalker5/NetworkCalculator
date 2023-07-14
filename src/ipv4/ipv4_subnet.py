from . import get_network_bits, calculate_all_ip_addresses, split_address, calculate_ip_address, \
    convert_binary_string_to_decimal_octets, calculate_subnet_mask
from common import AddressType


def calculate_subnets(ip_address, subnet_mask, number_of_hosts, number_of_networks):
    # Validate the requested number of hosts/networks
    if number_of_hosts < 0:
        raise ValueError(f"{number_of_hosts} is not valid for the number of hosts")

    if number_of_networks < 0:
        raise ValueError(f"{number_of_networks} is not valid for the number of networks")

    if number_of_hosts == 0 and number_of_networks == 0:
        raise ValueError(f"Must specify a number of hosts or a number of networks")

    if number_of_hosts > 0 and number_of_networks > 0:
        raise ValueError(f"Cannot specify both a number of hosts and a number of networks")

    # Get the IP address and number of network bits
    ip_address, network_bits = get_network_bits(ip_address, subnet_mask)

    # Calculate the number of bits we need to take from the host portion
    for n in range(0, 32):
        if number_of_hosts > 0:
            number_of_hosts_for_n = pow(2, n) - 2
            if number_of_hosts_for_n >= number_of_hosts:
                break
        else:
            number_of_networks_for_n = pow(2, n)
            if number_of_networks_for_n >= number_of_networks:
                break

    # Calculate the new number of network bits and check it's in range
    new_network_bits = network_bits + n
    if new_network_bits > 32:
        raise ValueError(f"Not enough host bits left to support {number_of_hosts} hosts per subnet")

    # Split the address into octets, get the binary version and generate a non-delimited binary
    # string representing the IP address
    octets = split_address(ip_address)
    _, binary_octets = calculate_ip_address(octets, new_network_bits, AddressType.NETWORK)
    binary_ip_address = "".join(binary_octets)

    # To calculate the address of each subsequent network, we need to iterate through all possible
    # binary combinations of the subnet bits
    networks = []
    for i in range(0, pow(2, n)):
        # They're the "n" bits starting at network_bits + 1: Generate a binary IP address string
        # with this combination in the subnet bits and 0 in the host bits
        subnet_bits = bin(i).replace("0b", "").zfill(n)
        current_binary_address = binary_ip_address[:network_bits] + subnet_bits + "0" * (32 - new_network_bits)

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
