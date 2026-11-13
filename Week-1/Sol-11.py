easy_mode = input("Easy mode? Type yes or no: ").lower()

print("I am thinking of an animal. Can you guess what animal it is?")

animal = "zebra"

question = input("Ask me a yes or no question: ")

while question.lower() != "is it a zebra?":
    if easy_mode == "yes":
        print("No, but it lives in Africa.")
    else:
        print("No.")

    question = input("Ask me a yes or no question: ")

print("Correct! 🦓")