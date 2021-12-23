from pygame.surface import Surface

from config import BACKGROUND_COLOR
from controller.game_state import GameState


def controller(screen: Surface, game_state: GameState):
    game_state.key_handler.update()
    if game_state.key_handler.quit:
        return False

    screen.fill(BACKGROUND_COLOR)
    game_state.player.tick(game_state)
    game_state.player.display(screen)
    for enemy in game_state.enemy_entities:
        enemy.tick(game_state)
        enemy.display(screen)
        if game_state.player.display_polygon.collide(enemy.display_polygon):
            game_state.player.collide(enemy)
            enemy.collide(game_state.player)
    return True
