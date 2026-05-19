"""Tests for the Calculator class."""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


class TestAdd:
    def test_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5

    def test_negative_numbers(self, calc):
        assert calc.add(-1, -1) == -2

    def test_zero(self, calc):
        assert calc.add(0, 0) == 0


class TestSubtract:
    def test_basic(self, calc):
        assert calc.subtract(10, 3) == 7

    def test_negative_result(self, calc):
        assert calc.subtract(3, 10) == -7


class TestMultiply:
    def test_basic(self, calc):
        assert calc.multiply(4, 5) == 20

    def test_by_zero(self, calc):
        assert calc.multiply(100, 0) == 0


class TestDivide:
    def test_basic(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self, calc):
        with pytest.raises(ValueError, match="zero"):
            calc.divide(1, 0)


class TestPower:
    def test_positive_exponent(self, calc):
        assert calc.power(2, 3) == 8.0

    def test_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1.0

    def test_negative_exponent(self, calc):
        assert calc.power(2, -2) == pytest.approx(0.25)

    def test_base_one(self, calc):
        assert calc.power(1, 100) == 1.0


class TestAverage:
    def test_single_value(self, calc):
        assert calc.average([5]) == 5.0

    def test_multiple_values(self, calc):
        assert calc.average([2, 4, 6]) == 4.0

    def test_empty_list_raises(self, calc):
        with pytest.raises(ValueError, match="empty"):
            calc.average([])

    def test_negative_values(self, calc):
        assert calc.average([-2, -4]) == -3.0
