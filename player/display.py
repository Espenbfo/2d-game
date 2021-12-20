import pygame
from pygame.surface import Surface
from config import BASE_PLAYER_COLOR
from gameTypes import FloatPairTuple


def display(screen: Surface, coords: FloatPairTuple, size: FloatPairTuple):
    pygame.draw.rect(screen, BASE_PLAYER_COLOR, pygame.Rect(coords, size))
