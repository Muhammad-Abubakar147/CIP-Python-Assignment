animal = "zebra"

print("I am thinking of an animal. Can you guess what animal it is?")

question = input("Ask me a yes or no question: ")

while question.lower() != "is it a zebra?":
    if question.lower() == "hint":
        print("It has black and white stripes.")
    else:
        print("No.")

    question = input("Ask me a yes or no question, or type hint: ")

print("Correct! 🦓")