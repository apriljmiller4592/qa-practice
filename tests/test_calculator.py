from src.calculator import add, subtract, multiply, divide, power
import pytest

def test_add():

    first_num = 2
    second_num = 3

    result = add(first_num, second_num)
    
    assert result == 5

def test_add_negative_numbers():

    first_num = -5
    second_num = -3

    result = add(first_num, second_num)

    assert result == -8

def test_subtract():
    
    first_num = 3
    second_num = 2

    result = subtract(first_num, second_num)

    assert result == 1

def test_multiply():

    first_num = 2
    second_num = 3

    result = multiply(first_num, second_num)

    assert result == 6

def test_divide():

    first_num = 6
    second_num = 2

    result = divide(first_num, second_num)

    assert result == 3

def test_divide_by_0():

    first_num = 10
    second_num = 0

    with pytest.raises(ValueError):
        divide(first_num, second_num)

def test_power():
    
    first_num = 2
    second_num = 2

    result = power(first_num, second_num)

    assert result == 4

def test_exponent_0():

    first_num = 2
    second_num = 0

    result = power(first_num, second_num)

    assert result == 1

def test_negative_base():

    first_num = -2
    second_num = 2

    result = power(first_num, second_num)

    assert result == 4

def test_exponent_1():

    first_num = 10
    second_num = 1

    result = power(first_num, second_num)

    assert result == 10

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
