import unittest
from sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_sum_of_digits(self):
        """
        Test the sum_of_digits function.

        This method tests the sum_of_digits function with various inputs to ensure it
        returns the correct sum of the digits of the given number.

        Test cases:
        - sum_of_digits(123) should return 6
        - sum_of_digits(456) should return 15
        - sum_of_digits(789) should return 24
        - sum_of_digits(0) should return 0
        - sum_of_digits(111) should return 3
        - sum_of_digits(999) should return 27
        """
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(456), 15)
        self.assertEqual(sum_of_digits(789), 24)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(111), 3)
        self.assertEqual(sum_of_digits(999), 27)

if __name__ == "__main__":
    unittest.main()
