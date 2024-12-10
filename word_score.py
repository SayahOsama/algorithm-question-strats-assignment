import unittest


def high_score_word(s):
    
    def word_score(word):
            return sum(ord(char) - ord('a') + 1 for char in word)

    words = s.split()

    highest_word = ""
    highest_score = 0

    for word in words:
        score = word_score(word)
        if score > highest_score:
            highest_word = word
            highest_score = score
            print("highest word:",highest_word, "highest score:", highest_score)
        elif score == highest_score:
            continue

    return highest_word

class TestHighScoreWord(unittest.TestCase):
    
    def test_high_score_word(self):
        # Test cases with different words and their scores
        self.assertEqual(high_score_word("man bat dog"), "man")  # 'man' -> 28, 'bat' -> 23, 'dog' -> 26
        self.assertEqual(high_score_word("hello world python"), "python")  # 'python' -> 98
        self.assertEqual(high_score_word("apple banana kiwi"), "kiwi")  # 'apple' -> 50, 'banana' -> 54, 'kiwi' -> 49
        self.assertEqual(high_score_word("zebra fox"), "zebra")  # 'zebra' -> 72, 'fox' -> 42
        self.assertEqual(high_score_word("a aa aaa aaaa"), "aaaa")  # 'aaaa' -> 4, 'aaa' -> 3, 'aa' -> 2, 'a' -> 1

    def test_tie_case(self):
        # Case where multiple words have the same score, should return the first one
        self.assertEqual(high_score_word("abc acb bac"), "abc")  # All words have score 6, return the first

    def test_single_word(self):
        # Case where there is only one word
        self.assertEqual(high_score_word("hello"), "hello")  # Only one word

    def test_empty_string(self):
        # Case with an empty string
        self.assertEqual(high_score_word(""), "")  # No words, return empty string

if __name__ == "__main__":
    unittest.main()