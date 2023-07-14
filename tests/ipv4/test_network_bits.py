from src.ipv4 import calculate_network_bits


def test_network_bits_class_a():
    network_bits = calculate_network_bits([255, 0, 0, 0])
    assert 8 == network_bits


def test_network_bits_class_b():
    network_bits = calculate_network_bits([255, 255, 0, 0])
    assert 16 == network_bits


def test_network_bits_class_c():
    network_bits = calculate_network_bits([255, 255, 255, 0])
    assert 24 == network_bits


def test_network_bits_example_1():
    network_bits = calculate_network_bits([255, 255, 240, 0])
    assert 20 == network_bits


def test_network_bits_example_2():
    network_bits = calculate_network_bits([255, 255, 128, 0])
    assert 17 == network_bits
