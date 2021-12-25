from __future__ import annotations

from pygame.surface import Surface

import controller.game_state
from helpers.color import Color
from shape.polygon import Polygon


class Entity:
    def __init__(self, polygon, hp=10, speed=10, color=(200, 170, 164)):
        self.original_polygon: Polygon = polygon
        self.display_polygon: Polygon = polygon
        self.hp = hp
        self.max_speed = speed
        self.original_color = Color(*color)
        self.display_color = Color(*color)
        self.type = "entity"

    def damage(self, incoming_damage: float | int):
        self.hp -= incoming_damage
        return self.hp <= 0

    def display(self, screen: Surface):
        self.display_polygon.display(screen, self.display_color.rgb())

    def tick(self, game_state: controller.game_state.GameState):
        return False

    def collide(self, other: Entity):
        pass