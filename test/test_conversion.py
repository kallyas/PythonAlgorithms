import unittest

from conversion import *

class TestConversions(unittest.TestCase):


    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary('8'), '1000')
        self.assertEqual(decimal_to_binary('10'), '1010')
        self.assertEqual(decimal_to_binary('15'), '1111')

    def test_decimal_to_binary_invalid(self):
        self.assertRaises(ValueError, decimal_to_binary, 'abc')
        self.assertRaises(ValueError, decimal_to_binary, '1.5')
        self.assertRaises(ValueError, decimal_to_binary, '-1')

    def test_decimal_to_binary_empty(self):
        self.assertRaises(ValueError, decimal_to_binary, '')

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1000'), 8)
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('1111'), 15)

    def test_binary_to_decimal_invalid(self):
        self.assertRaises(ValueError, binary_to_decimal, 'abc')
        self.assertRaises(ValueError, binary_to_decimal, '1.5')
        self.assertRaises(ValueError, binary_to_decimal, '-1')

    def test_binary_to_decimal_empty(self):
        self.assertRaises(ValueError, binary_to_decimal, '')

    def test_hexa_decimal_to_decimal(self):
        self.assertEqual(hexa_decimal_to_decimal('A'), 10)
        self.assertEqual(hexa_decimal_to_decimal('F'), 15)
        self.assertEqual(hexa_decimal_to_decimal('1'), 1)

    def test_hexa_decimal_to_decimal_invalid(self):
        self.assertRaises(ValueError, hexa_decimal_to_decimal, 'abc')
        self.assertRaises(ValueError, hexa_decimal_to_decimal, '1.5')
        self.assertRaises(ValueError, hexa_decimal_to_decimal, '-1')

    def test_hexa_decimal_to_decimal_empty(self):
        self.assertRaises(ValueError, hexa_decimal_to_decimal, '')

    def test_decimal_to_hexa(self):
        self.assertEqual(decimal_to_hexa(10), 'A')
        self.assertEqual(decimal_to_hexa(15), 'F')
        self.assertEqual(decimal_to_hexa(1), '1')

    def test_decimal_to_hexa_invalid(self):
        self.assertRaises(ValueError, decimal_to_hexa, 'abc')
        self.assertRaises(ValueError, decimal_to_hexa, '1.5')
        self.assertRaises(ValueError, decimal_to_hexa, '-1')

    def test_decimal_to_hexa_empty(self):
        self.assertRaises(ValueError, decimal_to_hexa, '')

    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal('43'), 35)
        self.assertEqual(octal_to_decimal('10'), 8)
        self.assertEqual(octal_to_decimal('15'), 13)

    def test_octal_to_decimal_invalid(self):
        self.assertRaises(ValueError, octal_to_decimal, 'abc')
        self.assertRaises(ValueError, octal_to_decimal, '1.5')
        self.assertRaises(ValueError, octal_to_decimal, '-1')

    def test_octal_to_decimal_empty(self):
        self.assertRaises(ValueError, octal_to_decimal, '')

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal('8'), '10')
        self.assertEqual(decimal_to_octal('10'), '12')
        self.assertEqual(decimal_to_octal('175'), '257')

    def test_decimal_to_octal_invalid(self):
        self.assertRaises(ValueError, decimal_to_octal, 'abc')
        self.assertRaises(ValueError, decimal_to_octal, '1.5')
        self.assertRaises(ValueError, decimal_to_octal, '-1')

    def test_decimal_to_octal_empty(self):
        self.assertRaises(ValueError, decimal_to_octal, '')


if __name__ == '__main__':
    unittest.main()