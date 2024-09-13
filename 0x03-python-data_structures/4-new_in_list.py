#!/usr/bin/python3

def new_in_list(my_list, idx, element):
  """
  Creates a new list with an element replaced at a specific position, similar to C-style replacement.

  Args:
      my_list (list): The original list.
      idx (int): The index of the element to replace.
      element: The new element to insert at the specified index.

  Returns:
      A new list with the replacement applied, or a copy of the original list if the index is invalid.
  """
  new_list = my_list.copy()  # Create a copy to avoid modifying the original
  length = len(new_list)
  if idx < 0 or idx >= length:
    return new_list  # Return copy if index is invalid
  new_list[idx] = element
  return new_list

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
