#!/usr/bin/python3

def max_integer(my_list=[]):
  """
  Finds the biggest integer in a list.

  Args:
      my_list (list, optional): The list of integers to search. Defaults to [].

  Returns:
      The biggest integer in the list, or None if the list is empty.
  """
  if not my_list:
    return None  # Return None for empty list

  # Initialize with the first element as a starting point
  max_value = my_list[0]
  for element in my_list[1:]:  # Start from the second element
    if element > max_value:
      max_value = element

  return max_value

# Example usage
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
