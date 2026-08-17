"""
Interactive Scientific Calculator & Expression Evaluator Engine
Author: Anees Shaikh
Description: Modular OOP Calculator in Python supporting basic arithmetic, trigonometric, logarithmic operations, history logging, and exception handling.
"""

import math

class Calculator:
    """Core Calculator engine providing arithmetic, scientific functions, and history."""
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        res = a + b
        self._record(f"{a} + {b} = {res}")
        return res

    def subtract(self, a: float, b: float) -> float:
        res = a - b
        self._record(f"{a} - {b} = {res}")
        return res

    def multiply(self, a: float, b: float) -> float:
        res = a * b
        self._record(f"{a} * {b} = {res}")
        return res

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        res = a / b
        self._record(f"{a} / {b} = {res}")
        return res

    def power(self, base: float, exponent: float) -> float:
        res = math.pow(base, exponent)
        self._record(f"{base} ^ {exponent} = {res}")
        return res

    def square_root(self, val: float) -> float:
        if val < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        res = math.sqrt(val)
        self._record(f"√({val}) = {res}")
        return res

    def logarithm(self, val: float, base: float = 10) -> float:
        if val <= 0:
            raise ValueError("Logarithm argument must be greater than zero.")
        res = math.log(val, base)
        self._record(f"log{base}({val}) = {res}")
        return res

    def sin(self, angle_degrees: float) -> float:
        radians = math.radians(angle_degrees)
        res = math.sin(radians)
        self._record(f"sin({angle_degrees}°) = {res}")
        return res

    def cos(self, angle_degrees: float) -> float:
        radians = math.radians(angle_degrees)
        res = math.cos(radians)
        self._record(f"cos({angle_degrees}°) = {res}")
        return res

    def _record(self, entry: str):
        """Record calculation to session history."""
        self.history.append(entry)

    def get_history(self) -> list:
        return self.history
