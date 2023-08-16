def calculate_emptying_time(length, width, height, pump_flow_rate):
  """
  Calculates the time it takes to empty a rectangular swimming pool.

  Args:
    length: The length of the swimming pool in meters.
    width: The width of the swimming pool in meters.
    height: The height of the swimming pool in meters.
    pump_flow_rate: The flow rate of the pump in cubic meters per hour.

  Returns:
    The time it takes to empty the swimming pool in hours.
  """

  pool_volume = length * width * height
  emptying_time = pool_volume / pump_flow_rate

  return emptying_time


if __name__ == "__main__":
  length = 12
  width = 7
  height = 2
  pump_flow_rate = 17

  emptying_time = calculate_emptying_time(length, width, height, pump_flow_rate)

  print("It will take {} hours to empty the swimming pool.".format(emptying_time))
