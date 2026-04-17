import pygame
from pygame.locals import QUIT
from Game import GameModel
from View import View
from Controller import Controller

pygame.init()
game = GameModel()
view = View(game)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        