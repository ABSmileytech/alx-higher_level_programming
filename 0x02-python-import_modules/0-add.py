#!/usr/bin/python3
# 0-import_add.py
if __name__ == "__main__":
    """Print the sum of 1 and 2."""

from add_0 import add  # Import the add function

a = 1
b = 2

# Use string formatting to display the result
print("{} + {} = {}".format(a, b, add(a, b)))
