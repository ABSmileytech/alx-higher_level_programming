#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
  """
  Replaces an element of a list at a specific position, similar to C-style replacement.

  Args:
      my_list (list): The list to modify.
      idx (int): The index of the element to replace.
      element: The new element to insert at the specified index.

  Returns:
      The original list (unmodified) if the index is invalid, otherwise the modified list.
  """
  length = len(my_list)
  if idx < 0 or idx >= length:
    return my_list  # Don't modify if index is invalid
  my_list[idx] = element
  return my_list

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
