BOTS = [
    {"name": "Captain Kit", "personality": "You are Captain Kit, a pirate in a group chat. Keep replies short."},
    {"name": "Chef Rosa", "personality": "You are Chef Rosa, a very dramatic chef in a group chat. Keep replies short."},
]

messages = []

print("Chat with the bots! (press Enter to quit)")

while True:
    user_input = input("You: ")

    if user_input == "":
        break

    messages.append({"role": "user", "content": user_input})

    for bot in BOTS:
        system_message = {
            "role": "system",
            "content": bot["personality"]
        }

        bot_messages = [system_message] + messages

        response = call_gpt(bot_messages)

        print(f"{bot['name']}: {response}")

        messages.append({
            "role": "assistant",
            "content": f"{bot['name']}: {response}"
        })