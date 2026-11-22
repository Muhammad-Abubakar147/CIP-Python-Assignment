def decode(message, shift):
    decoded = ""

    for char in message:
        if char.isalpha():
            decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decoded += char

    return decoded


def crack(message, word):
    for shift in range(26):
        decoded = decode(message, shift)

        if word.lower() in decoded.lower():
            print(f"Shift {shift}: {decoded}")


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")
    word = input("A word you think is in it: ")

    crack(message, word)


if __name__ == "__main__":
    main()