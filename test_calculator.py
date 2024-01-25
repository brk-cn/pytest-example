import pytest
from calculator import calculator

def test_addition():
    assert calculator(1, 2, '+') == 3
    assert calculator(-1, -2, '+') == -3
    assert calculator(0, 0, '+') == 0

def test_subtraction():
    assert calculator(1, 2, '-') == -1
    assert calculator(2, 1, '-') == 1
    assert calculator(0, 0, '-') == 0

def test_multiplication():
    assert calculator(1, 2, '*') == 2
    assert calculator(-1, 2, '*') == -2
    assert calculator(-1, -2, '*') == 2
    assert calculator(1, 0, '*') == 0

def test_division():
    assert calculator(2, 1, '/') == 2
    assert calculator(1, 2, '/') == 0.5

def test_invalid_operand():
    with pytest.raises(ValueError):
        calculator(1, 1, '%')

def test_invalid_input():
    with pytest.raises(ValueError):
        calculator("a", "b", '+')

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        calculator(1, 0, '/')
