def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
    # Rule 1: length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: first two characters must be letters
    if not s[:2].isalpha():
        return False

    # Rule 3, 4, 5
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif not char.isalpha():
            return False
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()
