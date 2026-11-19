
from ai import call_gpt

INDENT = "    "


def make_message(role, content):
    return {
        "role": role,
        "content": content
    }


def peek(messages):
    print(f"{INDENT}The record has {len(messages)} messages:")

    for message in messages:
        role = message["role"]
        content = message["content"]
        print(f"{INDENT}{role}: {content}")


def format_messages(messages):
    conversation = ""

    for message in messages:
        if message["role"] == "user":
            conversation += "User: " + message["content"] + "\n"
        else:
            conversation += "Assistant: " + message["content"] + "\n"

    conversation += "Assistant:"
    return conversation


def main():
    print("Chat with the bot! (press Enter to quit)")

    messages = []

    while True:
        message = input("You: ")

        if message == "":
            break

        if message == "peek":
            peek(messages)
            continue

        messages.append(make_message("user", message))

        prompt = format_messages(messages)
        reply = call_gpt(prompt)

        messages.append(make_message("assistant", reply))

        print("Bot: " + reply)


if __name__ == "__main__":
    main()
