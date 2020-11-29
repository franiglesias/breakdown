from pygame import Surface
from pygame.draw import ellipse
from pygame.sprite import Sprite, Group, spritecollide


class Ball(Sprite):
    def __init__(self, size, position, color):
        super().__init__()
        self.position = position
        self.size = size

        self.image = self.create_ball_image(size=size, color=color)

        self.rect = self.image.get_rect()
        self.rect.x = self.position.x()
        self.rect.y = self.position.y()

        self.dx = 1
        self.dy = 1

        self.borders = Group()
        self.pad = Group()
        self.goal = Group()
        self.top = Group()

    @staticmethod
    def create_ball_image(size, color):
        chroma = (0, 255, 0)
        image = Surface(size.tuple())
        image.fill(chroma)
        image.set_colorkey(chroma)
        ellipse(image, color, [0, 0, size.width(), size.height()])
        return image

    def bind_border(self, border):
        self.borders.add(border)

    def bind_top(self, top):
        self.top.add(top)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        for _ in spritecollide(self, self.borders, False):
            self.dx *= -1

        for _ in spritecollide(self, self.top, False):
            self.dy *= -1
