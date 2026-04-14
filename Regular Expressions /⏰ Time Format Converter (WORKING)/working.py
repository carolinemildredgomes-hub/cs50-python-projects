import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)",
        s
    )

    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    start_min = match.group(2)
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_min = match.group(5)
    end_period = match.group(6)

    start = time_convert(start_hour, start_min, start_period)
    end = time_convert(end_hour, end_min, end_period)

    return f"{start} to {end}"


def time_convert(hour, minute, period):
    if hour < 1 or hour > 12:
        raise ValueError

    if minute is None:
        minute = 0
    else:
        minute = int(minute)

    if minute < 0 or minute > 59:
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
