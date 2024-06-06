from client import IPv4Client
from cli.user_input import prompt_for_string, prompt_for_integer
from cli.presentation import create_ip_string, print_network_details_row, IP_COLUMN_WIDTH


def request_subnet_details(api_url, ip_address, subnet_mask, hosts, networks, network_bits):
    """
    Given an IP address, subnet mask and a number of hosts/networks to subnet for, call the API to retrieve
    the subnet details

    :param api_url: Protocol, hostname and port for the REST API
    :param port: Port number for the REST API
    :param ip_address: IP address in dotted decimal notation with optional /n suffix
    :param subnet_mask: Subnet mask in dotted decimal (or None if the IP address includes /n)
    :param hosts: Number of hosts to accommodate or 0
    :param networks: Number of subnets required or 0
    :param network_bits: Number of network bits required or 0
    """
    try:
        client = IPv4Client(api_url)
        subnets = client.get_subnet_details(ip_address, subnet_mask, hosts, networks, network_bits)

        # Print overview details
        print()
        print(f"Subnet Mask       : {create_ip_string(subnets, 'subnet_mask')}")
        print(f"Network Bits      : {subnets['network_bits']}")
        print()

        # Tabulate the subnet details
        number_of_subnets = len(subnets["networks"])
        number_column_width = len(str(number_of_subnets))

        print_network_details_row("#", "Network", "First Host", "Last Host", "Broadcast", number_column_width, IP_COLUMN_WIDTH)
        print_network_details_row("-", "-------", "----------", "---------", "---------", number_column_width, IP_COLUMN_WIDTH)

        for i in range(0, number_of_subnets):
            network_details = subnets["networks"][i]
            network_address = create_ip_string(network_details, 'network')
            first_host = create_ip_string(network_details, 'first')
            last_host = create_ip_string(network_details, 'last')
            broadcast = create_ip_string(network_details, 'broadcast')

            print_network_details_row(i + 1, network_address, first_host, last_host, broadcast, number_column_width, IP_COLUMN_WIDTH)

        print()
    
    except BaseException as e:
        print()
        print(f"Error: {str(e)}")
        print()


def subnetting_main(api_url):
    """
    Entry point for subnetting calculation and reporting

    :param api_url: Protocol, hostname and port for the REST API
    """
    while True:
        print("IPv4 Subnet Calculator")
        print()

        ip_address = prompt_for_string("IP Address?")
        if not ip_address:
            break

        subnet_mask = prompt_for_string("Subnet Mask?")
        hosts = prompt_for_integer("Number of Hosts?", 0, None)
        networks = prompt_for_integer("Number of Networks?", 0, None)
        network_bits = prompt_for_integer("Number of Network Bits?", 0, None)
        if hosts == None and networks == None and network_bits == None:
            break

        request_subnet_details(api_url, ip_address, subnet_mask, hosts, networks, network_bits)
