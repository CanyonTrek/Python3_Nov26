#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module contains basic functions for a calc app
""" 
    Basic Calc Functions - including add, mul and div
"""
import sys

def add(*args):
    """ Return SUM of all arguments as a float
    >>> add(4, 3, 2, 1)
    10.0
    >>> add(30, 20)
    50.0
    """
    total = 0
    for num in args:
        total += num
    return float(total)

def mul(*args):
    """ Return PRODUCT of all arguments as a float
    >>> mul(4, 3, 2)
    24.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return quotient of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("------------- Basic Calc Examples -------------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 * 1 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("-----------------------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Only EXECUTE if ran directly as a program
    # Ignore if imported as a module
    import doctest
    doctest.testmod()
    main()
    sys.exit(0) # Explicit EXIT with return code (0=success)