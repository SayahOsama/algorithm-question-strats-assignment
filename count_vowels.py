
import unittest

def is_vowel(c):
    vowels = set(['a','e','i','o','u'])
    return c in vowels

def is_consonant(c):
    return not is_vowel(c) 
    
def count_vowels(str):
    count = 0
    for c in str.lower():
        if c.isalpha():
            if is_vowel(c):
                count += 1
    return count

def count_consonants(str):
    count = 0
    for c in str.lower():
        if c.isalpha():
            if is_consonant(c):
                count += 1
    return count

class TestCountFunctions(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)  # 'e', 'o'
        self.assertEqual(count_vowels("HELLO"), 2)  # 'E', 'O'
        self.assertEqual(count_vowels("world"), 1)  # 'o'
        self.assertEqual(count_vowels(""), 0)       # empty string
        self.assertEqual(count_vowels("12345"), 0) # no vowels
        self.assertEqual(count_vowels("aeiou"), 5) # all vowels
        self.assertEqual(count_vowels("AEIOU"), 5) # all vowels, uppercase

    def test_count_consonants(self):
        self.assertEqual(count_consonants("hello"), 3)  # 'h', 'l', 'l'
        self.assertEqual(count_consonants("HELLO"), 3)  # 'H', 'L', 'L'
        self.assertEqual(count_consonants("world"), 4)  # 'w', 'r', 'l', 'd'
        self.assertEqual(count_consonants(""), 0)       # empty string
        self.assertEqual(count_consonants("12345"), 0) # no consonants
        self.assertEqual(count_consonants("bcdfgh"), 6) # all consonants
        self.assertEqual(count_consonants("BCDFGH"), 6) # all consonants, uppercase

if __name__ == "__main__":
    unittest.main()