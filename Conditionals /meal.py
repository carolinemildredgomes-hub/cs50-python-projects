def main():
    # Prompt the user for a time
    time_str = input("Time: ")

    # Convert time to float hours
    time = convert(time_str)

    # Determine which meal it is
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    # Otherwise, do nothing


def convert(time):
    # Split the string into hours and minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Convert minutes to fraction of an hour
    total_hours = hours + minutes / 60

    return total_hours


if __name__ == "__main__":
    main()
