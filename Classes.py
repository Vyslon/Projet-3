import random
import pygame
from pygame.locals import *

class Level:
    def __init__(self, file):
        """
        Initialize attributes of the class
        """
        self.lvlConfigFile = file
        self.structure = 0
        self.items1 = ()
        self.items2 = ()
        self.items3 = ()


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

        for i in range(0, 3):
            x, y = 0, 0
            while ((self.structure[y][x] != 'n') or ((y, x) == self.items1
                    or (y, x) == self.items2
                    or (y, x) == self.items3)):
                y = random.randrange(0, len(self.structure)-1, 1)
                x = random.randrange(0, len(self.structure)-1, 1)
            if i == 0:
                self.items1 = (y, x)
            elif i == 1:
                self.items2 = (y, x)
            elif i == 2:
                self.items3 = (y, x)


    def display(self, window):
        #Display items
        startingpointimage = pygame.image.load("start.png").convert()
        endingpointimage = pygame.image.load("end.png").convert_alpha()
        wallimage = pygame.image.load("wall.png").convert()
        item1 = pygame.image.load("item1.png").convert()
        item2 = pygame.image.load("item2.png").convert()
        item3 = pygame.image.load("item3.png").convert()
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
                if (y, x) == self.items1:
                    window.blit(item1, (x * 30, y * 30))
                elif (y, x) == self.items2:
                    window.blit(item2, (x * 30, y * 30))
                elif (y, x) == self.items3:
                    window.blit(item3, (x * 30, y * 30))
                x += 1
            y += 1


class Character:
    def __init__(self):
        self.mgimage = pygame.image.load("macgyver.png").convert_alpha()
        self.mgpos = [0, 0]
        self.mgnbitemfound = 0

    def move(self, choice):
        #Moving character in the desired direction (if possible)
        pass

