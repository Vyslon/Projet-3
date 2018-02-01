#import pygame and pygame constants
#import constants.py & classes.py


program_loop = 1
menu_loop = 1
game_loop = 1

while program_loop:
    #Display menu
    #Refresh screen
    while menu_loop:
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
    #Limit the number of frames per second so that the program will not take too much ressources
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
