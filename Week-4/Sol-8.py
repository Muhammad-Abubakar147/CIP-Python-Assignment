LETTERS = ["a", "c", "e", "i", "o", "t"]
EMOJIS = ["🍎", "🐱", "🥚", "🍦", "🐙", "🌮"]


def build_alphabet(letters, emojis):
    emoji_dict = {}

    for i in range(len(letters)):
        emoji_dict[letters[i]] = emojis[i]

    return emoji_dict


def print_emoji_dict(emoji_dict):
    for letter, emoji in emoji_dict.items():
        print(f"{letter}: {emoji}")


def main():
    alphabet = build_alphabet(LETTERS, EMOJIS)
    print_emoji_dict(alphabet)


if __name__ == "__main__":
    main()