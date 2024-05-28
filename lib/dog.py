#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# File: lib/dog.py

class Dog:
    def __init__(self, name="unknown", breed="Mutt"):
        self._name = None
        self.name = name
        self.breed = breed
    def name(self):
        # print (f"{self._name}")
        return self._name
    
    def name(self, name):
        if (type(name) in (str)) and 1 <= len(name) <= 25:
            print(f"{name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            return ""
    def sit(self):
        print(f"{self.name} is sitting.")
    
    def bark(self):
        print(f"{self.name} says woof!")
