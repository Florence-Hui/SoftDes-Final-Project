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
    pressed_keys = pygame.key.get_pressed()
    controller.check_inputs(pressed_keys)
    view.screen = screen
    view.draw_grid()
    view.show_score()
    view.show_game_status()

    pygame.display.flip()

pygame.quit()
