from pygame import Surface
from pygame.sprite import Sprite

from game.engine.keyboard import KeyboardControlEngine


class Pad(Sprite):
    def __init__(self, size, position, color):
        super().__init__()

        self.image = self.image_of_pad(size, color)
        self.rect = self.image.get_rect()
        self.rect.y = position[0]
        self.rect.x = position[1] - size[1] / 2
        self.dx = 0
        self.control_engine = None

    def bind_control_engine(self, engine):
        self.control_engine = engine

    @staticmethod
    def image_of_pad(size, color):
        image = Surface(size)
        image.fill(color)
        return image

    def update(self):
        self.rect.x += self.dx

    def handle(self, event):
        self.control_engine.handle(event)

    def stop(self):
        self.dx = 0

    def right(self):
        self.dx = 1

    def left(self):
        self.dx = -1