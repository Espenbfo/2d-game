from math import atan2, sin, cos, pi

from entity.main import Entity
from entity.player.main import Player
from helpers.degree import Degree
from shape.arrow import Arrow
from helpers.point import Point


class Charger(Entity):
    def __init__(self):
        super().__init__(polygon=Arrow(0, 0, 10, 40), color=(240, 80, 90))
        self.type = "charger"
        self.speed = 200
        self.damage = 10
        self.rotation_speed = 1

    def point(self, player: Player, time_delta):
        player.position = player.display_polygon.center
        position = self.display_polygon.center
        diff = player.position - position
        angle = Degree(atan2(*diff.pos))
        self.original_polygon.rotate((angle - self.original_polygon.rotation.degree) * time_delta * self.rotation_speed)
        self.display_polygon = self.original_polygon.move(*(Point(cos(self.original_polygon.rotation.degree - pi / 2),
                                                                  -sin(
                                                                      self.original_polygon.rotation.degree - pi / 2)) *
                                                            time_delta * self.speed).pos)

    def tick(self, game_state):
        self.point(game_state.player, game_state.time_delta)

    def collide(self, other: Entity):
        if other.type == "player":
            other.damage(self.damage)
            self.original_polygon.rotate(pi)
            self.original_polygon.move(*(Point(cos(self.original_polygon.rotation.degree - pi / 2),
                                                        -sin(self.original_polygon.rotation.degree - pi / 2)) * 60).pos)
