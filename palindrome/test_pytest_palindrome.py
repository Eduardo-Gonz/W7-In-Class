import palindrome

def test_valid_input():
    assert palindrome.is_palindrome("redivider") == "This is a palindrome!"
    assert palindrome.is_palindrome("reviver") == "This is a palindrome!"
    assert palindrome.is_palindrome("Oregon State") == "Not a palindrome!"
    assert palindrome.is_palindrome("Picture Frame") == "Not a palindrome!"

def test_edge_input():
    assert palindrome.is_palindrome("race11ecar") == "This is a palindrome!"
    assert palindrome.is_palindrome(["hello"]) == TypeError
