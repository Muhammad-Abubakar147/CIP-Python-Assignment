import random

def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print("Khansole Academy")

    answer = int(input(f"What is {num1} + {num2}? "))

    correct_answer = num1 + num2

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The expected answer is {correct_answer}")


if __name__ == "__main__":
    main()