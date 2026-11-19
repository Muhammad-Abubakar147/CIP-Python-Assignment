
from ai import call_gpt

INDENT = "    "
MAX_WORDS = 150

PERSONALITY = "You are a friendly Python tutor. Explain programming concepts in simple language, use short examples, and keep your replies short."


def make_message(role, content):
    return {
        "role": role,
        "content": content
    }


def peek(messages):
    visible_messages = [m for m in messages if m["role"] != "system"]

    print(f"{INDENT}The record has {len(visible_messages)} messages:")

    for message in visible_messages:
        role = message["role"]
        content = message["content"]
        print(f"{INDENT}{role}: {content}")


def format_messages(messages):
    conversation = ""

    for message in messages:
        role = message["role"]
        content = message["content"]

        if role == "system":
            conversation += "Instructions: " + content + "\n\n"
        elif role == "user":
            conversation += "User: " + content + "\n"
        else:
            conversation += "Assistant: " + content + "\n"

    conversation += "Assistant:"
    return conversation


def rewind(messages):
    if len(messages) < 3:
        return messages

    return messages[:-2]


def count_words(messages):
    total = 0

    for message in messages:
        total += len(message["content"].split())

    return total


def forget(messages):
    if len(messages) < 6:
        return messages

    return messages[:1] + messages[5:]


def compact(messages):
    if len(messages) < 3:
        return messages

    old_messages = messages[1:len(messages) - 1]

    instruction = (
        "Summarize this conversation in two or three sentences. "
        "Keep names and anything the user said about themselves.\n\n"
    )

    summary = call_gpt(instruction + format_messages(old_messages))

    return [
        messages[0],
        make_message(
            "system",
            "Summary of the conversation so far: " + summary
        ),
        messages[-1]
    ]


def main():
    print("Chat with the bot! (press Enter to quit)")

    messages = [make_message("system", PERSONALITY)]

    while True:
        message = input("You: ")

        if message == "":
            break

        if message == "peek":
            peek(messages)
            continue

        if message == "rewind":
            messages = rewind(messages)
            print(f"{INDENT}Rewound! The record has {len(messages)} messages.")
            continue

        messages.append(make_message("user", message))

        if count_words(messages) > MAX_WORDS:
            words = count_words(messages)

            choice = input(
                f"{INDENT}My memory is full ({words} words)! "
                "Type 'forget' or 'compact': "
            )

            if choice == "compact":
                messages = compact(messages)
            else:
                messages = forget(messages)

            words = count_words(messages)

            print(
                f"{INDENT}Now I remember "
                f"{len(messages)} messages, {words} words."
            )

        prompt = format_messages(messages)
        reply = call_gpt(prompt)

        messages.append(make_message("assistant", reply))

        print("Bot: " + reply)


if __name__ == "__main__":
    main()
