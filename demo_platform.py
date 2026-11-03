#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import os
import sys

if sys.platform == "win32":
    my_home = os.environ["HOMEPATH"]
elif sys.platform == "linux":
    my_home = os.environ["HOME"]
else:
    my_home = "/users/donald"

print("My home directory is:", my_home)