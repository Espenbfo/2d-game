from __future__ import annotations

from typing import List

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

import controller.game_state


class SquareEntity:
    def __init__(self, rect=Rect(0, 0, 10, 10), hp=10, speed=10, color=(200, 170, 164)):
        self.rect = rect
        self.hp = hp
        self.max_speed = speed
        self.color = color

    def damaged(self, incoming_damage: float | int):
        self.hp -= incoming_damage
        return self.hp <= 0

    def display(self, screen: Surface):
        pygame.draw.rect(screen, self.color, self.rect)

    def tick(self, game_state: controller.game_state.GameState):
        return False
