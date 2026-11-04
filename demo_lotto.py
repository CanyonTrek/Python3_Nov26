#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO generate 6
# random lottery numbers
""" 
    DocString
"""
import random

# lotto = []
#while len(lotto) < 6:
#    num = random.randint(1, 50)
#    if not num in lotto:
#        lotto.append(num)
#    else:
#        print("Duplicate number =", num)

lotto = set() # Create EMPTY set

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)

print("Lottery numbers =", sorted(lotto))
print("Done")