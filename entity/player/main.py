import random

import pygame.mouse

from bullet.standard.main import Bullet
from controller.event_handler import KeyHandler
from entity.main import Entity
from math import sqrt, atan2
from config import BASE_PLAYER_SPEED, BASE_PLAYER_COLOR
from helpers.degree import Degree
from helpers.point import Point
from shape.hexagon import Hexagon


class Player(Entity):

    def __init__(self):
        super().__init__(Hexagon(0, 0, 40 * sqrt(3), 40 * 2), hp=10, color=BASE_PLAYER_COLOR)
        self.velocity = (0, 0)
        self.max_speed = BASE_PLAYER_SPEED
        self.type = "player"
        self.hurt_time = 0.3
        self.hurt_time_left = 0

        self.fire_rate = 1000
        self.time_to_next_bullet = 1 / self.fire_rate
        self.spread = 0.3

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
            if vx < self.max_speed:
                vx += (self.max_speed * horizontal - vx) / 4
        else:
            vx *= 0.4
        if vertical:
            if vy < self.max_speed:
                vy += (self.max_speed * vertical - vy) / 4
        else:
            vy *= 0.4
        self.translate(vx * time, vy * time)

        self.velocity = vx, vy

    def tick(self, game_state):
        self.move(game_state.key_handler, game_state.time_delta)
        self.original_polygon.scale(1 + 0 * game_state.time_delta)
        self.original_polygon.rotate(-3 * game_state.time_delta)

        if self.hurt_time_left:
            self.hurt_time_left = max(self.hurt_time_left - game_state.time_delta, 0)
            self.invincible = False

        if self.time_to_next_bullet < 0:
            if game_state.key_handler.clicked("left"):
                self.time_to_next_bullet += 1 / self.fire_rate
                self.fire(game_state)
        else:
            self.time_to_next_bullet -= game_state.time_delta

    def fire(self, game_state):
        position = self.display_polygon.center
        mouse_pos = Point(*pygame.mouse.get_pos())
        diff = mouse_pos - position
        angle = Degree(atan2(*diff.pos)) + (random.random() - 0.5) * self.spread
        game_state.add_friendly(Bullet(*self.display_polygon.center.pos, initial_rotation=angle))

    def display(self, screen):
        self.display_color = self.original_color.gamma(0.5 * (self.hurt_time_left / self.hurt_time))
        super().display(screen)
        smaller_polygon = self.original_polygon.__copy__()
        smaller_polygon.scale(0.71)
        display = smaller_polygon.move(0,0)
        display.display(screen, (200, 90, 128))
        smaller_polygon = self.original_polygon.__copy__()
        smaller_polygon.scale(0.35)
        display = smaller_polygon.move(0,0)
        display.display(screen, (0, 90, 128))

    def damage(self, incoming_damage):
        super().damage(incoming_damage)
        self.hurt_time_left = self.hurt_time
        self.invincible = True
