import pytest
from src.ipv4 import calculate_subnets


def test_calculate_subnets_for_hosts_with_suffix_1():
    subnets = calculate_subnets("10.1.1.0/24", number_of_hosts=14)
    number_of_networks = len(subnets["networks"])
    assert 16 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [10, 1, 1, 0] == subnets["networks"][0]["network"]
    assert ["00001010", "00000001", "00000001", "00000000"] == subnets["networks"][0]["network_binary"]
    assert [10, 1, 1, 240] == subnets["networks"][number_of_networks - 1]["network"]
    assert ["00001010", "00000001", "00000001", "11110000"] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_hosts_without_suffix_1():
    subnets = calculate_subnets("10.1.1.0", "255.255.255.0", number_of_hosts=14)
    number_of_networks = len(subnets["networks"])
    assert 16 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [10, 1, 1, 0] == subnets["networks"][0]["network"]
    assert ["00001010", "00000001", "00000001", "00000000"] == subnets["networks"][0]["network_binary"]
    assert [10, 1, 1, 240] == subnets["networks"][number_of_networks - 1]["network"]
    assert ["00001010", "00000001", "00000001", "11110000"] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_hosts_with_suffix_2():
    subnets = calculate_subnets("192.168.1.64/26", number_of_hosts=8)
    number_of_networks = len(subnets["networks"])
    assert 4 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [192, 168, 1, 64] == subnets["networks"][0]["network"]
    assert ['11000000', '10101000', '00000001', '01000000'] == subnets["networks"][0]["network_binary"]
    assert [192, 168, 1, 112] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['11000000', '10101000', '00000001', '01110000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_hosts_without_suffix_2():
    subnets = calculate_subnets("192.168.1.64", "255.255.255.192", number_of_hosts=8)
    number_of_networks = len(subnets["networks"])
    assert 4 == number_of_networks
    assert 28 == subnets["network_bits"]
    assert [255, 255, 255, 240] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11110000"] == subnets["subnet_mask_binary"]
    assert [192, 168, 1, 64] == subnets["networks"][0]["network"]
    assert ['11000000', '10101000', '00000001', '01000000'] == subnets["networks"][0]["network_binary"]
    assert [192, 168, 1, 112] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['11000000', '10101000', '00000001', '01110000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_networks_with_suffix_1():
    subnets = calculate_subnets("10.128.192.0/18", number_of_networks=30)
    number_of_networks = len(subnets["networks"])
    assert 32 == number_of_networks
    assert 23 == subnets["network_bits"]
    assert [255, 255, 254, 0] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111110", "00000000"] == subnets["subnet_mask_binary"]
    assert [10, 128, 192, 0] == subnets["networks"][0]["network"]
    assert ['00001010', '10000000', '11000000', '00000000'] == subnets["networks"][0]["network_binary"]
    assert [10, 128, 254, 0] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['00001010', '10000000', '11111110', '00000000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_networks_without_suffix_1():
    subnets = calculate_subnets("10.128.192.0", "255.255.192.0", number_of_networks=30)
    number_of_networks = len(subnets["networks"])
    assert 32 == number_of_networks
    assert 23 == subnets["network_bits"]
    assert [255, 255, 254, 0] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111110", "00000000"] == subnets["subnet_mask_binary"]
    assert [10, 128, 192, 0] == subnets["networks"][0]["network"]
    assert ['00001010', '10000000', '11000000', '00000000'] == subnets["networks"][0]["network_binary"]
    assert [10, 128, 254, 0] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['00001010', '10000000', '11111110', '00000000'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_network_bits_with_suffix_1():
    subnets = calculate_subnets("192.168.1.96/28", number_of_network_bits=30)
    number_of_networks = len(subnets["networks"])
    assert 4 == number_of_networks
    assert 30 == subnets["network_bits"]
    assert [255, 255, 255, 252] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11111100"] == subnets["subnet_mask_binary"]
    assert [192, 168, 1, 96] == subnets["networks"][0]["network"]
    assert ['11000000', '10101000', '00000001', '01100000'] == subnets["networks"][0]["network_binary"]
    assert [192, 168, 1, 108] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['11000000', '10101000', '00000001', '01101100'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_calculate_subnets_for_network_bits_without_suffix_1():
    subnets = calculate_subnets("192.168.1.96", "255.255.255.240", number_of_network_bits=30)
    number_of_networks = len(subnets["networks"])
    assert 4 == number_of_networks
    assert 30 == subnets["network_bits"]
    assert [255, 255, 255, 252] == subnets["subnet_mask"]
    assert ["11111111", "11111111", "11111111", "11111100"] == subnets["subnet_mask_binary"]
    assert [192, 168, 1, 96] == subnets["networks"][0]["network"]
    assert ['11000000', '10101000', '00000001', '01100000'] == subnets["networks"][0]["network_binary"]
    assert [192, 168, 1, 108] == subnets["networks"][number_of_networks - 1]["network"]
    assert ['11000000', '10101000', '00000001', '01101100'] == subnets["networks"][number_of_networks - 1]["network_binary"]


def test_invalid_hosts_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_hosts=-1)


def test_invalid_networks_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_networks=-1)


def test_invalid_network_bits_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_network_bits=-1)


def test_no_hosts_or_networks_or_network_bits_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24")


def test_hosts_and_networks_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_hosts=10, number_of_networks=10)


def test_networks_and_network_bits_error():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_networks=10, number_of_network_bits=10)


def test_too_many_hosts_error_with_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_hosts=1000000)


def test_too_many_hosts_error_without_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0", "255.255.255.0", number_of_hosts=1000000)


def test_too_many_networks_error_with_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_networks=1000000)


def test_too_many_networks_error_without_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0", "255.255.255.0", number_of_networks=1000000)


def test_too_many_network_bits_error_with_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0/24", number_of_network_bits=1000000)


def test_too_many_network_bits_error_without_suffix():
    with pytest.raises(ValueError):
        _ = calculate_subnets("10.1.1.0", "255.255.255.0", number_of_network_bits=1000000)

