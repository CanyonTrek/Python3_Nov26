#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through a SEQUENCE
# (str/tuple/list/dict/set) using an ITERATOR for loop
""" 
    DocString
"""
import sys
#              0            1       2         3         4            5
heroes = ['abdul kalam', 'tyson', 'bowie', 'ziggy', 'aladdin', 'billy connolly']

# ITERATE through the names using an ITERATOR for loop
for name in heroes:
    print(name, end="\n")
print("Heroes=", heroes)

# ITERATE through the names using an ITERATOR for loop and modify the list
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes=", heroes)

# ITERATE through the names using an ITERATOR for loop and modify the list
# using  built-in enumerate() function - returns a TUPLE(idx, obj)
for (idx, name) in enumerate(heroes):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes=", heroes)


try:
    sys.exit(0) # Explicit EXIT with return code (0=success, 1-255=error code)
    # sys.exit("Goodbye") # Explicit EXIT (expr -> STDERR, RED), error=1
except SystemExit:
    print("Exiting script..")
    sys.exit(0)