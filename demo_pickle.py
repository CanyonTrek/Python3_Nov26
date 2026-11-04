#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import pickle
import pprint
import gzip # tarfile, shutil, bz2

movies = { 'ola': ['pulp fiction', 'shawshank redemption', 'mr harrigans phone'],
           'elaine': ['sound of music', 'the godfather', 'cinema parsdiso'],
           'irfan': ['the prestige', 'interstellar', 'the dark knight'],
           'iain': ['cold harbour', 'romuald and juliette', 'princess bride']
}

# Open file handle for WRITING in BINARY mode
# with open(r"f:\labs\projects\Python3_Nov26\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\Python3_Nov26\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=4) # Pickle protocol (0=ascii, 1-5=binary)
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Default=4
    # pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Default=5

# Open file handle for READING in BINARY mode
# with open(r"f:\labs\projects\Python3_Nov26\movies.p", mode="rb") as fh_in:
with gzip.open(r"f:\labs\projects\Python3_Nov26\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)