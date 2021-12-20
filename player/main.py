from player.display import display


class Player:

    def __init__(self):
        self.coords = (0, 0)
        self.size = (50, 50)

    def display(self, screen):
        display(screen, self.coords, self.size)
