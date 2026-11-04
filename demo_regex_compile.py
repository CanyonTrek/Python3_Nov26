#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text in a file using
# Python str testing and Regex Pattern matching using the re.py module
"""
    DocString
"""
import re
# Open FILE HANDLE for READING in TEXT mode
fh_in = open(r"f:\labs\words", mode="rt")

reobj = re.compile(r"^(.)(.).\2\1$") # PRE-Compiles PATTERN ONLY ONCE

for line in fh_in:
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match lines with 5 CHAR palindromes
    m = reobj.search(line) # USE precompiled pattern
    if m:
        print(f"Matched {m.group()} on {m.string.rstrip()} at {m.start()}-{m.end()}")
