import random

class Tile:
    """Represents a single tile on the 2048 grid.

    Args:
        value (int): The numeric value of the tile (e.g., 2, 4, 8).
        special_type (str): The theme-specific category of the tile.
        merged (bool): Tracks if the tile has already merged during the current turn.
    """
    def __init__(self, value, special_type="normal"):
        self.value = value
        self.special_type = special_type
        self.merged = False
        self.game_over = False

class GameModel:
    """Handle the logic, math, and grid state of the 2048 game

    Attributes:
        size (int): The dimensions of the square grid (default 4x4).
        grid (list): A 2D list representing the game grid, containing Tile objects or None.
        score (int): The player's current cumulative score.
    """
    def __init__(self, size=4):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.score = 0
        self.playing = True
        self.win_value = 2048
        self.reset()

    def reset(self):
        """Resets the grid to an empty state and spawns two initial tiles."""
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        """Finds an empty cell and spawns a new Tile with a value of 2 or 4.
        
        A value of 2 has a 90% probability, while 4 has a 10% probability.
        """
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] is None]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = Tile(2 if random.random() < 0.9 else 4)

    def slide_row(self, row):
        """Performs the 2048 logic on a single row of Tiles.

        This includes shifting tiles to the left, merging adjacent tiles of 
        identical values, and updating the game score.

        Args:
            row (list): A list of Tile objects or None representing one row.

        Returns:
            list: The processed row after sliding and merging.
        """
        # Shift all tiles to the left
        new_row = [tile for tile in row if tile is not None]
        
        # Merge identical neighbors
        for i in range(len(new_row) - 1):
            if (new_row[i] and new_row[i+1] and new_row[i].value == new_row[i+1].value and 
                not new_row[i].merged and not new_row[i+1].merged):
                new_row[i].value *= 2
                self.score += new_row[i].value
                new_row.pop(i+1)
                new_row.append(None)
        
        # Fill the rest with None
        while len(new_row) < self.size:
            new_row.append(None)
        return new_row
    
    def rotate_grid(self, grid):
        """Transposes the grid to swap rows and columns.
        
        Args:
            grid (list): The 2D grid to be transposed.

        Returns:
            list: The transposed 2D grid.
        """
        return [list(row) for row in zip(*grid)]

    def reverse_grid(self, grid):
        """Reverses the order of elements in each row of the grid.
        
        Args:
            grid (list): The 2D grid to be reversed.

        Returns:
            list: The grid with reversed rows.
        """
        return [row[::-1] for row in grid]

    def move(self, direction):
        """Executes a move in the specified direction.

        Uses grid transformations (rotation/reversal) to reuse the 'Left' slide 
        logic for all four directions. Spawns a new tile if the grid changes.

        Args:
            direction (str): The movement direction ('UP', 'DOWN', 'LEFT', or 'RIGHT').

        Returns:
            bool: True if the move resulted in a change to the grid, False otherwise.
        """
        if not self.playing:
            return False
        
        changed = False
        
        # Transform the grid based on direction
        if direction == "UP":
            self.grid = self.rotate_grid(self.grid)
        elif direction == "DOWN":
            self.grid = self.rotate_grid(self.grid)
            self.grid = self.reverse_grid(self.grid)
        elif direction == "RIGHT":
            self.grid = self.reverse_grid(self.grid)
        # "LEFT" needs no transformation

        # Perform the actual sliding/merging (Reuse Left logic)
        for r in range(self.size):
            old_values = [t.value if t else None for t in self.grid[r]]
            self.grid[r] = self.slide_row(self.grid[r])
            new_values = [t.value if t else None for t in self.grid[r]]
            
            if old_values != new_values:
                changed = True

        # Transform the grid back to its original orientation
        if direction == "UP":
            self.grid = self.rotate_grid(self.grid)
        elif direction == "DOWN":
            self.grid = self.reverse_grid(self.grid)
            self.grid = self.rotate_grid(self.grid)
        elif direction == "RIGHT":
            self.grid = self.reverse_grid(self.grid)

        if changed:
            self.add_random_tile()
            self.check_win()
            self.check_game_over()
            
            for row in self.grid:
                for tile in row:
                    if tile:
                        tile.merged = False
                        
        return changed
    
    def check_game_over(self):
        """
        Determines if the game is over by checking if any merges/ moves remain
        Set self.game_over to True if it is impossible
        """
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    return False
        for r in range(self.size):
            for c in range(self.size):
                current_val = self.grid[r][c].value
                # Check if can merge horizontally
                if c < self.size - 1:
                    if self.grid[r][c+1].value == current_val:
                        return False
                # Check if can merge vertically
                if r < self.size - 1:
                    if self.grid[r+1][c].value == current_val:
                        return False
        self.game_over = True
        self.playing = False
        return True
    
    def check_win(self):
        """
        Checks if any tile on the board has reached the win_value (2048).
        If so, stops the game and sets the win state.
        """
        if not self.playing:
            return False

        for row in self.grid:
            for tile in row:
                if tile and tile.value >= self.win_value:
                    self.playing = False
                    self.game_over = True 
                    return True
        return False
                

        

        
class ThemeManager:
    """Manages asset paths and naming conventions for different game tracks."""
    def __init__(self):
        self.current_theme = "ECE"
        self.placeholder = {"name": "Candidate Weekend", "path": "..."}
        self.themes = {
            "ECE": {
                2: {"name": "Entering College", "path": "..."},
                4: {"name": "", "path": "..."},
                8: {"name": "", "path": "..."},
            },
            "MechE": {
                2: {"name": "Entering College", "path": "..."},
                4: {"name": "A Successful Hopper", "path": "..."},
                8: {"name": "", "path": "..."},
            }
        }

    def set_theme(self, theme_name):
        """Updates the active theme."""
        if theme_name in self.themes:
            self.current_theme = theme_name

    def get_tile_data(self, value):
        """Returns the data dictionary for a specific tile value."""
        theme_dict = self.themes.get(self.current_theme,{})
        return theme_dict.get(value, self.placeholder)