import pytest
from src.ipv4 import calculate_subnets


def test_calculate_subnets_for_hosts_with_suffix():
    subnets = calculate_subnets("10.1.1.0/24", None, 14, 0)
    number_of_networks = len(subnets["networks"])
    assert 16 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [10, 1, 1, 0] == subnets["networks"][0]["network"]
    assert ["00001010", "00000001", "00000001", "00000000"] == subnets["networks"][0]["network_binary"]
    assert [10, 1, 1, 240] == subnets["networks"][number_of_networks - 1]["network"]
    assert ["00001010", "00000001", "00000001", "11110000"] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_hosts_without_suffix():
    subnets = calculate_subnets("10.1.1.0", "255.255.255.0", 14, 0)
    number_of_networks = len(subnets["networks"])
    assert 16 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [10, 1, 1, 0] == subnets["networks"][0]["network"]
    assert ["00001010", "00000001", "00000001", "00000000"] == subnets["networks"][0]["network_binary"]
    assert [10, 1, 1, 240] == subnets["networks"][number_of_networks - 1]["network"]
    assert ["00001010", "00000001", "00000001", "11110000"] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_networks_with_suffix():
    subnets = calculate_subnets("10.128.192.0/18", None, 0, 30)
    number_of_networks = len(subnets["networks"])
    assert 32 == number_of_networks
    assert 23 == subnets["network_bits"]
    assert [255, 255, 254, 0] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111110", "00000000"] == subnets["subnet_mask_binary"]
    assert [10, 128, 192, 0] == subnets["networks"][0]["network"]
    assert ['00001010', '10000000', '11000000', '00000000'] == subnets["networks"][0]["network_binary"]
    assert [10, 128, 254, 0] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['00001010', '10000000', '11111110', '00000000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_networks_without_suffix():
    subnets = calculate_subnets("10.128.192.0", "255.255.192.0", 0, 30)
    number_of_networks = len(subnets["networks"])
    assert 32 == number_of_networks
    assert 23 == subnets["network_bits"]
    assert [255, 255, 254, 0] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111110", "00000000"] == subnets["subnet_mask_binary"]
    assert [10, 128, 192, 0] == subnets["networks"][0]["network"]
    assert ['00001010', '10000000', '11000000', '00000000'] == subnets["networks"][0]["network_binary"]
    assert [10, 128, 254, 0] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['00001010', '10000000', '11111110', '00000000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_invalid_hosts_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, -1, 0)


def test_invalid_networks_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, 0, -1)


def test_no_hosts_or_networks_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, 0, 0)


def test_hosts_and_networks_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, 10, 10)


def test_too_many_hosts_error_with_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, 1000000, 0)


def test_too_many_hosts_error_without_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0", "255.255.255.0", 1000000, 0)


def test_too_many_networks_error_with_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", None, 0, 1000000)


def test_too_many_networks_error_without_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0", "255.255.255.0", 0, 1000000)
