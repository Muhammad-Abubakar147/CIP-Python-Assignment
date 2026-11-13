animal = "dog"

print("I am thinking of an animal. Can you guess what animal it is?")

question = input("Ask me a yes or no question: ")

while question.lower() != "is it a dog?":
    print("No.")
    question = input("Ask me a yes or no question: ")

print("Correct!")