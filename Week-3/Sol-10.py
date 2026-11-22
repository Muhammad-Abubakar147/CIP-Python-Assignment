import random

WORDS = ["candy", "apple", "grape", "brain", "train"]

def wordle():
    correct_word = random.choice(WORDS)

    print("Welcome to Wordle!")

    guesses = []

    for i in range(6):
        guess = input("Enter your guess: ").lower()

        if guess in guesses:
            print("You already guessed that one!")
            continue

        guesses.append(guess)

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
            print(f"Congratulations! You guessed the word in {len(guesses)} tries!")
            return

    print(f"Better luck next time! The correct word was '{correct_word}'.")


wordle()