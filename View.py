"""
View.py
"""

import pygame

class View:
    def __init__(self, model):
        self.model = model
        pygame.intit()

        self.cell_size = 100
        self.screen = pygame.display.set_mode((400,500))
        self.font = pygame.font.SysFont(None, 40) #which font?
        self.large_font = pygame.font.SysFont(None, 60)

    def draw_grid(self):
        self.screen.fill((255, 255, 255)) #background: white
        for r in range(self.model.size):
            for c in range(self.model.size):
                x = c*self.cell_size
                y = r*self.cell_size + 100
                tile = self.model.board[r][c]
                if tile is not None:
                    self.draw_tile(tile,x,y)
                else:
                    pygame.draw.rect(self.screen, (128, 128, 0), (x,y, self.cell_size, self.cell_size)) #empty color: olive

    def draw_tile(self, tile, x, y):
        pygame.draw.rect(self.screen, (0, 128, 0), (x,y, self.cell_size, self.cell_size)) #tile color: green
        text = self.font.render(str(tile.value), True, (0, 0, 0)) #text color: black
        self.screen.blit(text, (x + 30, y + 30)) # change to the middle later

    def show_score(self):
        pygame.draw.rect(self.screen, (128, 128, 0), (10,10,380,80)) #score background: white
        text = self.font.render(f"Score: {self.model.score}", True, (0, 0, 0))
        self.screen.blit(text, (20, 20)) # middle?

    def animate_move(self, direction):
        pass

    def show_game_over(self):
        if self.model.game_over:
            pygame.draw.rect(self.screen, (255, 0, 0), (50, 200, 300, 100)) #square box: red
            text = self.large_font.render("Game Over!", True, (0, 0, 0)) #text color: black
            self.screen.blit(text, (80, 220)) # middle?

