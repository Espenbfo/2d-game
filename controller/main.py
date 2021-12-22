from pygame.surface import Surface

from config import BACKGROUND_COLOR
from controller.event_handler import KeyHandler
from controller.game_state import GameState
from entity.player.main import Player


def controller(screen: Surface, game_state: GameState):
    game_state.key_handler.update()
    if game_state.key_handler.quit:
        return False

    screen.fill(BACKGROUND_COLOR)
    game_state.player.tick(game_state)
    game_state.player.display(screen)
    return True
