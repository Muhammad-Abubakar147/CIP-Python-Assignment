import random

WORDS = ["candy", "apple", "grape", "brain", "train"]

def wordle():
    correct_word = random.choice(WORDS)

    print("Welcome to Wordle!")

    for i in range(6):
        guess = input("Enter your guess: ").lower()

        right_place = 0
        wrong_place = 0

        for j in range(5):
            if guess[j] == correct_word[j]:
                right_place += 1
            elif guess[j] in correct_word:
                wrong_place += 1

        print(f"Right place: {right_place}, wrong place: {wrong_place}")

        if guess == correct_word:
            print(f"Congratulations! You guessed the word in {i + 1} tries!")
            return

    print(f"Better luck next time! The correct word was '{correct_word}'.")


wordle()