import random
from ai import call_gpt

def main():
    correct_count = 0

    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        prompt = f"""
        Create a one-sentence addition word problem using
        these two numbers: {num1} and {num2}.
        Do not include the answer.
        """

        story = call_gpt(prompt)

        print("Khansole Academy")
        answer = int(input(story + " "))

        correct_answer = num1 + num2

        if answer == correct_answer:
            correct_count += 1
            print(f"Correct! You've gotten {correct_count} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {correct_answer}")
            correct_count = 0


if __name__ == "__main__":
    main()