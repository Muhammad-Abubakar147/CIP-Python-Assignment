messages = [system_message]

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    if user_input.lower() == "new chat":
        messages = messages[:1]
        print("Started a new chat! The record has", len(messages), "messages.")
        continue

    messages.append({"role": "user", "content": user_input})

    response = call_gpt(messages)
    print("Bot:", response)

    messages.append({"role": "assistant", "content": response})