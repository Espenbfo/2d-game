from __future__ import annotations

from pygame.surface import Surface

import controller.game_state
from config import WINDOW_SIZE
from helpers.color import Color
from helpers.point import Point
from helpers.polygon import Polygon

ID = 0


class Entity:
    def __init__(self, polygon, hp=10, speed=10, color=(200, 170, 164), initial_position=Point(0,0)):
        self.original_polygon: Polygon = polygon
        self.display_polygon: Polygon = polygon
        self.original_polygon.displacement = initial_position
        self.hp = hp
        self.max_speed = speed
        self.original_color = Color(*color)
        self.display_color = Color(*color)
        self.type = "entity"
        self.invincible = False
        self.to_be_deleted = False
        global ID
        self.id = ID
        ID += 1

    def damage(self, incoming_damage: float | int):
        self.hp -= incoming_damage
        if self.hp < 0:
            self.to_be_deleted = True

    def display(self, screen: Surface):
        self.display_polygon.display(screen, self.display_color.rgb())

    def tick(self, game_state: controller.game_state.GameState):
        return False

    def translate(self, x, y, limit=WINDOW_SIZE):
        self.display_polygon = self.original_polygon.move(x, y, limit)

    def collide(self, other: Entity):
        pass

    def is_colliding(self, other: Entity):
        return self.display_polygon.collide(other.display_polygon)