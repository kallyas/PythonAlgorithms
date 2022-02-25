import unittest
from maths import *

class TestMaths(unittest.TestCase):

    def test_absolute_max_positives(self):
        self.assertEqual(absolute_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(absolute_max([345, 100, 679, 234, 567]), 679)

    def test_absolute_max_negatives(self):
        self.assertEqual(absolute_max([-1, -2, -3, -4, -5]), 5)
        self.assertEqual(absolute_max([-345, -100, -679, -234, -567]), 679)

    def test_absolute_max_mixed(self):
        self.assertEqual(absolute_max([-1, 2, -3, 4, -5]), 5)
        self.assertEqual(absolute_max([-345, 100, -679, 234, -567]), 679)

    def test_absolute_max_empty(self):
        self.assertRaises(ValueError, absolute_max, [])

    def test_absolute_max_one_element(self):
        self.assertEqual(absolute_max([-1]), 1)
        self.assertEqual(absolute_max([1]), 1)

    def test_absolute_max_one_element_zero(self):
        self.assertEqual(absolute_max([0]), 0)

    def test_absolute_max_invalid_type(self):
        self.assertRaises(ValueError, absolute_max, [1, 'a'])

    def test_absolute_min_positives(self):
        self.assertEqual(absolute_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(absolute_min([345, 100, 679, 234, 567]), 100)

    def test_absolute_min_negatives(self):
        self.assertEqual(absolute_min([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(absolute_min([-345, -100, -679, -234, -567]), -679)

    def test_absolute_min_mixed(self):
        self.assertEqual(absolute_min([-1, 2, -3, 4, -5]), -5)
        self.assertEqual(absolute_min([-345, 100, -679, 234, -567]), -679)

    def test_absolute_min_empty(self):
        self.assertRaises(ValueError, absolute_min, [])

    def test_absolute_min_one_element(self):
        self.assertEqual(absolute_min([-1]), -1)
        self.assertEqual(absolute_min([1]), 1)

    def test_absolute_min_one_element_zero(self):
        self.assertEqual(absolute_min([0]), 0)

    def test_absolute_min_invalid_type(self):
        self.assertRaises(ValueError, absolute_min, [1, 'a'])

    def test_check_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(199))
        self.assertTrue(is_prime(71))

    def test_check_is_prime_fail(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(200))
        self.assertFalse(is_prime(301))

    def test_check_is_prime_non_integer(self):
        self.assertRaises(ValueError, is_prime, 'a')
        self.assertRaises(ValueError, is_prime, 1.5)

    def test_check_is_prime_negative(self):
        self.assertFalse(is_prime(-1))

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative_number(self):
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, -342)

    def test_factorial_non_integer(self):
        self.assertRaises(ValueError, factorial, 're')


    def test_fast_exponential(self):
        self.assertEqual(fast_exponential(2, 0), 1)
        self.assertEqual(fast_exponential(2, 5), 32)
        self.assertEqual(fast_exponential(10, 20), pow(10, 20))

    def test_fast_exponential_with_negative_exponent(self):
        self.assertEqual(fast_exponential(2, -5), pow(2, -5))
        self.assertEqual(fast_exponential(10, -20), pow(10, -20))

    def test_fast_exponential_non_integer(self):
        self.assertRaises(ValueError, fast_exponential, 'q', 'd')

    def test_perfect_square(self):
        self.assertTrue(is_perfect_square(4))

if __name__ == '__main__':
    unittest.main()