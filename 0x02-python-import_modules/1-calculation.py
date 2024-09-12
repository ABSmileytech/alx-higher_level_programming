# 1-calculation.py

from calculator_1 import add, sub, mul, div  # Import multiple functions

a = 10
b = 5

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("{} + {} = {}".format(a, b, result_add))  # Print 1
print("{} - {} = {}".format(a, b, result_sub))  # Print 2
print("{} * {} = {}".format(a, b, result_mul))  # Print 3
print("{} / {} = {}".format(a, b, result_div))  # Print 4
