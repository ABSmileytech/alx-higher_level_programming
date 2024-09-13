#!/usr/bin/python3

def no_c(my_string):
  """
  Removes all characters 'c' and 'C' from a string.

  Args:
      my_string (str): The string to remove characters from.

  Returns:
      A new string with all 'c' and 'C' characters removed.
  """
  new_string = ""
  for char in my_string:
    if char.lower() != 'c':  # Check lowercase version to remove both 'c' and 'C'
      new_string += char
  return new_string

# Example usage
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
