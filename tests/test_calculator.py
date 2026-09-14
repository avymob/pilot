from calculator import divide, add, subtract, multiply
import pytest

def test_divide_normal():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    assert divide(6, -2) == -3
    assert divide(6, 0.5) == 12
    assert divide(7.5, 2.5) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Denominator must not be zero"):
        divide(1, 0)
    with pytest.raises(ValueError, match="Denominator must not be zero"):
        divide(5.4, 0)

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
    assert add(-2, -3) == -5
    assert add(0.5, 1.5) == 2.0
    assert add(-1.1, 2.2) == 1.1

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(-5, 2) == -7
    assert subtract(2, 5) == -3
    assert subtract(-5, -2) == -3
    assert subtract(0.5, 1.5) == -1.0
    assert abs(subtract(-1.1, 2.2) - (-3.3)) < 1e-9

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(3, -4) == -12
    assert multiply(-3, -4) == 12
    assert multiply(0.5, 2) == 1.0
    assert multiply(-1.5, 2) == -3.0
