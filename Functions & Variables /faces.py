def convert(text):
    # Replace emoticons with emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    # Ask the user for input
    user_input = input()

    # Send the input to convert()
    result = convert(user_input)

    # Print the result
    print(result)


main()
