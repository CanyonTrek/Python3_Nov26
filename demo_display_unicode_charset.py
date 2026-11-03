#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the entire UNICODE (0-65535) charset
""" 
    DocString
"""

# ITERATE through the Unicode charset USING ITERATOR for loop
for pos in range(0, 65536, 1):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print(" ")