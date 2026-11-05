#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is a highly realistic online Tank game
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Instanciate/create 3 new Tank objects
    ola_tank = tank.Tank("German", "Tiger")
    emma_tank = tank.Tank("American", "Sherman")
    elaine_tank = tank.Tank("British", "Churchill")

    # And the game begins..
    ola_tank.accel(63)
    emma_tank.accel(22)

    elaine_tank.rotate_left(289)
    elaine_tank.accel(39)
    elaine_tank.shoot()

    # And success..
    ola_tank.take_damage(58)
    emma_tank.take_damage(41)

    # And now for some VISUALS - well some print statements..
    print(f"Health of Ola's tank is {ola_tank._health}") # POOR CODE

    # And status of the two tanks..
    print(f"Health of Ola's and Emma's tanks = {ola_tank + emma_tank}")

    # Ola receives a HEALTH boost
    # ola_tank._health = 100 # POOR CODE
    # print(f"New health of Ola's tank is {ola_tank._health}") # POOR CODE
    ola_tank.set_health(101) # Setter method :-)
    print(f"New health of Ola's tank is {ola_tank.get_health()}") # Getter method :-)
    ola_tank.tank_health = 102
    print(f"New health of Ola's tank is {ola_tank.tank_health}") # Property variable
    return None


# Namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0)