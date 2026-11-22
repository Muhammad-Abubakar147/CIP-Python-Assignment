def encode(message, shift):
    encoded = ""

    for char in message:
        if char.isalpha():
            encoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded += char

    return encoded


def double_lock(message, n):
    first_lock = encode(message, n)
    second_lock = encode(first_lock, n)

    return second_lock


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    shift = int(input("Enter a shift: "))

    secret = double_lock(message, shift)

    print(f"Double-locked message: {secret}")


if __name__ == "__main__":
    main()