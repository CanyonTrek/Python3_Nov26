#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module describes a class of Tank
""" 
    Tank class
"""
from app import vehicle

class Tank(vehicle.Vehicle):
    # Has TWO components: Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # No explicit return AS IMPLICITLY CALLED



    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # SPECIAL METHODS...
    def __add__(self, other):
        return self._health + other._health

    # GETTER and SETTER methods
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Defines  ONE VARIABLE name interface to the GETTER and SETTER
    tank_health = property(get_health, set_health)