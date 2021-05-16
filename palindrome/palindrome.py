def is_palindrome(str):
    low = 0
    high = len(str) - 1

    while(low < high):
        if(str[low] != str[high]):
            return print("Not a palindrome!")
        low += 1
        high -=1


    return print("This is a palindrome!")



def prompt_user():
    userInput = input("Enter a string to see if it is a palindrome: ")
    
    is_palindrome(userInput)

    return 0



prompt_user()