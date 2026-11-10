# https://github.com/ManuelCoding/lab10-NS-MM
# Partner 1: Neville Shaw
# Partner 2: Manuel Martinez


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(25,5), 0.5)
        self.assertEqual(logarithm(2, 16), 4)
        self.assertEqual(logarithm(81,9), 0.5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,0)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(-2, -4), 8)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 3), 3/2)
        self.assertEqual(div(4, -2), -2/4)
        self.assertEqual(div(-2, -2), -2/-2)

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, -1), 4)
        self.assertEqual(add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(5, -1), 6)
        self.assertEqual(subtract(-1, -2), 1)

    # def test_log_invalid_base(self): # 1 assertion
    #     with self.assertRaises(ZeroDivisionError):
    #         logarithm(0, 5)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, -12), 13)
        self.assertEqual(hypotenuse(9, -40), 41)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
           square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
