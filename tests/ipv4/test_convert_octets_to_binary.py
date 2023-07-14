import pytest
from src.ipv4 import convert_octets_to_binary


def test_valid_octets():
    octets = convert_octets_to_binary([192, 168, 0, 10])
    assert 4 == len(octets)
    assert "11000000" == octets[0]
    assert "10101000" == octets[1]
    assert "00000000" == octets[2]
    assert "00001010" == octets[3]
