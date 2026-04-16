from datetime import date
from seasons import convert_to_words


def test_one_year():
    birth = date(2025, 4, 16)
    today = date(2026, 4, 16)

    assert convert_to_words(birth, today) == "Five hundred twenty-five thousand, six hundred minutes"


def test_one_day():
    birth = date(2026, 4, 15)
    today = date(2026, 4, 16)

    assert convert_to_words(birth, today) == "One thousand, four hundred forty minutes"
