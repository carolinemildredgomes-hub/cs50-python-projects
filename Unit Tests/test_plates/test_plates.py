from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("HELLO") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("1ABC") == False
    assert is_valid("A1") == False


def test_zero_number():
    assert is_valid("CS05") == False


def test_middle_letter_after_number():
    assert is_valid("AB1C") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("HI!") == False
