from src.ipv4 import get_network_bits


def test_without_ip_address_suffix():
    ip_address, bits = get_network_bits("172.16.35.123", "255.255.240.0")
    assert "172.16.35.123" == ip_address
    assert 20 == bits


def test_with_ip_address_suffix():
    ip_address, bits = get_network_bits("172.16.35.123/20", None)
    assert "172.16.35.123" == ip_address
    assert 20 == bits
