def search(messages, word):
    for message in messages:
        if message["role"] != "system" and word.lower() in message["content"].lower():
            print(message["role"] + ":", message["content"])


messages = [system_message]

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    if user_input == "search":
        word = input("Search for: ")
        search(messages, word)
        continue

    messages.append({"role": "user", "content": user_input})

    response = call_gpt(messages)
    print("Bot:", response)

    messages.append({"role": "assistant", "content": response})