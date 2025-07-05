import pytest
from src.ipv4 import calculate_ip_address
from src.common import AddressType


def test_calculate_network_address():
    decimal_octets, binary_octets = calculate_ip_address([172, 16, 35, 123], 20, AddressType.NETWORK)

    assert [172, 16, 32, 0] == decimal_octets
    assert ["10101100", "00010000", "00100000", "00000000"] == binary_octets


def test_calculate_first_host_address():
    decimal_octets, binary_octets = calculate_ip_address([172, 16, 35, 123], 20, AddressType.FIRST_HOST)

    assert [172, 16, 32, 1] == decimal_octets
    assert ["10101100", "00010000", "00100000", "00000001"] == binary_octets


def test_calculate_last_host_address():
    decimal_octets, binary_octets = calculate_ip_address([172, 16, 35, 123], 20, AddressType.LAST_HOST)

    assert [172, 16, 47, 254] == decimal_octets
    assert ["10101100", "00010000", "00101111", "11111110"] == binary_octets


def test_calculate_broadcast_address():
    decimal_octets, binary_octets = calculate_ip_address([172, 16, 35, 123], 20, AddressType.BROADCAST)

    assert [172, 16, 47, 255] == decimal_octets
    assert ["10101100", "00010000", "00101111", "11111111"] == binary_octets


def test_invalid_network_type_error():
    with pytest.raises(ValueError):
        _ = calculate_ip_address([172, 16, 35, 123], 20, -1)
