import random
import pygame
from pygame.locals import *

class Level:
    structure = 0
    def __init__(self, file):
        """
        Initialize attributes of the class
        """
        self.lvlConfigFile = file
        self.items1 = ()
        self.items1_up = 1
        self.items2 = ()
        self.items2_up = 1
        self.items3 = ()
        self.items3_up = 1
        self.endpos = []


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
                    self.endpos = [y, x]
                if ((y, x) == self.items1) and self.items1_up:
                    window.blit(item1, (x * 30, y * 30))
                elif ((y, x) == self.items2) and self.items2_up:
                    window.blit(item2, (x * 30, y * 30))
                elif ((y, x) == self.items3) and self.items3_up:
                    window.blit(item3, (x * 30, y * 30))
                x += 1
            y += 1


class Character:
    def __init__(self, level):
        self.mgimage = pygame.image.load("macgyver.png").convert_alpha()
        self.mgpos = [0, 0]
        self.mgnbitemfound = 0
        self.level = level

    def move(self, choice):
        """Moving character in the desired direction (if possible)"""
        if choice == "left":
            if ((self.mgpos[1] - 1) >= 0):
                hypot_pos = self.level.structure[self.mgpos[0]][self.mgpos[1] - 1]
                if (hypot_pos) == 's':
                    self.mgpos[1] = self.mgpos[1] - 1

                if (hypot_pos) == 'e':
                    self.mgpos[1] = self.mgpos[1] - 1

                if (hypot_pos) == 'w':
                    pass

                if (hypot_pos) == 'n':
                    self.mgpos[1] = self.mgpos[1] - 1
            print("left")
            print("({}, {})".format(self.mgpos[0], self.mgpos[1]))

        if choice == "right":
            if((self.mgpos[1] + 1) <= 14):
                hypot_pos = self.level.structure[self.mgpos[0]][self.mgpos[1] + 1]
                if (hypot_pos) == 's':
                    self.mgpos[1] = self.mgpos[1] + 1
                if (hypot_pos) == 'e':
                    self.mgpos[1] = self.mgpos[1] + 1
                if (hypot_pos) == 'w':
                    print("wall")
                if (hypot_pos) == 'n':
                    self.mgpos[1] = self.mgpos[1] + 1
            print("right")
            print("({}, {})".format(self.mgpos[0], self.mgpos[1]))

        if choice == "down":
            if ((self.mgpos[0] + 1) <= 14):
                hypot_pos = self.level.structure[self.mgpos[0] + 1][self.mgpos[1]]
                if (hypot_pos) == 's':
                    self.mgpos[0] = self.mgpos[0] + 1
                if (hypot_pos) == 'e':
                    self.mgpos[0] = self.mgpos[0] + 1
                if (hypot_pos) == 'w':
                    pass
                if (hypot_pos) == 'n':
                    self.mgpos[0] = self.mgpos[0] + 1
            print("down")
            print("({}, {})".format(self.mgpos[0], self.mgpos[1]))

        if choice == "up":
            if ((self.mgpos[0] - 1) >= 0):
                hypot_pos = self.level.structure[self.mgpos[0] - 1][self.mgpos[1]]
                if (hypot_pos) == 's':
                    self.mgpos[0] = self.mgpos[0] - 1
                if (hypot_pos) == 'e':
                    self.mgpos[0] = self.mgpos[0] - 1
                if (hypot_pos) == 'w':
                    pass
                if (hypot_pos) == 'n':
                    self.mgpos[0] = self.mgpos[0] - 1
            print("up")
            print("({}, {})".format(self.mgpos[0], self.mgpos[1]))

        if (self.mgpos[0], self.mgpos[1]) == (self.level.items1[0], self.level.items1[1]):
            self.level.items1_up = 0
            self.mgnbitemfound = self.mgnbitemfound + 1
        elif (self.mgpos[0], self.mgpos[1]) == (self.level.items2[0], self.level.items2[1]):
            self.level.items2_up = 0
            self.mgnbitemfound = self.mgnbitemfound + 1
        elif (self.mgpos[0], self.mgpos[1]) == (self.level.items3[0], self.level.items3[1]):
            self.level.items3_up = 0
            self.mgnbitemfound = self.mgnbitemfound + 1


