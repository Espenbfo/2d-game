from controller.event_handler import KeyHandler
from controller.main import controller
import pygame
from config import FRAMES_PR_SECOND, WINDOW_SIZE
from player.main import Player


def main():
    pygame.init()
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Espen's spill!")

    screen = pygame.display.set_mode(WINDOW_SIZE)

    player = Player()
    clock = pygame.time.Clock()
    time_delta = clock.tick(FRAMES_PR_SECOND)/1000
    key_handler = KeyHandler()
    while controller(screen, player, time_delta, key_handler):
        pygame.display.flip()
        time_delta = clock.tick(FRAMES_PR_SECOND)/1000


if __name__ == "__main__":
    main()
