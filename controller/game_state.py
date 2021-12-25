import time
from typing import List

from controller.event_handler import KeyHandler
import entity.charger.main
import entity.main


class GameState():
    def __init__(self, player: entity.main.Entity):
        self.player = player
        self.friendly_entities: List[entity.main.Entity] = []
        self.enemy_entities: List[entity.main.Entity] = [entity.charger.main.Charger(), entity.charger.main.Charger()]
        self.time_delta = 1
        self.frame = 0
        self.time = 0
        self.start_time = time.time()
        self.key_handler = KeyHandler()
