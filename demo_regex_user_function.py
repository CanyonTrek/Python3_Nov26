#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a resuable USER
# function with parameter passing
"""
    DocString
"""
import re

# Example of a User function with optional parameter passing
# and default values and annotations.
def search_pattern(pattern:str = r"^.{19}$", file:str = r"f:\labs\words")->None:
    fh_in = open(file, mode="rt")
    reobj = re.compile(pattern) # PRE-Compiles PATTERN ONLY ONCE

    for line in fh_in:
        m = reobj.search(line) # USE precompiled pattern
        if m:
            print(f"Matched {line.rstrip()}")
    fh_in.close()
    return None

search_pattern()
search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")