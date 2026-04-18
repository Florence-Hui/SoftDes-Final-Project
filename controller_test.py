"""
Contains methods that test whether the controller class works
"""

import pygame
from pygame.locals import QUIT
from Game import GameModel
from Controller import Controller

pygame.init()
game = GameModel()
controller = Controller(game)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("omg is that pygame")

running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    controller.check_inputs(pressed_keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))
    pygame.display.flip()