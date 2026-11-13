name = input("What's your name? ")

if name.lower() == "sam":
    print(f"Welcome, VIP {name.upper()}! The red carpet is ready for you.")
else:
    print(f"Welcome, {name}!")

animal = "zebra"

print("I am thinking of an animal. Can you guess what animal it is?")

question = input("Ask me a yes or no question: ")

while question.lower() != "is it a zebra?":
    print("No.")
    question = input("Ask me a yes or no question: ")

print("Correct! 🦓")