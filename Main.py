import pygame
from pygame.locals import QUIT
from Game import GameModel
from View import View
from Controller import Controller

pygame.init()
game = GameModel()
view = View(game)
controller = Controller(game)

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("2048")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    view.screen = screen
    view.draw_grid()
    view.show_score()

    pygame.display.flip()

pygame.quit()
