from pygame.surface import Surface

from config import BACKGROUND_COLOR
from controller.game_state import GameState


def controller(screen: Surface, game_state: GameState):
    game_state.key_handler.update()
    if game_state.key_handler.quit:
        return False

    screen.fill(BACKGROUND_COLOR)
    game_state.player.tick(game_state)

    for index, enemy in enumerate(game_state.enemy_entities):
        if enemy.to_be_deleted:
            game_state.enemy_entities.pop(index)
            continue
        enemy.tick(game_state)
        if game_state.player.is_colliding(enemy):
            game_state.player.collide(enemy)
            enemy.collide(game_state.player)
        enemy.display(screen)

    for index, friendly in enumerate(game_state.friendly_entities):
        if friendly.to_be_deleted:
            game_state.friendly_entities.pop(index)
            continue
        friendly.tick(game_state)

        for enemy in game_state.enemy_entities:
            if friendly.is_colliding(enemy):
                friendly.collide(enemy)
                enemy.collide(friendly)

        friendly.display(screen)

    game_state.player.display(screen)
    return True
