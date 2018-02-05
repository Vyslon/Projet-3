import pygame
from pygame.locals import *

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
        #Display items
        startingpointimage = pygame.image.load("start.png")
        endingpointimage = pygame.image.load("end.png")
        wallimage = pygame.image.load("wall.png")
        y, x = 0, 0
        for line in self.structure:
            for character in line:
                if character == 's':
                    window.blit(startingpointimage, (x * 30, y * 30))
                if character == 'w':
                    window.blit(endingpointimage,(x * 30,y * 30))
                if character == 'e':
                    window.blit(wallimage, (x * 30,y * 30))
                x += 1
            y += 1

        pass

class Character:
    def __init__(self):
        #initiallize attributes
        pass

    def move(self, choice):
        #Moving character in the desired direction (if possible)
        pass

