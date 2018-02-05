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
                        print(character)

                level_structure.append(line_level)
            self.structure = level_structure

        #for i in range (0,3)

    def display(self, window):
        #Display items
        startingpointimage = pygame.image.load("start.png").convert()
        endingpointimage = pygame.image.load("end.png").convert_alpha()
        wallimage = pygame.image.load("wall.png").convert()
        y, x = 0, 0

        for line in self.structure:
            x = 0
            for character in line:
                if character == 's':
                    window.blit(startingpointimage, (x * 30, y * 30))
                if character == 'w':
                    window.blit(wallimage,(x * 30,y * 30))
                if character == 'e':
                    window.blit(endingpointimage, (x * 30,y * 30))
                x += 1
            y += 1


class Character:
    def __init__(self):
        #initiallize attributes
        pass

    def move(self, choice):
        #Moving character in the desired direction (if possible)
        pass

