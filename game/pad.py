from pygame import Surface
from pygame.sprite import Sprite, spritecollide, Group


class Pad(Sprite):
    def __init__(self, size, position, color):
        super().__init__()

        self.borders = Group()
        self.image = self.create_pad_image(size=size, color=color)
        self.rect = self.image.get_rect()
        self.rect.y = position.y()
        self.rect.x = position.x() - size.width() / 2
        self.dx = 0
        self.control_engine = None

    def bind_control_engine(self, engine):
        engine.bind_pad(pad=self)
        self.control_engine = engine

    def bind_border(self, border):
        self.borders.add(border)

    @staticmethod
    def create_pad_image(size, color):
        image = Surface(size.tuple())
        image.fill(color)
        return image

    def update(self):
        self.rect.x += self.dx

        for _ in spritecollide(self, self.borders, False):
            self.rect.x -= self.dx
            self.stop()

    def handle(self, event):
        self.control_engine.handle(event)

    def stop(self):
        self.dx = 0

    def right(self):
        self.dx = 1

    def left(self):
        self.dx = -1
