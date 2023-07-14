from io import StringIO
from src.cli.user_input import prompt_for_integer

USER_PROMPT = "Please enter an integer"


def test_get_empty_user_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("\n"))
    number = prompt_for_integer(USER_PROMPT)
    assert None == number


def test_minimum_is_enforced(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("-1\n67\n"))
    number = prompt_for_integer(USER_PROMPT, 1)
    assert 67 == number


def test_maximum_is_enforced(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("100\n57\n"))
    number = prompt_for_integer(USER_PROMPT, maximum_value=60)
    assert 57 == number


def test_min_and_max_are_enforced(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("5\n100\n46\n"))
    number = prompt_for_integer(USER_PROMPT, 10, 50)
    assert 46 == number


def test_invalid_input_reprompts(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("ABC\n134\n"))
    number = prompt_for_integer(USER_PROMPT)
    assert 134 == number


def test_get_positive_integer(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("34\n"))
    number = prompt_for_integer(USER_PROMPT)
    assert 34 == number
