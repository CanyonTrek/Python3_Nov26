#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close, a FILEHANDLE for
# reading, writing and appending in TEXT mode.
""" 
    DocString
"""
movies = { 'ola': ['pulp fiction', 'shawshank redemption', 'mr harrigans phone'],
           'elaine': ['sound of music', 'the godfather', 'cinema parsdiso'],
           'irfan': ['the prestige', 'interstellar', 'the dark knight'],
           'iain': ['cold harbour', 'romuald and juliette', 'princess bride']
}

# Open filehandle for WRITING in TEXT mode
fh_out = open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="wt")

# ITERATE through the movies keys and write movie info to file
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Manually flush buffers..
fh_out.close() # Flush buffers and close file handle

print("-" * 60)

# Open filehandle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object! Careful of HUGE files
# text = fh_in.read(30) # Read NEXT 30 CHARS into str object!
# text = fh_in.readline() # Read NEXT LINE into str object!
# lines = fh_in.readlines() # Read ENTIRE file into a LIST object!. Careful of HUGE files!
# print(f"First line = {lines[0]}")
# print(f"Last line = {lines[-1]}")

# ITERATE through a file handle ONE line at a time USING
# an ITERATOR for loop..
# for line in open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="rt"):
# ITERATOR loop plus ITERABLE OBJECT (next/iter methods) NEWLINE!
for line in fh_in:
    print(line, end="")

fh_in.close()
