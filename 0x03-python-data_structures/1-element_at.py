#!/usr/bin/python3
def element_at(my_list, idx):
  """
  Retrieves an element from a list at a specified index, mimicking C-style access.

  Args:
      my_list (list): The list to retrieve an element from.
      idx (int): The index of the element to retrieve.

  Returns:
      The element at the specified index if valid, otherwise None.
  """
  length = len(my_list)
  if idx < 0 or idx >= length:
    return None
  return my_list[idx]

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
