import unittest

def find_median_char(str):
    if not str:
        return None
    unique_chars = sorted(set(str))
    return unique_chars[len(unique_chars) // 2]


class TestFindMedianChar(unittest.TestCase):
    def test_find_median_char(self):
        self.assertEqual(find_median_char("abc"), "b")  # Median of ['a', 'b', 'c'] is 'b'
        self.assertEqual(find_median_char("zab"), "b")  # Median of ['a', 'b', 'z'] is 'b'
        self.assertEqual(find_median_char("aaabccc"), "b")  # Median of ['a', 'b', 'c'] is 'b'
        self.assertEqual(find_median_char("dabc"), "c")  # Median of ['a', 'b', 'c', 'd'] is 'b' (lower middle of 'b' and 'c')
        self.assertEqual(find_median_char("a"), "a")  # Only one character
        self.assertEqual(find_median_char(""), None)  # Empty string returns None
        self.assertEqual(find_median_char("12345"), "3")  # Median of ['1', '2', '3', '4', '5'] is '3'
        self.assertEqual(find_median_char("Python"), "o")  # Median of ['P', 'h', 'n', 'o', 't', 'y'] is 'o'
        self.assertEqual(find_median_char("PPython"), "o")  # Duplicates do not affect result

    def test_case_sensitivity(self):
        self.assertEqual(find_median_char("aAbBcC"), "a")  # Median of ['A', 'B', 'C', 'a', 'b', 'c'] is 'a'

if __name__ == "__main__":
    unittest.main()