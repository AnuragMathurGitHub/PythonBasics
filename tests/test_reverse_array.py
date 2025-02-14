import unittest

def reverse_array(arr):
    return arr[::-1]

def reverse_array_manual(arr):
    """
    Reverses the elements of an array manually.
    This function takes an array as input and returns a new array with the elements
    in reverse order. The original array remains unchanged.
    Parameters:
        arr (list): The array to be reversed.
    Returns:
        list: A new array with the elements in reverse order.
    """
    left = 0
    right = len(arr) - 1
    result = arr.copy()  # Create a copy to preserve original
    
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    
    return result

class TestReverseArray(unittest.TestCase):
    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_array(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_array([]), [])
        self.assertEqual(reverse_array([1]), [1])

    def test_reverse_array_manual(self):
        self.assertEqual(reverse_array_manual([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_array_manual(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(reverse_array_manual([]), [])
        self.assertEqual(reverse_array_manual([1]), [1])

if __name__ == '__main__':
    unittest.main(exit=False)