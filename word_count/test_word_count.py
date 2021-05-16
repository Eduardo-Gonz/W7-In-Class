from typing import Type
import unittest
import word_count


class TestWordCount(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(word_count.count_words("This is an activity"), 4)
        self.assertEqual(word_count.count_words("Feel the rain on your skin."), 6)
        self.assertEqual(word_count.count_words("This is a complete sentence, isn't it?"), 7)
    
    def test_edge(self):
        with self.subTest(msg="Empty String"):
            self.assertEqual(word_count.count_words(""), 0)
        with self.subTest(msg="Numbers"):
            self.assertEqual(word_count.count_words(71), 0)
    

if __name__ == "__main__":
    unittest.main()