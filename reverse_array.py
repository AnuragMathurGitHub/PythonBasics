# Function to reverse an array
def reverse_array(arr):
    return arr[::-1] 

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print("Original array:", array)
    array.reverse()
    print("reversed array:", array)
    reversed_array = reverse_array(array)
    print("Original array:", array)
    print("Reversed array:", reversed_array)
array.reverse()

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