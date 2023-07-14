import pytest
from src.cli.presentation import create_ip_string

@pytest.fixture
def ip_addresses():
    return {
        "broadcast": [10, 128, 193, 255],
        "broadcast_binary": ["00001010", "10000000", "11000001", "11111111"],
        "first": [10, 128, 192, 1],
        "first_binary": ["00001010", "10000000", "11000000", "00000001"],
        "last": [10, 128, 193, 254],
        "last_binary": ["00001010", "10000000", "11000001", "11111110"],
        "network": [10, 128, 192, 0],
        "network_binary": ["00001010", "10000000", "11000000", "00000000"]
    }


def test_create_broadcast_ip_string(ip_addresses):
    ip_string = create_ip_string(ip_addresses, "broadcast")
    assert "10.128.193.255" == ip_string


def test_create_first_host_ip_string(ip_addresses):
    ip_string = create_ip_string(ip_addresses, "first")
    assert "10.128.192.1" == ip_string


def test_create_last_host_ip_string(ip_addresses):
    ip_string = create_ip_string(ip_addresses, "last")
    assert "10.128.193.254" == ip_string


def test_create_network_ip_string(ip_addresses):
    ip_string = create_ip_string(ip_addresses, "network")
    assert "10.128.192.0" == ip_string
