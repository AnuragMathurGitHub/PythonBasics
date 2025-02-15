def find_average(marks1, marks2, marks3):
    """Finds the average of three marks.

  Args:
    marks1: The mark for the first subject.
    marks2: The mark for the second subject.
    marks3: The mark for the third subject.

  Returns:
    The average of the three marks.
  """

    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    return average_marks


# if __name__ == "__main__":
# Get the marks for the three subjects from the user.
marks1 = float(input("Enter the mark for the first subject: "))
marks2 = float(input("Enter the mark for the second subject: "))
marks3 = float(input("Enter the mark for the third subject: "))

# Find the average of the three marks.
average_marks = find_average(marks1, marks2, marks3)

# Print the average marks.
print(f"The average marks are: {average_marks}")
