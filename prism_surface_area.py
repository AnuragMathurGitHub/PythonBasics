def surface_area_of_prism(a, b, c):
  """Calculates the surface area of a prism.

  Args:
    a: The length of the first side.
    b: The length of the second side.
    c: The length of the third side.

  Returns:
    The surface area of the prism.
  """

  surface_area = 2 * (a * b + b * c + c * a)

  return surface_area


# Get the lengths of the three sides of the prism from the user.
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

# Calculate the surface area of the prism.
surface_area = surface_area_of_prism(a, b, c)

# Print the surface area of the prism.
print(f"The surface area of the prism is: {surface_area}")