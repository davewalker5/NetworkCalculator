from client import IPv4Client
from cli.user_input import prompt_for_string
from cli.presentation import create_ip_string


def request_same_subnet_check(api_url, ip_address_1, ip_address_2, subnet_mask):
    """
    Determine if two IP addresses are on the same subnet

    :param api_url: Protocol, hostname and port for the REST API
    :param ip_address_1: First IP address in dotted decimal notation with optional /n suffix
    :param ip_address_2: Second IP address in dotted decimal notation with optional /n suffix
    :param subnet_mask: Subnet mask in dotted decimal  (not needed if both IP addresses include /n)
    """
    try:
        client = IPv4Client(api_url)
        same_subnet = client.on_same_subnet(ip_address_1, ip_address_2, subnet_mask)

        print()
        print(f"First IP    : {ip_address_1}")
        print(f"Second IP   : {ip_address_2}")
        print(f"Subnet Mask : {subnet_mask}")
        print(f"Same Subnet : {'Yes' if same_subnet else 'No'}")
        print()

    except BaseException as e:
        print()
        print(f"Error: {str(e)}")
        print()


def same_subnet_main(api_url):
    """
    Entry point for determining if two IPs are on the same subnet

    :param api_url: Protocol, hostname and port for the REST API
    """
    while True:
        print("IPv4 Same Subnet Calculator")
        print()

        ip_address_1 = prompt_for_string("First IP Address?")
        if not ip_address_1:
            break

        ip_address_2 = prompt_for_string("Second IP Address?")
        if not ip_address_2:
            break

        subnet_mask = prompt_for_string("Subnet Mask?")

        request_same_subnet_check(api_url, ip_address_1, ip_address_2, subnet_mask)
