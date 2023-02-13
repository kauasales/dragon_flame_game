import game
from config import *


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw_shields(self, sprite, x, y):

        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect(x, y, 0, 0)
        self.image = pygame.transform.scale(self.image, [90, 80])

    def shield_move(self, speed):
        self.rect.y += speed
