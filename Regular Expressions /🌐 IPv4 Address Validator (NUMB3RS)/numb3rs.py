import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Check basic format
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False

    # Split by dots
    parts = ip.split(".")

    # Must have exactly 4 parts
    if len(parts) != 4:
        return False

    for part in parts:
        # No leading zeros allowed
        if len(part) > 1 and part[0] == "0":
            return False

        # Must be between 0 and 255
        if int(part) < 0 or int(part) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
