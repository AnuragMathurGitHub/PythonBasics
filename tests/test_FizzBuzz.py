import unittest
from io import StringIO
import sys
from FizzBuzz import play_fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_play_fizz_buzz(self):
        expected_output = (
            "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n"
            "11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\n"
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        play_fizz_buzz()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()