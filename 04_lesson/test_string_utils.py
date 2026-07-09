import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_negative_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    skypro", "skypro"),
    ("   !!!", "!!!"),
    ("   123", "123"),
])
def test_trim_positive_spaces_before(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_negative_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("[04 april 2026]", "2026"),
])
def test_contains_positive_true(input_str, expected):
    assert string_utils.contains(input_str, expected) is True


def test_contains_positive_false():
    assert string_utils.contains("hello world", "U") is False


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
        ("", "A"),
])
def test_contains_Negative_false(input_str, expected):
    assert string_utils.contains(input_str, expected) is False


def test_contains_Negative_empty():
    with pytest.raises(ValueError):
        string_utils.contains("SkyPro", "")


def test_delete_symbol_positive_char():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_positive_not_found():
    assert string_utils.delete_symbol("SkyPro", "x") == "SkyPro"


def test_delete_symbol_negative_empty_string():
    assert string_utils.delete_symbol("", "k") == ""
