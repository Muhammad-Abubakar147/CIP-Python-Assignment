import random

WORDS = ["zebra", "tiger", "camel", "horse", "sheep"]

def wordle():
    correct_word = random.choice(WORDS)

    print("Welcome to Wordle!")

    for i in range(6):
        guess = input("Enter your guess: ").lower()

        result = ""

        for j in range(5):
            if guess[j] == correct_word[j]:
                result += "[" + guess[j] + "] "
            elif guess[j] in correct_word:
                result += "(" + guess[j] + ") "
            else:
                result += guess[j] + " "

        print("Result:", result.strip())

        if guess == correct_word:
            print(f"Congratulations! You guessed the word in {i + 1} tries!")
            return

    print("Better luck next time! The correct word was '" + correct_word + "'.")


wordle()