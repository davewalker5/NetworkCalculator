from io import StringIO
from src.cli.user_input import prompt_for_option

USER_PROMPT = "Option"
OPTIONS = ["Network Details", "Subnetting"]


def test_can_select_option(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("1\n"))
    option = prompt_for_option(OPTIONS, USER_PROMPT)
    assert 1 == option


def test_cannot_select_less_than_minimum_option(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("0\n\n"))
    option = prompt_for_option(OPTIONS, USER_PROMPT)
    assert None == option


def test_cannot_select_more_than_maximum_option(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("3\n\n"))
    option = prompt_for_option(OPTIONS, USER_PROMPT)
    assert None == option
