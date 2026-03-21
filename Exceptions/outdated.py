months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        # Format 1: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        # Format 2: Month DD, YYYY
        elif "," in date:
            month_str, rest = date.split(" ", 1)
            day, year = rest.split(",")
            day = int(day.strip())
            year = int(year.strip())

            if month_str not in months:
                continue

            month = months.index(month_str) + 1

        else:
            continue

        # Validate
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except ValueError:
        pass
