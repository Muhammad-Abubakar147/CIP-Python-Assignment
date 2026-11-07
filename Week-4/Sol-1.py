VOWELS = "aeiou"

def hide_vowels(message):
    result = ""

    for letter in message:
        if letter in VOWELS:
            result += "*"
        else:
            result += letter

    return result


def main():
    secret = input("Enter a secret: ")
    result = hide_vowels(secret)
    print(result)


if __name__ == "__main__":
    main()