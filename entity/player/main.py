from pygame.rect import Rect

from controller.event_handler import KeyHandler
from controller.game_state import GameState
from entity.player.display import display
from math import sqrt
from config import BASE_PLAYER_SPEED, WINDOW_SIZE, BASE_PLAYER_COLOR, SCREEN_RECT
from entity.square_entity.main import SquareEntity


class Player(SquareEntity):

    def __init__(self):
        super().__init__(rect=Rect(0,0,25,25), hp=10, color=BASE_PLAYER_COLOR)
        self.velocity = (0, 0)
        self.max_speed = BASE_PLAYER_SPEED

    def move(self, key_handler: KeyHandler, time: float):
        left = key_handler.pressed("left")
        right = key_handler.pressed("right")

        horizontal = - int(left) + int(right)

        up = key_handler.pressed("up")
        down = key_handler.pressed("down")

        vertical = - int(up) + int(down)

        if horizontal and vertical:
            horizontal /= sqrt(2)
            vertical /= sqrt(2)

        vx, vy = self.velocity
        if horizontal:
            if (vx < self.max_speed):
                vx += (self.max_speed*horizontal-vx)/4
        else:
            vx *= 0.4
        if vertical:
            if (vy < self.max_speed):
                vy += (self.max_speed*vertical-vy)/4
        else:
            vy *= 0.4
        self.rect = self.rect.move(vx * time, vy * time)
        self.rect = self.rect.clamp(SCREEN_RECT)

        self.velocity = vx, vy

    def tick(self, game_state: GameState):
        self.move(game_state.key_handler, game_state.time_delta)
