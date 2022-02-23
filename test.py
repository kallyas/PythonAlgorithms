# from conversions import binary_to_decimal as b2d, decimal_to_binary as d2b

from math import factorial
from ciphers.ceaser_cipher import decrypt, encrypt
from ciphers.morse_code import morse_decode, morse_encode
from conversions.binary_to_decimal import binary_to_decimal
from conversions.decimal_to_binary import decimal_to_binary
from conversions.decimal_to_octal import decimal_to_octal
from conversions.hexa_decimal_to_decimal import hexa_decimal_to_decimal
from conversions.decimal_to_hexa import decimal_to_hexa
from conversions.octal_to_decimal import octal_to_decimal
from maths.absolute_max import absolute_max
from maths.absolute_min import absolute_min
from maths.check_prime import is_prime
from maths.fast_exponential import fast_exponential
from maths.perfect_square import is_perfect_square



print(decimal_to_binary("708"))
print(binary_to_decimal("1011000100"))
print(hexa_decimal_to_decimal("1A"))
print(decimal_to_hexa(26))
print(octal_to_decimal("17"))
print(decimal_to_octal("15"))
print(absolute_max([-1, -2, -3, -4, -5]))
print(absolute_min(["-1", "-2", "-3", "-4", "-5"]))
print(is_prime(7))
print(factorial(5))
print(fast_exponential(2, 5))
print(is_perfect_square(16))
print(encrypt("hello", 3))
print(decrypt("khoor", 3))
# print(morse_encode("hello".upper()))
# print(morse_decode("......-...-..---"))