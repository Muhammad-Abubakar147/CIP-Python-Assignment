BOTS = [
    {"name": "Captain Kit", "personality": "You are Captain Kit, a pirate. Keep replies short."},
    {"name": "Chef Rosa", "personality": "You are Chef Rosa, a very dramatic chef. Keep replies short."},
    {"name": "Beep", "personality": "You are Beep, a very literal robot. Keep replies short."},
]

# Display available bots
for i, bot in enumerate(BOTS):
    print(f"{i}: {bot['name']}")

# Ask user to pick a bot
choice = int(input("Pick a bot: "))

selected_bot = BOTS[choice]
bot_name = selected_bot["name"]

messages = [
    {"role": "system", "content": selected_bot["personality"]}
]

print("Chat with the bot! (press Enter to quit)")

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

            print(f"{bot_name}: {response}")

            messages.append({"role": "assistant", "content": response})

    else:
        messages.append({"role": "user", "content": user_input})

        response = call_gpt(messages)

        print(f"{bot_name}: {response}")

        messages.append({"role": "assistant", "content": response})