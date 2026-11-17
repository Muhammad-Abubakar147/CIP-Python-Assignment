import random

def main():
    correct_in_a_row = 0

    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        if random.choice([True, False]):
            operator = "+"
            answer = num1 + num2
        else:
            operator = "-"
            answer = num1 - num2

        print(f"What is {num1} {operator} {num2}?")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            correct_in_a_row += 1
            print(f"Correct! You've gotten {correct_in_a_row} correct in a row.")
        else:
            print(f"Incorrect. The correct answer was {answer}.")
            print(f"You got {correct_in_a_row} correct in a row.")
            correct_in_a_row = 0

if __name__ == "__main__":
    main()