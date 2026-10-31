
from animal import get_random_animal
from ai import call_gpt


def main():
    animal = get_random_animal()

    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")

    while True:
        question = input("Ask me a yes or no question: ")

        if question.lower() == animal.lower():
            print("Correct!")
            break

        prompt = f"""
        I am thinking of this animal: {animal}.
        The user asks: "{question}"

        Answer only Yes. or No. based on the animal.
        Do not reveal the animal's name.
        """

        answer = call_gpt(prompt)
        print(answer)


if __name__ == "__main__":
    main()
