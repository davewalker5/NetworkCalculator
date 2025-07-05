IP_COLUMN_WIDTH = 18


def create_ip_string(ip_addresses, key):
    """
    Given a dictionary of network IP addresses from the API and a key, compile the octets for the specified
    key into a string in dot-separated format

    :param ip_addresses: Dictionary of network octets
    :param key: Key for the entry in the IP address dictionary to return a string for
    :return: IP address for the specified key in dot-separated format
    """
    return ".".join([str(o) for o in ip_addresses[key]])


def print_network_details_row(number, network, first_host, last_host, broadcast, number_column_width, ip_column_width):
    """
    Print a row in a table of network details, with column justification

    :param number: Row number
    :param network: Network address
    :param first_host: First host address
    :param last_host: Last host address
    :param broadcast: Broadcast address
    :param number_column_width: Justified width of the row number column
    :param ip_column_width: Justified width of the IP address columns
    """
    number_column = str(number).ljust(number_column_width, " ")
    network_column = network.ljust(ip_column_width, " ")
    first_column = first_host.ljust(ip_column_width, " ")
    last_column = last_host.ljust(ip_column_width, " ")
    broadcast_column = broadcast.ljust(ip_column_width, " ")
    print(f"{number_column} {network_column} {first_column} {last_column} {broadcast_column}")