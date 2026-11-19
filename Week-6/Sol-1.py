from ai import call_gpt


def main():
    print("Chat with the bot! (press Enter to quit)")

    while True:
        message = input("You: ")

        if message == "":
            break

        reply = call_gpt(message)
        print("Bot: " + reply)


if __name__ == "__main__":
    main()