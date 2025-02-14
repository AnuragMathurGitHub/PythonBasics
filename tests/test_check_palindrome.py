import unittest
from check_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome(""))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

    def test_mixed_cases(self):
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("RaceCar"))

    def test_with_numbers(self):
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(12345))

if __name__ == "__main__":
    unittest.main()