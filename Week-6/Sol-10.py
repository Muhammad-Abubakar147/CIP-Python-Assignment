messages = [
    {"role": "system", "content": "You are super sassy. Keep replies short."}
]

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    if user_input == "peek":
        print(f"The record has {len(messages)} messages:")
        for message in messages:
            print(f"{message['role']}: {message['content']}")

    elif user_input == "again":
        if len(messages) < 3 or messages[-1]["role"] != "assistant":
            print("Nothing to try again yet.")
        else:
            messages = messages[:-1]

            response = call_gpt(messages)

            print("Bot:", response)

            messages.append({"role": "assistant", "content": response})

    else:
        messages.append({"role": "user", "content": user_input})

        response = call_gpt(messages)

        print("Bot:", response)

        messages.append({"role": "assistant", "content": response})