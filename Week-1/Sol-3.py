def main():
    print("Hello! I am an AI joke bot.")
    
    while True:
        answer = input("Do you want to hear a joke? Type yes or no: ")

        if answer == "yes":
            tell_joke()
        elif answer == "no":
            break


def tell_joke():
    print("Why did the scarecrow win an award?")
    print("Because he was outstanding in his field!")


if __name__ == "__main__":
    main()
