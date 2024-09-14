#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
  """
  Deletes the item at a specific position in a list (if valid).

  Args:
      my_list (list, optional): The list to modify. Defaults to [].
      idx (int, optional): The index of the item to delete. Defaults to 0.

  Returns:
      A new list with the item at the specified index deleted (if valid), 
      or the original list if the index is invalid.
  """
  # Ensure list length and valid index
  if not my_list or idx < 0 or idx >= len(my_list):
    return my_list  # Return original list for invalid index

  new_list = []
  for i in range(len(my_list)):
    # Skip the element at the specified index
    if i != idx:
      new_list.append(my_list[i])
  return new_list

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
