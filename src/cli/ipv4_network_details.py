from client import IPv4Client
from cli.user_input import prompt_for_string
from cli.presentation import create_ip_string


def request_network_details(api_url, ip_address, subnet_mask):
    """
    Given an IP address and subnet mask, call the API to retrieve

    :param api_url: Protocol, hostname and port for the REST API
    :param ip_address: IP address in dotted decimal notation with optional /n suffix
    :param subnet_mask: Subnet mask in dotted decimal (or None if the IP address includes /n)
    """
    try:
        client = IPv4Client(api_url)
        details = client.get_network_details(ip_address, subnet_mask)

        print()
        print(f"Network Address   : {create_ip_string(details, 'network')}/{details['network_bits']}")
        print(f"Subnet Mask       : {create_ip_string(details, 'subnet')}")
        print(f"First Host        : {create_ip_string(details, 'first')}")
        print(f"Last Host         : {create_ip_string(details, 'last')}")
        print(f"Broadcast Address : {create_ip_string(details, 'broadcast')}")
        print()

    except BaseException as e:
        print()
        print(f"Error: {str(e)}")
        print()


def network_details_main(api_url):
    """
    Entry point for network details calculation and reporting

    :param api_url: Protocol, hostname and port for the REST API
    """
    while True:
        print("IPv4 Network Details Calculator")
        print()

        ip_address = prompt_for_string("IP Address?")
        if not ip_address:
            break

        subnet_mask = prompt_for_string("Subnet Mask?")

        request_network_details(api_url, ip_address, subnet_mask)
