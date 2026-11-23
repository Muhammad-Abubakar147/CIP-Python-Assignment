def combine(dict1, dict2):
    combined = dict1.copy()
    combined.update(dict2)
    return combined


def get_dictionary(player):
    dictionary = {}

    print(f"Player {player}, build your emoji dictionary!")
    print("Press enter when you are done.")

    while True:
        word = input("Word: ").lower()

        if word == "":
            break

        emoji = input(f"Emoji for {word}: ")
        dictionary[word] = emoji

    return dictionary


def main():
    dict1 = get_dictionary(1)
    dict2 = get_dictionary(2)

    emoji_dict = combine(dict1, dict2)

    print(f"\nWords in your dictionary: {len(emoji_dict)}")

    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")

    while True:
        sentence = input("\nEnter a sentence: ")

        translated_words = []

        for word in sentence.split():
            emoji = emoji_dict.get(word.lower(), word)
            translated_words.append(emoji)

        print(" ".join(translated_words))


if __name__ == "__main__":
    main()