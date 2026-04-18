"""
2048 Game View
"""
import pygame

class View:
    """
    A class that displays the current state of the game to the user, including the grid,
    score, and game over conditions.

    Attributes:
        model: An instance of the GameModel class
        cell_size: An integer representing the size of each cell in the grid.
        screen: A pygame surface object from the Main file.
        font: A pygame Font used for normal-sized text on the screen.
        large_font: A pygame Font for larger text on the screen.
    """
    def __init__(self, model):
        """
        Initializes the View with a reference to the game model.

        Args:
            model: An instance of the GameModel class containing information about the current
            2048 game being played.
        """
        self.model = model
        pygame.init()

        self.cell_size = 100
        self.screen = None
        self.font = pygame.font.SysFont(None, 40) #which font?
        self.large_font = pygame.font.SysFont(None, 60)

    def draw_grid(self):
        """
        Draws the game grid based on the current state of the model. 
        Each tile occupied is represented as a green rectangle with its value text displayed on top. 
        Empty cells and backgroundare shown as olive color.
        """
        self.screen.fill((128, 128, 128)) #background: olive
        for r in range(self.model.size):
            for c in range(self.model.size):
                x = c*self.cell_size
                y = r*self.cell_size + 100
                tile = self.model.grid[r][c]
                if tile is not None:
                    self.draw_tile(tile,x,y)
                else:
                    pygame.draw.rect(self.screen, (128, 128, 0), (x,y, self.cell_size, self.cell_size)) #empty color: olive

    def draw_tile(self, tile, x, y):
        """
        Draws a tile that is occupied at the specified coordinates.
        """
        pygame.draw.rect(self.screen, (0, 128, 0), (x,y, self.cell_size, self.cell_size)) #tile color: green
        text = self.font.render(str(tile.value), True, (0, 0, 0)) #text color: black
        self.screen.blit(text, (x + 30, y + 30)) # change to the middle later

    def show_score(self):
        """
        Displays the current score on the top of the screen.
        """
        pygame.draw.rect(self.screen, (128, 128, 0), (10,10,380,80)) #score background: white
        text = self.large_font.render(f"Score: {self.model.score}", True, (0, 0, 0))
        self.screen.blit(text, (20, 20)) # middle?

    def animate_move(self, direction):
        """
        Animates the movement of tiles in the specified direction. 

        Args:
            direction: A string indicating the direction of movement ("UP", "DOWN", "LEFT", "RIGHT").
        """
        old_positions = {}
        for r in range(self.model.size):
            for c in range(self.model.size):
                tile = self.model.grid[r][c]
                if tile:
                    old_positions[id(tile)] = (c, r)

        self.model.move(direction)

        new_positions = {}
        for r in range(self.model.size):
            for c in range(self.model.size):
                tile = self.model.grid[r][c]
                if tile:
                    new_positions[id(tile)] = (c, r)

        frames = 10
        for frame in range(frames):
            progress = frame / frames
            self.screen.fill((255, 255, 255))
            self.show_score()
            for tile_id in new_positions:
                if tile_id in old_positions:
                    start_c, start_r = old_positions[tile_id]
                    end_c, end_r = new_positions[tile_id]
                    curr_c = start_c + (end_c - start_c) * progress
                    curr_r = start_r + (end_r - start_r) * progress
                else:
                    curr_c, curr_r = new_positions[tile_id]
                x = curr_c * self.cell_size
                y = curr_r * self.cell_size + 100
                for row in self.model.grid:
                    for t in row:
                        if t and id(t) == tile_id:
                            self.draw_tile(t, x, y)
            pygame.display.flip()
            pygame.time.delay(20)


    def show_game_status(self):
        """
        Displays game over or win messages when the game has ended.
        For the game over message, the game resets after displaying the message.
        """
        if self.model.check_game_over():
            pygame.draw.rect(self.screen, (255, 0, 0), (50, 200, 300, 100)) #square box: red
            text = self.large_font.render("Game Over!", True, (0, 0, 0)) #text color: black
            self.screen.blit(text, (80, 220)) # middle?
            self.model.reset()
        if self.model.check_win():
            pygame.draw.rect(self.screen, (0, 255, 0), (50, 200, 300, 100)) #square box: green
            text = self.large_font.render("Congratulations!You Graduated!", True, (0, 0, 0))
            self.screen.blit(text, (80, 220))