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
# with ANNOTATIONS (embedded comment)
def say_hello(greeting:str ="ciao", recipient:str ="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="witajcie", recipient="przyjaciele") # Named parameter passing
say_hello(recipient="amigos", greeting="hola") # Named parameters (in different order)
say_hello("cześć", recipient="przyjaciele") # Mixed parameter (positional->named)
say_hello("ciao", 3.14)
say_hello()

print(f"Annotations for say_hello is {say_hello.__annotations__}") # FACT finding