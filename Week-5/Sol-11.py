import random

def encode(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decode(message, shift):
    return encode(message, -shift)


def crack(message):
    for shift in range(26):
        decoded = decode(message, shift)
        print(f"Shift {shift}: {decoded}")


def spy_message(topic):
    prompt = f"Write a short secret spy message about {topic}. Use lowercase letters."
    return call_gpt(prompt)


def main():
    print("Welcome to the Code Machine!")

    topic = input("Enter a topic: ")

    message = spy_message(topic)
    shift = random.randint(1, 25)

    secret = encode(message, shift)

    print(f"Secret briefing: {secret}")

    input("Can anyone crack it? Press enter to find out.")

    crack(secret)


if __name__ == "__main__":
    main()