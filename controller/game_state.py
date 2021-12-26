import time
from typing import List

from bullet.standard.main import Bullet
from config import WINDOW_SIZE, FRAMES_PR_SECOND
from controller.event_handler import KeyHandler
import entity.charger.main
import entity.main


class GameState():
    def __init__(self, player: entity.main.Entity):
        self.player = player
        self.friendly_entities: List[entity.main.Entity] = [Bullet(100, 100),
                                                            Bullet(200, 100),
                                                            Bullet(100, 200),
                                                            Bullet(200, 200),]
        self.enemy_entities: List[entity.main.Entity] = [entity.charger.main.Charger(0, 0),
                                                         entity.charger.main.Charger(*WINDOW_SIZE)]
        self.time_delta = FRAMES_PR_SECOND/1000
        self.frame = 0
        self.time = 0
        self.start_time = time.time()
        self.key_handler = KeyHandler()

    def add_friendly(self, e:entity.main.Entity):
        self.friendly_entities.append(e)