animal = "elephant"
gpt_response = ""

print("I am thinking of an animal. Can you guess what animal it is?")

while gpt_response != "Correct!":
    question = input("Ask me a yes or no question: ")
    gpt_response = input("GPT response: ")

print("Correct!")