from math import sin, cos, pi
from entity.main import Entity
from helpers.degree import Degree
from helpers.point import Point
from shape.triangle import Triangle


class Bullet(Entity):
    def __init__(self, x, y, size=10, strength=10, initial_rotation=Degree(0)):
        super().__init__(Triangle(0, 0, size, size), initial_position=Point(x, y))
        self.type = "bullet"
        self.strength = strength
        self.original_polygon.rotation = initial_rotation
        self.speed = 300

    def collide(self, other: Entity):
        self.to_be_deleted = True

        other.damage(self.strength)

    def tick(self, game_state):
        self.move(game_state.time_delta)

    def move(self, time_delta):
        self.display_polygon = self.original_polygon.move(*(Point(cos(self.original_polygon.rotation.degree - pi / 2),
                                                                  -sin(
                                                                      self.original_polygon.rotation.degree - pi / 2)) *
                                                            time_delta * self.speed).pos, None)
        if self.original_polygon.outside_bounds():
            self.to_be_deleted = True
