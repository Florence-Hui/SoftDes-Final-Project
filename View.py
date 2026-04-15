"""
2048 Game View
"""

import pygame
from Game import *


class View():
    def __init__(self, model):
        self.model = model
        #self.assets?

    def draw_tiles(self):
        if not self.game_over:
        for row in self.model.board:
            print(row)

    def show_score(self):
        print(f"Score: {self.model.score}")
    
    def draw(self):
        self.draw_score()
        self.draw_tiles()

    def animate_move(self, direction):
        pass

    def show_game_over(self):
        print("Game Over!")
