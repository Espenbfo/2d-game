import time
from typing import List

from controller.event_handler import KeyHandler
import entity.square_entity.main


class GameState():
    def __init__(self, player: entity.square_entity.main.SquareEntity):
        self.player = player
        self.friendly_entities: List[entity.square_entity.main.SquareEntity] = []
        self.enemy_entities: List[entity.square_entity.main.SquareEntity] = []
        self.time_delta = 0
        self.frame = 0
        self.time = 0
        self.start_time = time.time()
        self.key_handler = KeyHandler()
