#!/usr/bin/python3
import sys
"""  Description:  Calculates the factorial of a number using recursion.  """

def factorial(n):
    if n == 0:
        return 1
    else:
        """
            Parameters: n (int): The number to calculate the factorial of.

            Returns: int: The factorial of the given number.
        """
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

