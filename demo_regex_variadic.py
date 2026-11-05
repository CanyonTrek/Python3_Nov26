#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a VARIADIC USER
# function which accepts a VARIABLE number of parameters.
"""
    A collection of user functions for searching file/s for
    patterns using Regular Expressions
"""
import re

# Example of a Variadic Function that allows a variable number
# of parameters and captures them in a TUPLE (RO)
def search_pattern(pattern:str = r"^.{19}$", *files):
    """ Search for Regex patterns in file/s and return lines matched  """
    reobj = re.compile(pattern)  # PRE-Compiles PATTERN ONLY ONCE
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")
        for line in fh_in:
            m = reobj.search(line) # USE precompiled pattern
            if m:
                print(f"Matched {line.rstrip()}")
                lines += 1
        fh_in.close()
    return lines

num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words", r"f:\labs\words2", r"f:\labs\words3")
print(f"Lines returned = {num_lines}")