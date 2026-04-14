from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_w, K_s, K_a, K_d,
    K_ESCAPE, K_SPACE
)


class Controller():
    
    def __init__(self, model):
        self.model = model
        self.keys_pressed = {}
    
    def check_inputs(self, keys_pressed):
        if not self.game.check_transition():
            self.keys_pressed = keys_pressed
            
            is_moving = self.check_movement()
            
            if not is_moving:
                self.check_other_inputs()
    
    def check_movement(self):
        key = ""
        
        if self.keys_pressed[K_UP] or self.keys_pressed[K_w]:
            key = "UP"
        elif self.keys_pressed[K_DOWN] or self.keys_pressed[K_s]:
            key = "DOWN"
        elif self.keys_pressed[K_LEFT] or self.keys_pressed[K_a]:
            key = "LEFT"
        elif self.keys_pressed[K_RIGHT] or self.keys_pressed[K_d]:
            key = "RIGHT"
        
        self.game.move_tiles(key)
        return key != ""
        # CHANGE move_tiles TO WHATEVER THE CORRESPONDING METHOD IN THE GAME CLASS IS
    
    def check_other_inputs(self):
        if self.keys_pressed[K_SPACE]:
            pass    # fill in menu selection functionality later
        elif self.keys_pressed[K_ESCAPE]:
            self.game.quit()