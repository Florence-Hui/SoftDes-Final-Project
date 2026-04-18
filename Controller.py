"""
This contains the class for the controller of a custom 2048 game.
"""

from time import sleep
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_w, K_s, K_a, K_d,
    K_ESCAPE, K_SPACE
)


class Controller():
    """
    A class that reads user input and calls corresponding methods in the
    game class for a custom 2048 game.
    
    Attributes:
        model: An instance of the GameModel class containing information
        about the current 2048 game being played.
        
        keys_pressed: A dictionary in which the keys represent keys on a
        keyboard, which are mapped to boolean values that are True if the
        key is being pressed and False otherwise.
        
        _last_command: A string containing the last command made by the user,
        in all uppercase (i.e., "LEFT" or "UP"), or an empty string if the
        user most recently pressed nothing.
    """
    
    def __init__(self, model):
        '''
        Initializes the Controller class.
        
        Args:
            model: An instance of the GameModel class containing information
            about the current 2048 game being played.
        '''
        self.model = model
        self.keys_pressed = {}
        self._last_command = ""
    
    def check_inputs(self, keys_pressed):
        """
        Checks all inputs for the game, and calls corresponding methods
        when a key is pressed. Only checks for individual key presses,
        not holds.
        """
        #if not self.game.check_animation(): #CHANGE BASED ON GAME METHOD
        self.keys_pressed = keys_pressed
        
        if self._last_command != "" and self._check_movement() != "":
            return
        
        key = self._check_movement()
        self._last_command = key
        
        if key != "":
            self.model.move(key)
            print(key) #FOR DEBUGGING, REMOVE LATER

        else:
            self._check_other_inputs()
    
    def _check_movement(self):
        """
        Checks for presses of the movement keys, both WASD and the arrow keys.
        Calls the method for moving tiles if a key is being pressed.
        
        Returns:
            A boolean that is true if an movement key is being pressed,
            or false otherwise.
        """
        key = ""
        
        if self.keys_pressed[K_UP] or self.keys_pressed[K_w]:
            key = "UP"
        elif self.keys_pressed[K_DOWN] or self.keys_pressed[K_s]:
            key = "DOWN"
        elif self.keys_pressed[K_LEFT] or self.keys_pressed[K_a]:
            key = "LEFT"
        elif self.keys_pressed[K_RIGHT] or self.keys_pressed[K_d]:
            key = "RIGHT"
        
        return key
    
    def _check_other_inputs(self):
        """
        Checks the space bar and escape key for inputs from the user
        """
        if self.keys_pressed[K_SPACE]:
            pass    # fill in menu selection functionality later
        elif self.keys_pressed[K_ESCAPE]:
            self.model.quit()