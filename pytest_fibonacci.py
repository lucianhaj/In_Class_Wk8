import fibonacci
import pytest


def test_fibonacci():
    assert fibonacci.fib(5) == 3
    assert fibonacci.fib(6) == 5
    assert fibonacci.fib(11) == 144


def test_factorial():
    assert fibonacci.fact(5) == 120
    assert fibonacci.fact(4) == 24


if __name__ == "__main__":
    pytest.main()

