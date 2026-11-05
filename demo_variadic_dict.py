#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define, name, and call (resuse) a user
# function with optional parameters passing and return value.
"""
    DocString
"""
# Example of a USER function
# with optional parameter passing with default values
# CAPTURE NAMED PARAMETERS into dictionary called my_dict
def say_hello(**my_dict):
    message = f"{my_dict['greeting']} {my_dict['recipient']}"
    print(message)
    print(my_dict)
    return None

say_hello(greeting="witajcie", recipient="przyjaciele") # Named parameter passing
say_hello(recipient="amigos", greeting="hola") # Named parameters (in different order)
