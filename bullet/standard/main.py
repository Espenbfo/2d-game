from pygame.rect import Rect


class SquareBullet:
    def __init__(self, rect: Rect):
        self.rect = rect

    def collides(self, rect):
        return self.rect.colliderect(rect)