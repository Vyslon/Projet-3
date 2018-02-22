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
        self.end_pos = []

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

        starting_point_image = pygame.image.load("start.png").convert()
        ending_point_image = pygame.image.load("end.png").convert_alpha()
        wall_image = pygame.image.load("wall.png").convert()
        item1 = pygame.image.load("item1.png").convert_alpha()
        item2 = pygame.image.load("item2.png").convert_alpha()
        item3 = pygame.image.load("item3.png").convert_alpha()
        y, x = 0, 0

        for line in self.structure:
            x = 0
            for character in line:
                if character == 's':
                    window.blit(starting_point_image, (x * 30, y * 30))
                if character == 'w':
                    window.blit(wall_image,(x * 30, y * 30))
                if character == 'e':
                    window.blit(ending_point_image, (x * 30, y * 30))
                    self.end_pos = [y, x]
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
        self.image = pygame.image.load("macgyver.png").convert_alpha()
        self.pos = [0, 0]
        self.nb_item_found = 0
        self.level = level

    def move(self, choice):
        """Moving character in the desired direction (if possible)"""
        if choice == "left":
            if (self.pos[1] - 1) >= 0:
                hypothetical_pos = self.level.structure[self.pos[0]][self.pos[1] - 1]
                if hypothetical_pos == 's':
                    self.pos[1] = self.pos[1] - 1

                if hypothetical_pos == 'e':
                    self.pos[1] = self.pos[1] - 1

                if hypothetical_pos == 'w':
                    pass

                if hypothetical_pos == 'n':
                    self.pos[1] = self.pos[1] - 1
            print("left")
            print("({}, {})".format(self.pos[0], self.pos[1]))

        if choice == "right":
            if(self.pos[1] + 1) <= 14:
                hypothetical_pos = self.level.structure[self.pos[0]][self.pos[1] + 1]
                if hypothetical_pos == 's':
                    self.pos[1] = self.pos[1] + 1
                if hypothetical_pos == 'e':
                    self.pos[1] = self.pos[1] + 1
                if hypothetical_pos == 'w':
                    print("wall")
                if hypothetical_pos == 'n':
                    self.pos[1] = self.pos[1] + 1
            print("right")
            print("({}, {})".format(self.pos[0], self.pos[1]))

        if choice == "down":
            if (self.pos[0] + 1) <= 14:
                hypothetical_pos = self.level.structure[self.pos[0] + 1][self.pos[1]]
                if hypothetical_pos == 's':
                    self.pos[0] = self.pos[0] + 1
                if hypothetical_pos == 'e':
                    self.pos[0] = self.pos[0] + 1
                if hypothetical_pos == 'w':
                    pass
                if hypothetical_pos == 'n':
                    self.pos[0] = self.pos[0] + 1
            print("down")
            print("({}, {})".format(self.pos[0], self.pos[1]))

        if choice == "up":
            if (self.pos[0] - 1) >= 0:
                hypothetical_pos = self.level.structure[self.pos[0] - 1][self.pos[1]]
                if hypothetical_pos == 's':
                    self.pos[0] = self.pos[0] - 1
                if hypothetical_pos == 'e':
                    self.pos[0] = self.pos[0] - 1
                if hypothetical_pos == 'w':
                    pass
                if hypothetical_pos == 'n':
                    self.pos[0] = self.pos[0] - 1
            print("up")
            print("({}, {})".format(self.pos[0], self.pos[1]))

        if (self.pos[0], self.pos[1]) == (self.level.items1[0], self.level.items1[1]):
            self.level.items1_up = 0
            self.nb_item_found = self.nb_item_found + 1
        elif (self.pos[0], self.pos[1]) == (self.level.items2[0], self.level.items2[1]):
            self.level.items2_up = 0
            self.nb_item_found = self.nb_item_found + 1
        elif (self.pos[0], self.pos[1]) == (self.level.items3[0], self.level.items3[1]):
            self.level.items3_up = 0
            self.nb_item_found = self.nb_item_found + 1
