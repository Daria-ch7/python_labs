import pytest

from src.lib.text import count_freq, normalize, tokenize, top_n


@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(src, expected):
    assert normalize(src) == expected

@pytest.mark.parametrize(
    "src,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(src, expected):
    assert tokenize(src) == expected


@pytest.mark.parametrize(
        "tokens, expected",
        [
            (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
            (["good","good","good"], {"good":3}),
            (["💕","💕","💕","🤷‍♀️"],{"💕":3,"🤷‍♀️":1}),
        ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected

@pytest.mark.parametrize(
        "words, n, expected",
        [
        ({"c":6, "a":6, "b":2}, 2, [("a", 6), ("c", 6)]),
        ({"a": 3, "b": 2}, 5, [("a", 3), ("b", 2)]),
        ],
)

def test_top_n(words, n, expected):
    assert top_n(words, n) == expected

def test_empty():
    assert normalize("") == ""
    assert tokenize("") == []
    assert count_freq([]) == {}
    assert top_n({}, 5) == []

