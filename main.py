from vending_machine.VendingMachine import VendingMachine
from utilities.sum_of_digits import sum_of_digits
from utilities.check_palindrome import is_palindrome

def main():
    # Example usage of VendingMachine
    machine = VendingMachine(10, 2)
    try:
        change = machine.buy(3, 10)
        print(f"Change: {change}")
    except ValueError as e:
        print(e)

    # Example usage of sum_of_digits
    number = 12345
    print(f"Sum of digits of {number}: {sum_of_digits(number)}")

    # Example usage of is_palindrome
    word = "racecar"
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

if __name__ == "__main__":
    main()
