def letter_to_shift(key):
    return ord(key.lower()) - ord('a')


def encode(message, shift):
    encoded = ""

    for char in message:
        if char.isalpha():
            encoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded += char

    return encoded


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    key = input("Enter a key letter: ")

    shift = letter_to_shift(key)
    secret = encode(message, shift)

    print(f"Secret: {secret}")


if __name__ == "__main__":
    main()