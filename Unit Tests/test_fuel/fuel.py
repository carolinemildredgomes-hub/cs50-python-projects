def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    # Negative values are invalid
    if x < 0 or y < 0:
        raise ValueError

    # Denominator cannot be zero
    if y == 0:
        raise ZeroDivisionError

    # Numerator cannot be greater than denominator
    if x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
