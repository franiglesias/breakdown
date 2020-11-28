from pygame import Surface
from pygame.sprite import Sprite


class Border(Sprite):
    def __init__(self, size, position, color):
        super().__init__()
        self.image = self.create_image(size, color)
        self.rect = self.image.get_rect()
        self.rect.y = position.y()
        self.rect.x = position.x()

    @staticmethod
    def create_image(size, color):
        image = Surface(size.tuple())
        image.fill(color)
        return image
