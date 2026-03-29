import inflect

p = inflect.engine()


def main():
    names = []

    while True:
        try:
            name = input("Name: ")
            if name:  # only add non-empty names
                names.append(name)
        except EOFError:
            print()  # ensure final output is on a new line
            break

    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
