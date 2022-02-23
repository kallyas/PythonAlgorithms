from conversions.decimal_to_binary import decimal_to_binary

def test_decimal_to_binary():
    assert decimal_to_binary("0") == "0"
    assert decimal_to_binary("1") == "1"
    assert decimal_to_binary("2") == "10"
    assert decimal_to_binary("3") == "11"
    assert decimal_to_binary("4") == "100"
    assert decimal_to_binary("5") == "101"
    assert decimal_to_binary("6") == "110"
    assert decimal_to_binary("7") == "111"
    assert decimal_to_binary("8") == "1000"
    assert decimal_to_binary("9") == "1001"
    assert decimal_to_binary("10") == "1010"

def test_decimal_to_binary_invalid():
    assert not decimal_to_binary("a")
    assert not decimal_to_binary("2w")
    assert not decimal_to_binary("1.2")

def test_binary_to_decimal_empty():
    assert not decimal_to_binary("")
