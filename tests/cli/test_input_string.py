from io import StringIO
from src.cli.user_input import prompt_for_string

USER_PROMPT = "Please enter an IP address"


def test_get_empty_user_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("\n"))
    value = prompt_for_string(USER_PROMPT)
    assert None == value


def test_test_get_non_empty_user_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("10.1.1.0\n"))
    value = prompt_for_string(USER_PROMPT)
    assert "10.1.1.0" == value
