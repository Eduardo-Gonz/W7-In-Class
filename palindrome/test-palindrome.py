import unittest
import palindrome


class TestPalindrome(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(palindrome.is_palindrome("racecar"), "This is a palindrome!")
        self.assertEqual(palindrome.is_palindrome("level"), "This is a palindrome!")
        self.assertEqual(palindrome.is_palindrome("kevin"), "Not a palindrome!")
        self.assertEqual(palindrome.is_palindrome("cool pencil"), "Not a palindrome!")
    def test_edge(self):
        with self.subTest(msg="Empty String"):
            self.assertEqual(palindrome.is_palindrome(""), "This is a palindrome!")
        with self.subTest(msg="numbers"):
            self.assertEqual(palindrome.is_palindrome(10), TypeError)


if __name__ == "__main__":
    unittest.main()