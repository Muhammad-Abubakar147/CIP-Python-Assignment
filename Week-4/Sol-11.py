messages = [system_message]

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    if user_input == "show":
        print("The record has", len(messages), "messages:")
        for message in messages:
            print(message["role"] + ":", message["content"])
        continue

    messages.append({"role": "user", "content": user_input})

    response = call_gpt(messages)
    print("Bot:", response)

    messages.append({"role": "assistant", "content": response})