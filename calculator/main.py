#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script is a Calc App with Basic and Advanced functions
""" 
    Calc app with basic and advanced features
"""
import sys
from app import basic # SAFER and preferred, call using basic.add()
# from app.basic import add, mul, div # Means you can call using add()

def main():
    while True:
        menu = """
            Menu Options
            ------------
            1.Display Basic Calc examples
            2.Display Adv Calc examples
            3.Display Scientific examples
        """
        print(menu)
        option = input("Enter option (1-4,q=quit): ")

        match option:
            case "1":
                print(f"9 + 8 + 7 = {basic.add(9, 8, 7)}")
                print(f"9 * 8 * 7 = {basic.mul(9, 8, 7)}")
                print(f"9 / 8 = {basic.div(9, 8)}")
            case "2":
                pass
            case "q":
                print("Quitting app..")
                break
            case _:
                print("Invalid option")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Only EXECUTE if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0) # Explicit EXIT with return code (0=success)