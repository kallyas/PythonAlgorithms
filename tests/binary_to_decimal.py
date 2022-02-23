from conversions.binary_to_decimal import binary_to_decimal

# write tests for binary conversion
def test_binary_to_decimal():
    assert binary_to_decimal("0") == 0
    assert binary_to_decimal("1") == 1
    assert binary_to_decimal("10") == 2
    assert binary_to_decimal("11") == 3
    assert binary_to_decimal("100") == 4
    assert binary_to_decimal("101") == 5
    assert binary_to_decimal("110") == 6
    assert binary_to_decimal("111") == 7
    assert binary_to_decimal("1000") == 8
    assert binary_to_decimal("1001") == 9


def test_binary_to_decimal_invalid():
    assert not binary_to_decimal("a")
    assert not binary_to_decimal("1a")
    assert not binary_to_decimal("1.1")
    assert not binary_to_decimal("1.1.1")


def test_binary_to_decimal_empty():
    assert not binary_to_decimal("")




