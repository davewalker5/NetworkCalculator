import pytest
from src.ipv4 import split_address


def test_valid_address():
    octets = split_address("192.168.0.10")
    assert 4 == len(octets)
    assert 192 == octets[0]
    assert 168 == octets[1]
    assert 0 == octets[2]
    assert 10 == octets[3]


def test_negative_octet_error():
    with pytest.raises(ValueError):
        _ = split_address("192.168.-1.10")


def test_out_of_range_octet_error():
    with pytest.raises(ValueError):
        _ = split_address("192.999.0.10")


def test_non_numeric_octet_error():
    with pytest.raises(ValueError):
        _ = split_address("192.168.0.BAD")


def test_too_many_octets_error():
    with pytest.raises(ValueError):
        _ = split_address("192.168.0.10.255")
