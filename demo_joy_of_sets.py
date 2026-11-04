#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and shrink AND
# combine SETS using SET operators (Remember VENN diagrams)
""" 
    DocString
"""
marvel_fans = {'ola', 'will', 'mike', 'julian', 'irfan', 'donald'}
dc_fans = set() # Creates an empty set

# Grow a set...
dc_fans.add('donald')
dc_fans.add('elaine')
dc_fans.add('asia')

# Shrink a set..
# dc_fans.pop() # Random removal (and return) of a VALUE

# comic_fans = dc_fans.copy() # Copy the set
# comic_fans.clear() # Empty the set

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")
print("-" * 60)

# Combine SETS using SET METHODS (Venn Diagrams)
print(f"Fans of either Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# Combine SETS using SET OPERATORS (Venn Diagrams)
print(f"Fans of either Marvel or DC = {marvel_fans | dc_fans}") # UNION
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}") # INTERSECTION
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}") # DIFFERENCE
print(f"Fans of ONLY Marvel OR DC = {marvel_fans ^ dc_fans}") # Symmetric difference