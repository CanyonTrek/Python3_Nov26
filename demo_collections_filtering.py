#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and OPTIONALLY FILTER
# collections using several techniques..
""" 
    DocString
"""
# Source collection - list of names
students = ['will', 'josh', 'iain', 'asia', 'paul', 'julian', 'donald',
            'aleksandra', 'will']

# Copy and optionally filter source list
# 1.Using an Iterator loop + source, optional condition, expression
wee_names = []
for name in students: # 1.Iterator Loop + source collection
    if len(name) < 5: # 2.Optional condition - filtering
        wee_names.append(name.upper()) # 3.expression
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if parameters is less than 5 chars """
    if len(name) < 5:
        return True
    else:
        return False

# 2.Using an Iterator loop + source, user function (filtering), expression
wee_names = []
for name in students: # 1.Iterator Loop + source collection
    if filter_names(name): # 2.User function - filtering
        wee_names.append(name.upper()) # 3.expression
print(f"2.Short names = {wee_names}")

# 3.Using built-in filter() function + source, user function (filtering).
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Using built-in filter() function + source, LAMBDA function (filtering).
wee_names = list(filter(lambda name:len(name) < 5, students))
print(f"4.Short names = {wee_names}")

# 5.Using LIST COMPREHENSION - expression, iterator loop + source, condition (filtering)
wee_names = [ name.upper() for name in students if len(name) < 5 ]
print(f"5.Short names = {wee_names}")

# 5.1.Using LIST COMPREHENSION - expression, iterator loop + source, condition (filtering)
wee_names = [ (name.upper(), len(name)) for name in students if len(name) < 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2.Using DICT COMPREHENSION - expression, iterator loop + source, condition (filtering)
# DICT keys are Unique - duplicates are removed: FREE FILTERING
wee_names = { name.upper(): len(name) for name in students if len(name) < 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3.Using SET COMPREHENSION - expression, iterator loop + source, condition (filtering)
# SET Values are Unique - duplicates are removed: FREE FILTERING
wee_names = { name.upper() for name in students if len(name) < 5 }
print(f"5.3.Short names = {wee_names}")