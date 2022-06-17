import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_result_is_zero_on_initialization(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.get_result())

    def test_add_one_number(self):
        calculator = Calculator()
        calculator.add(5)
        self.assertEqual(5, calculator.get_result())

    def test_add_two_numbers(self):
        calculator = Calculator()
        calculator.add(5)
        calculator.add(3)
        self.assertEqual(8, calculator.get_result())

    def test_result_is_zero_after_getting_result(self):
        calculator = Calculator(False)
        calculator.add(5)
        calculator.get_result()
        self.assertEqual(0, calculator.get_result())

    def test_result_is_saved_after_getting_result(self):
        calculator = Calculator()
        calculator.add(5)
        calculator.get_result()
        self.assertEqual(5, calculator.get_result())

    def test_subtract_one_number(self):
        calculator = Calculator()
        calculator.subtract(5)
        self.assertEqual(-5, calculator.get_result())

    def test_subtract_two_numbers(self):
        calculator = Calculator()
        calculator.subtract(5)
        calculator.subtract(3)
        self.assertEqual(-8, calculator.get_result())
    
    def test_subtract_than_add(self):
        calculator = Calculator()
        calculator.subtract(5)
        calculator.add(3)
        self.assertEqual(-2, calculator.get_result())

    def test_add_than_subtract(self):
        calculator = Calculator()
        calculator.add(5)
        calculator.subtract(3)
        self.assertEqual(-2, calculator.get_result())