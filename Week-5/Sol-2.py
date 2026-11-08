
def build_emoji_dict():
    emoji_dict = {}

    print("Let's build your emoji dictionary! Press enter when you are done.")

    while True:
        word = input("Word: ")

        if word == "":
            break

        emoji = input("Emoji for " + word.lower() + ": ")
        emoji_dict[word.lower()] = emoji

    return emoji_dict


def print_emoji_dict(emoji_dict):
    for word in emoji_dict:
        print(word + ": " + emoji_dict[word])


def translate(sentence, emoji_dict):
    result = ""

    for word in sentence.split():
        lower_word = word.lower()

        if lower_word in emoji_dict:
            result += emoji_dict[lower_word]
        else:
            result += word

        result += " "

    return result


def main():
    emoji_dict = build_emoji_dict()

    print("Words in your dictionary:", len(emoji_dict))

    print_emoji_dict(emoji_dict)

    while True:
        sentence = input("Enter a sentence: ")

        if sentence == "":
            break

        print(translate(sentence, emoji_dict))


if __name__ == "__main__":
    main()
