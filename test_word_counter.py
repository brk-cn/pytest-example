import pytest
from word_counter import word_counter

@pytest.mark.parametrize("text, expected_count", [
    ("Hello World!", 2),
    ("", 0),
    ("    ", 0),
    ("1 2 3 4 5", 5),
    ("Hello! How are you? I'm fine, thank you.", 8),
    ("  This    text    has    multiple    spaces.  ", 5),
    ("Hello\nWorld", 2),
    ("Tab\tTab\tTab", 3),
    ("Merhaba, dünya! こんにちは、世界", 4)
])

def test_word_counter(text, expected_count):
    assert word_counter(text) == expected_count
