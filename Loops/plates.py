def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Rule 1: length
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: first two must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3 & 4: numbers logic
    number_started = False

    for c in s:

        # Rule 5: only letters and numbers
        if not c.isalnum():
            return False

        if c.isdigit():

            if not number_started:
                number_started = True

                if c == "0":
                    return False

        else:  # c is a letter
            if number_started:
                return False

    return True


main()
