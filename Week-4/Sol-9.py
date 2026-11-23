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

    print(f"\nWords in your dictionary: {len(emoji_dict)}")

    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")

    while True:
        sentence = input("\nEnter a sentence: ")

        if sentence == "":
            break

        translated_words = []

        for word in sentence.split():
            word = word.lower()

            if word not in emoji_dict:
                prompt = f"Give me one suitable emoji for the word '{word}'. Return only the emoji."
                emoji = call_gpt(prompt)
                emoji_dict[word] = emoji.strip()

            translated_words.append(emoji_dict[word])

        print(" ".join(translated_words))

    print(f"\nWords in your dictionary: {len(emoji_dict)}")

    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")


if __name__ == "__main__":
    main()