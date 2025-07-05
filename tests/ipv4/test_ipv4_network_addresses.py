import pytest
from src.ipv4 import calculate_network_properties


def test_calculate_network_properties():
    properties = calculate_network_properties("172.16.35.123", "255.255.240.0")
    assert [172, 16, 47, 255] == properties["broadcast"]
    assert ["10101100", "00010000", "00101111", "11111111"] == properties["broadcast_binary"]
    assert [172, 16, 32, 1] == properties["first"]
    assert ["10101100", "00010000", "00100000", "00000001"] == properties["first_binary"]
    assert [172, 16, 47, 254] == properties["last"]
    assert ["10101100", "00010000", "00101111", "11111110"] == properties["last_binary"]
    assert [172, 16, 32, 0] == properties["network"]
    assert ["10101100", "00010000", "00100000", "00000000"] == properties["network_binary"]
    assert [255, 255, 240, 0] == properties["subnet"]
    assert ["11111111", "11111111", "11110000", "00000000"] == properties["subnet_binary"]
    assert 20 == properties["network_bits"]


def test_calculate_network_properties_cidr():
    properties = calculate_network_properties("172.16.35.123/20", None)
    assert [172, 16, 47, 255] == properties["broadcast"]
    assert ["10101100", "00010000", "00101111", "11111111"] == properties["broadcast_binary"]
    assert [172, 16, 32, 1] == properties["first"]
    assert ["10101100", "00010000", "00100000", "00000001"] == properties["first_binary"]
    assert [172, 16, 47, 254] == properties["last"]
    assert ["10101100", "00010000", "00101111", "11111110"] == properties["last_binary"]
    assert [172, 16, 32, 0] == properties["network"]
    assert ["10101100", "00010000", "00100000", "00000000"] == properties["network_binary"]
    assert [255, 255, 240, 0] == properties["subnet"]
    assert ["11111111", "11111111", "11110000", "00000000"] == properties["subnet_binary"]
    assert 20 == properties["network_bits"]
