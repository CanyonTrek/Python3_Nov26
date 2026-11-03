#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO REPEAT a BLOCK of
# commands a specific repetitions using a COUNTER LOOP
""" 
    DocString
"""

count = 0 # 1.Initialise counter START
while count < 10: # 2.Test condition STOP
    print(count)
    count += 1 # 3.Increment counter STEP

# Alternatively we could use a FOR loop plus the
# built-in range(start=0, stop, step=1) function
for num in range(0, 10, 1):
    print(num)

for num in range(0, 10):
    print(num)

for num in range(10):
    print(num)