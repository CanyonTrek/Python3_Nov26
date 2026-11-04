#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO CREATE, and grow, and shrink
# dictionaries and how to access keys and values
""" 
    DocString
"""
import pprint
# Create a multi-dimensional dictionary of lists
movies = { 'ola': ['pulp fiction', 'shawshank redemption', 'mr harrigans phone'],
           'elaine': ['sound of music', 'the godfather', 'cinema parsdiso'],
           'irfan': ['the prestige', 'interstellar', 'the dark knight'],
}

# Add to a dict
movies['iain'] = ['cold harbour', 'romuald and juliette', 'princess bride']

# Shrink a dict
# movies.pop('irfan') # Remove a key+value
# movies.popitem() # Remove LAST INSERTED key+value
# films = movies.copy() # Copies dictionary
# films.clear() # Empties the dictionary

# Access a dict
pprint.pprint(movies)
print("-" * 60)
print(f"Ola's favourite movies are {movies['ola']}")
print(f"Ola's favourite movies are {movies.get('ola')}")
print(f"Elaine's ultimate movies is {movies['elaine'][0]}")
print("-" * 60)

# ITERATE through keys ONE key at a time using an
# ITERATOR for loop plus the .keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# ITERATE through VALUES ONE VALUE at a time using an
# ITERATOR for loop plus the .values() method
for films in movies.values():
    print(f"Recommended films: {films}")

# ITERATE through KEY+VALUE PAIR ONE VALUE at a time using an
# ITERATOR for loop plus the .items() method
for (name, films) in movies.items():
    print(f"{name} LOVES the films {films}")