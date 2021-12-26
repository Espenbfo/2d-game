from math import atan2, sin, cos, pi, sqrt

from entity.main import Entity
from entity.player.main import Player
from helpers.degree import Degree
from shape.arrow import Arrow
from helpers.point import Point
from random import random

class Charger(Entity):
    def __init__(self, x=0, y=0):
        super().__init__(polygon=Arrow(0, 0, 10, 40), color=(240, 80, 90), initial_position=Point(x, y))
        self.type = "charger"
        self.speed = 200
        self.strength = 10
        self.rotation_speed = 10
        self.hp= 100

    def point(self, player: Player, time_delta):
        player.position = player.display_polygon.center
        position = self.display_polygon.center
        diff = player.position - position + Point(random()-0.5, random()-0.5)*100
        angle = Degree(atan2(*diff.pos))
        self.original_polygon.rotate((angle - self.original_polygon.rotation.degree) * time_delta * self.rotation_speed)
        self.translate(*(Point(cos(self.original_polygon.rotation.degree - pi / 2),
                                                                  -sin(
                                                                      self.original_polygon.rotation.degree - pi / 2)) *
                                                            time_delta * self.speed).pos)

    def tick(self, game_state):
        self.point(game_state.player, game_state.time_delta)

    def collide(self, other: Entity):
        if other.type == "player":
            other.damage(self.strength)
            self.original_polygon.rotate(pi)
            self.original_polygon.move(*(Point(cos(self.original_polygon.rotation.degree - pi / 2),
                                                        -sin(self.original_polygon.rotation.degree - pi / 2)) * 60).pos)
