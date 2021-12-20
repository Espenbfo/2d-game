from controller.main import controller
import pygame
from config import FRAMES_PR_SECOND, WINDOW_SIZE

def main():
    pygame.init()
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Espen's spill!")

    screen = pygame.display.set_mode(WINDOW_SIZE)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()