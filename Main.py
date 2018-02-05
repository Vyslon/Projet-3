import pygame
from pygame.locals import *
from Constants import *
from Classes import *

program_loop = 1
menu_loop = 0
game_loop = 1

window_size = 450
window = pygame.display.set_mode((window_size, window_size))

while program_loop:
    #Display menu
    #Refresh screen
    while menu_loop:
        pass
    #Limit the number of frames per second so that the program will not take too much ressources
    #For every event
    #   If quit icon
    #       game_loop = 0
    #       menu_loop = 0
    #       program_loop = 0
    #   If enter key
    #       game_loop = 1
    #       menu_loop = 0
    #If game_loop
    #   load and display background
    #   create level structure
    #   display level
    #   Instantiate the character
    while game_loop:
        pygame.time.Clock().tick(30)

        background = pygame.image.load("background.png").convert()
        window.blit(background, (0, 0))
        game_loop = 0
        program_loop = 0
    #For every event
    #   If quit icon
    #       game_loop = 0
    #       menu_loop = 0
    #       program_loop = 0
    #   If escape
    #       game_loop = 0
    #       menu_loop = 1
    #   If arrow keys
    #       character.move()
    #Display character at new position
    #Refresh screen
    #If character.pos == 'e' (end)
    #   game_loop = 0
    #   menu_loop = 1
    #If character.items < nb_items_needed
    #   display loosing screen
    #   refresh screen
    #Else
    #   display winning screen
    #   refresh screen
