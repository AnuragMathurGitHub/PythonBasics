# Perform the arithmetic operations on the two integers.
def arithmetic_operations(no1, no2):
    """Performs arithmetic operations on two integers.

  Args:
    no1: The first integer.
    no2: The second integer.

  Returns:
    A dictionary containing the results of the arithmetic operations.
  """

    fun_results = {}
    fun_results["addition"] = num1 + num2
    fun_results["subtraction"] = num1 - num2
    fun_results["multiplication"] = num1 * num2
    fun_results["division"] = num1 / num2
    fun_results["floor_division"] = num1 // num2
    fun_results["modulus"] = num1 % num2
    fun_results["exponentiation"] = num1 ** num2

    return fun_results


# Get the two integers from the user.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

results = arithmetic_operations(num1, num2)

# Print the results of the arithmetic operations.
for operation, result in results.items():
    print(f"{operation}: {result}")