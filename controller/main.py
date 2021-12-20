import pygame
from pygame.surface import Surface
import pygame.event

from config import BACKGROUND_COLOR
from controller.event_handler import KeyHandler
from player.main import Player


def controller(screen: Surface, player: Player, td: float, key_handler: KeyHandler):
    key_handler.update()
    if key_handler.quit:
        return False

    screen.fill(BACKGROUND_COLOR)
    player.tick(key_handler, td)
    player.display(screen)
    return True
