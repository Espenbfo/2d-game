from controller.event_handler import KeyHandler
from controller.game_state import GameState
from controller.main import controller
import pygame
from config import FRAMES_PR_SECOND, WINDOW_SIZE
from entity.player.main import Player


def main():
    pygame.init()
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Espen's spill!")

    screen = pygame.display.set_mode(WINDOW_SIZE)

    game_state = GameState(Player())
    clock = pygame.time.Clock()
    while controller(screen, game_state):
        pygame.display.flip()
        game_state.time_delta = clock.tick(FRAMES_PR_SECOND)/1000
        print(clock.get_fps())


if __name__ == "__main__":
    main()
