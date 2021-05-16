def count_words(str):
    wordCount = len(str.split())

    return wordCount


def prompt_user():
    userInput = input("Enter a string to check how many words it has: ")

    print(count_words(userInput))

    return 0