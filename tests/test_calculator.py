from src.calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-5, -3) == -8

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_0():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (4, 5, 9),
        (-4, -5, -9),
        (3, 5, 8),
    ],
)

def test_parameterized(a, b, expected):
    assert add(a, b) == expected