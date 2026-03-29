import sys
import requests


def main():
    # 1. Check command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 2. API request
    try:
        api_key = "3055d130286f7a0168fcfe821f2f7d3d9f4d43703da18637a7e95a2b9abeac58"

        url = "https://rest.coincap.io/v3/assets/bitcoin"

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            sys.exit("API request failed")

        data = response.json()

        price = float(data["data"]["priceUsd"])

    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Error fetching data")

    # 3. Calculate total cost
    total = n * price

    # 4. Output
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
