def reverse_dict(emoji_dict):
    reversed_dict = {}

    for word, emoji in emoji_dict.items():
        reversed_dict[emoji] = word

    return reversed_dict


def main():
    emoji_dict = {}

    print("Let's build your emoji dictionary!")
    print("Press enter when you are done.")

    while True:
        word = input("Word: ").lower()

        if word == "":
            break

        emoji = input(f"Emoji for {word}: ")
        emoji_dict[word] = emoji

    print(f"Words in your dictionary: {len(emoji_dict)}")

    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")

    reverse = reverse_dict(emoji_dict)

    while True:
        message = input("Enter an emoji message: ")

        translated_words = []

        for emoji in message.split():
            word = reverse.get(emoji, emoji)
            translated_words.append(word)

        print(" ".join(translated_words))


if __name__ == "__main__":
    main()