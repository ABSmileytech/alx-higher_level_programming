#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
  """
  Adds corresponding elements of two tuples and returns a new tuple.

  Args:
      tuple_a (tuple, optional): The first tuple. Defaults to ().
      tuple_b (tuple, optional): The second tuple. Defaults to ().

  Returns:
      A new tuple containing the sum of corresponding elements.
  """
  # Handle tuples with less than 2 elements
  len_a = min(len(tuple_a), 2)  # Use at most the first 2 elements of tuple_a
  len_b = min(len(tuple_b), 2)  # Use at most the first 2 elements of tuple_b

  # Create the new tuple with element-wise sums, using 0 for missing values
  new_tuple = tuple(a + (b if len_b > i else 0) for i, a in enumerate(tuple_a[:len_a]))

  return new_tuple

# Example usage
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
