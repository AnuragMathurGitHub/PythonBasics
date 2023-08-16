def find_speed(distance, time):
  """Finds the speed of an object.

  Args:
    distance: The distance traveled by the object.
    time: The time taken to travel the distance.

  Returns:
    The speed of the object.
  """

  speed = distance / time

  return speed


# Get the distance traveled by the plane from the user.
distance = int(input("Enter the distance in meters: "))

# Get the time taken by the plane to travel the distance from the user.
time = int(input("Enter the time in seconds: "))

# Find the speed of the plane.
speed = find_speed(distance, time)

# Print the speed of the plane.
print(f"The speed of the plane is: {speed} meters per second")

# Convert the speed to kilometers per hour.
speed_kilometers_per_hour = speed * 3600 / 1000

# Print the speed of the plane in kilometers per hour.
print(f"The speed of the plane is: {speed_kilometers_per_hour} kilometers per hour")
