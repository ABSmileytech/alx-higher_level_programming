#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
  """
  Prints all integers of a list in reverse order, one per line.

  Args:
      my_list (list, optional): The list to print integers from. Defaults to [].
  """
  # Loop through the list in reverse order
  for num in reversed(my_list):
    print("{:d}".format(num))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
