from datetime import date
import sys
import inflect


def main():
    birth = input("Date of Birth: ").strip()

    try:
        year, month, day = map(int, birth.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    print(convert_to_words(birth_date))


def convert_to_words(birth_date, today=None):
    if today is None:
        today = date.today()

    difference = today - birth_date
    minutes = difference.days * 1440

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
