from src.calculator import add, subtract, multiply, divide, power
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

def test_power():
    assert power(2, 2) == 4

def test_exponent_0():
    assert power(2, 0) == 1

def test_negative_base():
    assert power(-2, 2) == 4

def test_exponent_1():
    assert power(10, 1) == 10

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (4, 5, 9),
        (-4, -5, -9),
        (3, 5, 8),
    ],
)

def test_add_with_mult_inputs(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 2, 4),
        (4, 0, 1),
        (-4, 4, 256),
        (-4, 2, 16),
        (10, 1, 10)
    ],
)

def test_power_with_mult_inputs(base, exponent, expected):
    assert power(base, exponent) == expected
