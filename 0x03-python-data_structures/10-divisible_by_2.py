#!/usr/bin/python3

def divisible_by_2(my_list=[]):
  """
  Creates a new list with True/False values indicating divisibility by 2.

  Args:
      my_list (list, optional): The list to check for divisibility. Defaults to [].

  Returns:
      A new list with True/False values for divisibility by 2 at each index.
  """
  return [element % 2 == 0 for element in my_list]  # List comprehension

# Example usage
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
