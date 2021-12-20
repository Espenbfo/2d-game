import pygame
from controls import keys

NEWLY_UP = -2
UP = -1
DOWN = 1
NEWLY_DOWN = 2


class KeyHandler:
    def __init__(self):
        self.quit = False
        self.keys = {key: UP for key in keys.keys()}
        self.mouse_keys = {"left": UP, "right": UP}

    def justPressed(self, key: str):
        return self.keys[key] == NEWLY_DOWN

    def pressed(self, key:str):
        return self.keys[key] == DOWN or self.keys[key] == NEWLY_DOWN

    def justReleased(self, key: str):
        return self.keys[key] == NEWLY_UP

    def released(self, key: str):
        return self.keys[key] == UP or self.keys[key] == NEWLY_UP

    def update(self):
        for key, value in self.keys.items():
            if value == NEWLY_UP:
                self.keys[key] = UP
            elif value == NEWLY_DOWN:
                self.keys[key] = DOWN
        for key, value in self.mouse_keys.items():
            if value == NEWLY_UP:
                self.mouse_keys[key] = UP
            elif value == NEWLY_DOWN:
                self.mouse_keys[key] = DOWN

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                for key in self.keys:
                    for key_code in keys[key]:
                        if event.key == key_code:
                            self.keys[key] = NEWLY_DOWN
                            break
            elif event.type == pygame.KEYUP:
                for key in self.keys:
                    for key_code in keys[key]:
                        if event.key == key_code:
                            self.keys[key] = NEWLY_UP
                            break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_keys["left"] = NEWLY_DOWN
                elif event.button == 3:
                    self.mouse_keys["right"] = NEWLY_DOWN

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_keys["left"] = NEWLY_UP
                elif event.button == 3:
                    self.mouse_keys["right"] = NEWLY_UP
