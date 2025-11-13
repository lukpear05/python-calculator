import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):


    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
#Add
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(1, 5), 6)
#subtrac
    def test_sub_positive_numbers(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_sub_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-4, -2), -2)
#multipl
    def test_multi_positive_numbers(self):
        self.assertEqual(self.calc.multiply(5, 3),15)

    def test_multi_positive_numbers2(self):
        self.assertEqual(self.calc.multiply(10, 3),30)
#division
    def test_divi_positive_numbers(self):
        self.assertEqual(self.calc.divide(8, 2),4)

    def test_divi_positive_numbers2(self):
        self.assertEqual(self.calc.divide(9, 3),3)
#modulo
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(19, 3), 1)

    def test_modulo_positive_numbers2(self):
        self.assertEqual(self.calc.modulo(12, 3), 0)


if __name__ == '__main__':
    unittest.main()