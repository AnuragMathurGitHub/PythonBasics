# Function to check if a string or number is a palindrome
def is_palindrome(s):
    """
    Check if a given string or number is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, 
    and capitalization).

    Parameters:
    s (str or int): The string or number to check.

    Returns:
    bool: True if the string or number is a palindrome, False otherwise.
    """
    import re
    s = str(s)
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    test_cases = ["madam", "hello", "racecar", "python", "level", 12321, 12345, "A man, a plan, a canal, Panama", "No 'x' in Nixon"]
    
    for case in test_cases:
        result = is_palindrome(case)
        print(f"Input: {case}")
        print(f"Output: {result}")
        print()

    # User input
    user_input = input("Enter a string or number to check if it's a palindrome: ")
    if user_input.isdigit():
        user_input = int(user_input)
    result = is_palindrome(user_input)
    print(f"Is '{user_input}' a palindrome? {result}")
