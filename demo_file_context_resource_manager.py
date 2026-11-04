#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open and close filehandler automatically
# and in more memory safer way using with statement (Context Resource Mgr)
"""
    DocString
"""
movies = { 'ola': ['pulp fiction', 'shawshank redemption', 'mr harrigans phone'],
           'elaine': ['sound of music', 'the godfather', 'cinema parsdiso'],
           'irfan': ['the prestige', 'interstellar', 'the dark knight'],
           'iain': ['cold harbour', 'romuald and juliette', 'princess bride']
}

with open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n")
        fh_out.write(f"{name} {movies[name]}\n")
        del fh_out
    # End of block - teardown/close file handle

print("-" * 60)

with open(r"f:\labs\projects\Python3_Nov26\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
