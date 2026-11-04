#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open and close a filehandle
# for random read, and write
"""
    DocString
"""
SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of file

# Open file handle for READING in TEXT mode
with open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(130, SOF) # Seek forwards 130 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

# Open file handle for READING in BINARY/Bytes mode
with open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-90, EOF) # Seek back 90 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-70, CUR) # Seek back 70 bytes from current byte position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")
