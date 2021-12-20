from controller.event_handler import KeyHandler
from player.display import display
from math import sqrt
from config import BASE_PLAYER_SPEED


class Player:

    def __init__(self):
        self.coords = (0, 0)
        self.size = (50, 50)

    def display(self, screen):
        display(screen, self.coords, self.size)

    def tick(self, key_handler: KeyHandler, time: float):
        left = key_handler.pressed("left")
        right = key_handler.pressed("right")

        horizontal = - int(left) + int(right)

        up = key_handler.pressed("up")
        down = key_handler.pressed("down")

        vertical = - int(up) + int(down)

        if horizontal and vertical:
            horizontal /= sqrt(2)
            vertical /= sqrt(2)
        self.coords = self.coords[0] + horizontal * BASE_PLAYER_SPEED * time, self.coords[
            1] + vertical * BASE_PLAYER_SPEED * time
