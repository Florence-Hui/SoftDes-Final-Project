from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_w, K_s, K_a, K_d,
    K_ESCAPE, K_SPACE,
    KEYDOWN, QUIT
)


class Controller():
    def __init__(self):
        self.keys_pressed = {}