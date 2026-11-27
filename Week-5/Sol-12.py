messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    if user_input == "peek":
        print(f"The record has {len(messages)} messages:")
        for message in messages:
            print(f"{message['role']}: {message['content']}")

    elif user_input == "costume":
        personality = input("New personality: ")

        new_system_message = {
            "role": "system",
            "content": personality
        }

        messages = [new_system_message] + messages[1:]

        print("Costume changed!")

    else:
        messages.append({"role": "user", "content": user_input})

        response = call_gpt(messages)

        print("Bot:", response)

        messages.append({"role": "assistant", "content": response})