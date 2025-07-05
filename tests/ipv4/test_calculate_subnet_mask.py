from src.ipv4 import calculate_subnet_mask


def test_calculate_subnet_mask_class_a():
    octets, binary_octets = calculate_subnet_mask(8)
    assert [255, 0, 0, 0] == octets
    assert ["11111111", "00000000", "00000000", "00000000"] == binary_octets


def test_calculate_subnet_mask_class_b():
    octets, binary_octets = calculate_subnet_mask(16)
    assert [255, 255, 0, 0] == octets
    assert ["11111111", "11111111", "00000000", "00000000"] == binary_octets


def test_calculate_subnet_mask_class_c():
    octets, binary_octets = calculate_subnet_mask(24)
    assert [255, 255, 255, 0] == octets
    assert ["11111111", "11111111", "11111111", "00000000"] == binary_octets


def test_calculate_subnet_mask_class_example_1():
    octets, binary_octets = calculate_subnet_mask(20)
    assert [255, 255, 240, 0] == octets
    assert ["11111111", "11111111", "11110000", "00000000"] == binary_octets


def test_calculate_subnet_mask_class_example_2():
    octets, binary_octets = calculate_subnet_mask(17)
    assert [255, 255, 128, 0] == octets
    assert ["11111111", "11111111", "10000000", "00000000"] == binary_octets
