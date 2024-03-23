import pytest
from factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_non_integer_input():
    with pytest.raises(ValueError):
        factorial("1")

def test_negative_input():
    with pytest.raises(ValueError):
        factorial(-1)
