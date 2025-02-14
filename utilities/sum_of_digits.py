# Function to find the sum of digits of a number
def sum_of_digits(n):
    """
    Calculate the sum of the digits of a given number.

    Parameters:
    n (int): The number to calculate the sum of its digits.

    Returns:
    int: The sum of the digits of the number.
    """
    return sum(int(digit) for digit in str(n))

# Example usage
if __name__ == "__main__":
    test_cases = [123, 456, 789, 0, 111, 999]
    
    for case in test_cases:
        result = sum_of_digits(case)
        print(f"Input: {case}")
        print(f"Output: {result}")
        print()

    # User input
    user_input = int(input("Enter a number to find the sum of its digits: "))
    result = sum_of_digits(user_input)
    print(f"The sum of the digits of {user_input} is {result}")
