#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo different ways of formatting
# strings using escape chars, str concatenation, str justification
# methods, the .format() methods and f-strings!
""" 
    DocString
"""
# Dict of planetary information - distance to SUN in Giga metres
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the dict keys and display keys+values nicely
# formatted using ESCAPE chars and str CONCATENATION - MEH!
for planet in planets.keys():
    print("\t\t" + planet + ":\t" + str(planets[planet]) + " Gm")

print("-" * 60)

# formatted using str justification methods and str CONCATENATION - OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 60)
# formatted using str.format() methods - GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm".format(planet, planets[planet]))

print("-" * 60)
# formatted using f-strings (Python 3.5 onwards) - My favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm")


















