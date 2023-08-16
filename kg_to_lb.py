def kilogram_to_pound(kilograms):
  """Converts a kilogram to a pound.

  Args:
    kilograms: The weight in kilograms.

  Returns:
    The weight in pounds.
  """

  pounds = kilograms * 2.20462262185

  return pounds


# Get the weight in kilograms from the user.
kilograms = float(input("Enter the weight in kilograms: "))

# Convert the weight to pounds.
pounds = kilogram_to_pound(kilograms)

# Print the weight in pounds.
print(f"The weight in pounds is: {pounds}")