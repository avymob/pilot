from calculator import divide
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
