def main():
    print("Let's build your emoji dictionary! Press enter when you are done.")

    emoji_dict = {}

    while True:
        word = input("Word: ")

        if word == "":
            break

        emoji = input(f"Emoji for {word}: ")
        emoji_dict[word] = emoji

    print(f"Words in your dictionary: {len(emoji_dict)}")

    for word in emoji_dict:
        print(f"{word}: {emoji_dict[word]}")

    while True:
        sentence = input("Enter a sentence: ")

        if sentence == "":
            break

        words = sentence.split()
        translated_words = []

        for word in words:
            translated_words.append(emoji_dict.get(word, word))

        print(" ".join(translated_words))


if __name__ == "__main__":
    main()