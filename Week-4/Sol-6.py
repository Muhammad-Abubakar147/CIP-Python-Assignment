def quiz(emoji_dict):
    score = 0

    for word, emoji in emoji_dict.items():
        guess = input(f"What word is {emoji}? ")

        if guess.lower() == word.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Nope, it was {word}.")

    print(f"You got {score} out of {len(emoji_dict)}!")


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

    quiz(emoji_dict)


if __name__ == "__main__":
    main()