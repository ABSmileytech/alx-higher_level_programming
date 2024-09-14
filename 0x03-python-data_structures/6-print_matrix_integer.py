#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
  """
  Prints a matrix of integers in a formatted multi-line output.

  Args:
      matrix (list, optional): The matrix of integers to print. Defaults to [].
  """
  # Check if the matrix is empty and handle it gracefully
  if not matrix:
    print()
    return
  for row in matrix:
    # Print each element in a row, separated by a space
    print("{:d} ".format(*row), end="")  # Unpack row elements for formatting
    print()  # New line after each row

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
