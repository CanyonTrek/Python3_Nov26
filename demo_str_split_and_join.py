#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO split and rejoin strings
# using the str.split() and str.join() methods
""" 
    DocString
"""
# Example from /etc/passwd on Linux for root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to MODIFY the string! BUT str are immutable!
fields = line.split(":") # Returns a LIST (Mutable)
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields) # Returns a modified str
print("Modified line =", line)