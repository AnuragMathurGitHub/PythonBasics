import numpy as np

def numpy_operations():
    """
    Demonstrate basic NumPy array operations.
    This function creates a NumPy array and performs various operations
    such as addition, multiplication, and calculating statistics.
    Returns:
        None
    """
    # Create an array
    arr = np.array([1, 2, 3, 4, 5])

    # Basic operations
    print("Array + 10:", arr + 10)  # Add 10 to every element
    print("Array * 2:", arr * 2)  # Multiply every element by 2

    # Array Statistics
    print("Sum:", arr.sum())
    print("Mean:", arr.mean())
    print("Max:", arr.max())
    print("Min:", arr.min())

if __name__ == '__main__':
    numpy_operations()
