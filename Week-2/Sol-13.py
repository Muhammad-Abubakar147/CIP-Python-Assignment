import random

def main():
    correct_count = 0
    max_number = 10

    print("Khansole Academy")

    while correct_count < 3:

        num1 = random.randint(1, max_number)
        num2 = random.randint(1, max_number)

        answer = int(input(f"What is {num1} + {num2}? "))

        correct_answer = num1 + num2

        if answer == correct_answer:
            correct_count += 1
            max_number *= 10

            print(f"Correct! You've gotten {correct_count} correct in a row.")

        else:
            print(f"Incorrect. The expected answer is {correct_answer}")
            correct_count = 0
            max_number = 10

    print("Congratulations! You mastered addition.")


if __name__ == "__main__":
    main()