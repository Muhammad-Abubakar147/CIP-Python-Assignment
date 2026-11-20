def main():
    print("Welcome to Wordle!")

    secret_word = input("Player 1, type a secret 5-letter word: ")

    for i in range(30):
        print()

    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        result = ""

        for i in range(5):
            if guess[i] == secret_word[i]:
                result += "[" + guess[i] + "] "
            elif guess[i] in secret_word:
                result += "(" + guess[i] + ") "
            else:
                result += guess[i] + " "

        print("Result:", result.strip())

        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {attempts} tries!")
            break


if __name__ == "__main__":
    main()