from app.calculator import add , subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 5) == 7

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
