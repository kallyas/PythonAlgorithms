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


if __name__ == '__main__':
    unittest.main()