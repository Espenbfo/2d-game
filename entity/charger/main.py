from math import atan2

from entity.main import Entity
from entity.player.main import Player
from shape.arrow import Arrow


class Charger(Entity):
    def __init__(self):
        super().__init__(polygon=Arrow(0,0,40,80), color=(240,80,90))
        self.type="charger"
        self.speed = 100
        self.damage = 10

    def point(self, player: Player, time_delta):
        player.position = player.display_polygon.center
        position = self.display_polygon.center
        diff = player.position-position
        angle = atan2(*diff.pos)
        self.original_polygon.rotation = -angle
        self.display_polygon = self.original_polygon.move(*(diff.normalized()*time_delta*self.speed).pos)

    def tick(self, game_state):
        self.point(game_state.player, game_state.time_delta)

    def collide(self, other: Entity):
        if other.type == "player":
            other.damage(self.damage)