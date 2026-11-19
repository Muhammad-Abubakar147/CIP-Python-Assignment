from ai import call_gpt


def make_message(role, content):
    return {
        "role": role,
        "content": content
    }


def main():
    print("Chat with the bot! (press Enter to quit)")

    messages = []

    while True:
        message = input("You: ")

        if message == "":
            break

        messages.append(make_message("user", message))

        reply = call_gpt(message)

        messages.append(make_message("assistant", reply))

        print("Bot: " + reply)


if __name__ == "__main__":
    main()