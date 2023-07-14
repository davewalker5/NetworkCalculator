import pytest
from src.ipv4 import validate_octets


def test_valid_octets():
    validate_octets([192, 168, 0, 10])


def test_negative_octet_error():
    with pytest.raises(ValueError):
        _ = validate_octets([192, 168, -1, 10])


def test_out_of_range_octet_error():
    with pytest.raises(ValueError):
        _ = validate_octets([192, 999, 0, 10])


def test_string_octet_error():
    with pytest.raises(ValueError):
        _ = validate_octets([192, 168, 0, "BAD"])


def test_float_octet_error():
    with pytest.raises(ValueError):
        _ = validate_octets([192, 168, 0, 10.1234])


def test_too_many_octets_error():
    with pytest.raises(ValueError):
        _ = validate_octets([192, 168, 0, 10, 255])
