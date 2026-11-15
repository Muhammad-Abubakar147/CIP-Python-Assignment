import random

def main():
    correct_count = 0
    total_problems = 0
    total_correct = 0

    print("Khansole Academy")

    while correct_count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        answer = int(input(f"What is {num1} + {num2}? "))

        correct_answer = num1 + num2

        total_problems += 1

        if answer == correct_answer:
            correct_count += 1
            total_correct += 1

            print(f"Correct! You've gotten {correct_count} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {correct_answer}")
            correct_count = 0

    print("Congratulations! You mastered addition.")
    print(f"You tried {total_problems} problems and got {total_correct} right.")


if __name__ == "__main__":
    main()