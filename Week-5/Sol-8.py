def decode(message, shift):
    decoded = ""

    for char in message:
        if char.isalpha():
            decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decoded += char

    return decoded


def crack(message):
    for shift in range(1, 26):
        decoded = decode(message, shift)
        print(f"Shift {shift}: {decoded}")


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    crack(message)


if __name__ == "__main__":
    main()