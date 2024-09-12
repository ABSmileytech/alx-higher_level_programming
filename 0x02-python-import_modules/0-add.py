#!/usr/bin/python3
# 0-import_add.py

from add_0 import add  # Import the add function

a = 1
b = 2

# Use string formatting to display the result
print("{} + {} = {}".format(a, b, add(a, b)))
