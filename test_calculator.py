"""
Unit Test Suite for Scientific Calculator
Author: Anees Shaikh
"""

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator operations."""
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_division(self):
        self.assertEqual(self.calc.divide(20, 4), 5.0)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_square_root_negative_error(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-9)

if __name__ == "__main__":
    unittest.main()
