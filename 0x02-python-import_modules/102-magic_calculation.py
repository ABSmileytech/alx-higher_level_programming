def magic_calculation(a, b):
    from magic_calculation_102 import add, sub  # Import functions

    if a < b:
        c = add(a, b)  # Call add if a is less than b
        for i in range(4, 6):  # Loop 4 times, i from 4 to 5
            c = add(c, i)  # Add i to c in each loop iteration
        return c  # Return the final value of c
    else:
        return sub(a, b)  # Call sub if a is not less than b

    # This line (LOAD_CONST None) is unreachable in the bytecode
    # due to the previous return statements. We can omit it.
