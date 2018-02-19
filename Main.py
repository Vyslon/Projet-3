import pygame
from pygame.locals import *
from Constants import *
from Classes import *

pygame.init()

window = pygame.display.set_mode((window_size, window_size))

"""Display Icon"""
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

"""Display Title"""
pygame.display.set_caption("MacGyver Labyrinth")

while program_loop:
    while menu_loop:
        pygame.time.Clock().tick(30)

        background = pygame.image.load("menu_background.png").convert()
        window.blit(background, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                menu_loop = 0
                program_loop = 0
            if event.type == KEYDOWN:
                if event.key == K_RETURN | K_KP_ENTER:
                    menu_loop = 0
                    game_loop = 1

    if game_loop:
        background = pygame.image.load("background.jpg").convert()
        window.blit(background, (0, 0))
        pygame.display.flip()

        lvl = Level("level_config.txt")
        lvl.generator()
        lvl.display(window)
        mg = Character(lvl)
        window.blit(mg.image, (mg.pos[0] * 30, mg.pos[1] * 30))
        pygame.display.flip()

    while game_loop:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_loop = 0
                program_loop = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_loop = 0
                    menu_loop = 1

                if event.key == K_LEFT:
                    mg.move("left")
                if event.key == K_RIGHT:
                    mg.move("right")
                if event.key == K_DOWN:
                    mg.move("down")
                if event.key == K_UP:
                    mg.move("up")

        if lvl.structure[mg.pos[0]][mg.pos[1]] == 'e':
            if mg.nb_item_found == 3:
                game_loop = 0
                menu_loop = 1
            else:
                game_loop = 0
                menu_loop = 1

        window.blit(background, (0, 0))
        lvl.display(window)
        window.blit(mg.image, (mg.pos[1] * 30, mg.pos[0] * 30))
        pygame.display.flip()

    if program_loop:
        if (lvl.structure[mg.pos[0]][mg.pos[1]] == 'e') and (mg.nb_item_found == 3):
            winning_loop = 1
            while winning_loop:
                pygame.time.Clock().tick(30)

                background_win = pygame.image.load("winning_screen.png").convert()
                window.blit(background_win, (0, 0))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        winning_loop = 0
                        menu_loop = 0
                        program_loop = 0
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN | K_KP_ENTER:
                            winning_loop = 0

        else:
            losing_loop = 1
            while losing_loop:
                pygame.time.Clock().tick(30)

                background_lose = pygame.image.load("losing_screen.png").convert()
                window.blit(background_lose, (0, 0))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        losing_loop = 0
                        menu_loop = 0
                        program_loop = 0
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN | K_KP_ENTER:
                            losing_loop = 0

