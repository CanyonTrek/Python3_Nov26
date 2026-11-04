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

# ITERATE through the file handle..
for line in fh_in:
    # Example of Str Testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"^the", line) # Match lines START with 'the'
    # m = re.search(r"ing$", line)  # Match lines ENDING with 'ing'
    # m = re.search(r"^ring$", line)  # Match lines ONLY with 'ring'
    # m = re.search(r"^.ing$", line)  # Match lines of 4 chars ENDING 'ing'
    # m = re.search(r"^[adrp]ing$", line)  # As above but start with [adrp]
    # m = re.search(r"^...................$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"^...................", line)  # Match lines AT LEAST 19 chars
    # m = re.search(r"^[A-Z]", line)  # Match lines START with a CAPITAL
    # m = re.search(r"\.", line)  # Match lines with a DOT
    # m = re.search(r"[.]", line)  # Match lines with a DOT
    # m = re.search(r"[0-9][0-9][0-9]", line)  # Match 3 consecutive DIGITS
    # m = re.search(r"[aieou][aeiou][aeiou][aeiou]", line)  # Match 4 consecutive VOWELS
    # m = re.search(r"[aieou]{5,}", line)  # Match AT Least 5 consecutive VOWELS
    # m = re.search(r"[aieou][^aeiou]*[aeiou][^aeiou]*[aeiou]", line)  # Vowel+Not Vowels+Vowel...
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines START/END with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines of 6 chars START/END with a CAPITAL
    # m = re.search(r"plumbing|discombobulated|onomatopeia", line)  # Match
    m = re.search(r"^(.)(.).\2\1$", line, flags=re.I|re.M)  # Match lines with 5 CHAR palindromes
    # m = re.match(r"^(.)(.).\2\1$", line)  # AUTO MATCHES START of LINE!
    # m = re.fullmatch(r"^(.)(.).\2\1\n$", line)  # Match ENTIRE line plus hidden chars
    if m:
        print(f"Matched {m.group()} on {m.string.rstrip()} at {m.start()}-{m.end()} "
              f"Groupings={m.groups()}, Group 1 = {m.group(1)} ")
