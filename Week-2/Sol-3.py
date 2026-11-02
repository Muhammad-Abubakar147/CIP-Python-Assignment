
import random

def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)

        correct_answer = num1 + num2

        print(f"What is {num1} + {num2}?")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            print(f"The expected answer is {correct_answer}")
            correct_in_a_row = 0

    print("Congratulations! You mastered addition.")


if __name__ == "__main__":
    main()
