#!/usr/bin/python3
def print_list_integer(my_list=[]):
  """
  Prints all integers in a list, one per line.

  Args:
    my_list (list, optional): The list to print integers from. Defaults to [].
  """
  for num in my_list:
    print("{:d}".format(num))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
