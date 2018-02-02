#import pygame

class Level:
    def __init__(self, file):
        """
        Initialize attributes of the class
        """
        self.lvlConfigFile = file
        self.structure = 0


    def generator(self):
        """Generate structure and place items has random locations"""
        with open(self.lvlConfigFile, "r") as file:
            level_structure = []
            for line in file:
                line_level = []
                for character in line:
                    if character != '\n':
                        line_level.append(character)

                level_structure.append(line_level)
            self.structure = level_structure

    def display(self, window):
        #Display labyrinth
        #Display items
        pass

class Character:
    def __init__(self):
        #initiallize attributes
        pass

    def move(self, choice):
        #Moving character in the desired direction (if possible)
        pass

