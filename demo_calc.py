#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a simple user function using
# a Lambda function (rather than the def statement)
""" 
    DocString
"""

def add(x, z):
    """ Return SUM of x and z as a float """
    return float(x+z)

def mul(x, z):
    """ Return PRODUCT of x and z as a float """
    return float(x*z)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")

# ALTERNATIVE to defining a SIMPLE user function when its only
# going to be used ONCE only!
print(f"4 + 3 = {(lambda x, z:float(x+z))(4, 3)}")
