ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def mirror_letter(letter):
    position = ALPHABET.find(letter)
    mirrored_position = 25 - position
    return ALPHABET[mirrored_position]


def mirror(message):
    result = ""

    for char in message:
        if char == " ":
            result += " "
        else:
            result += mirror_letter(char)

    return result


def main():
    print("Welcome to the Code Machine!")
    message = input("Enter a message: ")

    mirrored = mirror(message)
    print(f"Mirrored: {mirrored}")

    mirrored_again = mirror(mirrored)
    print(f"Mirrored again: {mirrored_again}")


if __name__ == "__main__":
    main()