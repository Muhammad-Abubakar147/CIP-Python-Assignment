def food_pack():
    return {
        "pizza": "🍕",
        "taco": "🌮",
        "apple": "🍎"
    }


def animal_pack():
    return {
        "cat": "🐱",
        "dog": "🐶",
        "fish": "🐟"
    }


def main():
    pack = input("Pick a pack (food or animals): ")

    if pack == "food":
        emoji_dict = food_pack()
    elif pack == "animals":
        emoji_dict = animal_pack()
    else:
        print("Invalid pack!")
        return

    print(f"Words in your dictionary: {len(emoji_dict)}")

    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")

    while True:
        sentence = input("Enter a sentence: ")

        words = sentence.split()
        translated = []

        for word in words:
            translated.append(emoji_dict.get(word, word))

        print(" ".join(translated))


if __name__ == "__main__":
    main()