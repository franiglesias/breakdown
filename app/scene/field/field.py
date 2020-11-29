from app.scene.field.border import Border
from app.scene.position import Position
from app.scene.size import Size


class Field(object):
    def __init__(self, size, position):
        thickness = 15
        white = (255, 255, 255)
        gray = (150, 150, 150)
        self.left = Border(
            size=Size(thickness, size.height()),
            position=position,
            color=white
        )
        self.right = Border(
            size=Size(thickness, size.height()),
            position=Position(size.width() - thickness, position.y()),
            color=white
        )
        self.top = Border(
            size=Size(size.width() - thickness * 2, thickness),
            position=Position(thickness, position.y()),
            color=white
        )
        self.bottom = Border(
            size=Size(size.width() - thickness * 2, thickness),
            position=Position(thickness, size.height() - thickness),
            color=gray
        )

    def add_sprites_to(self, scene):
        scene.add_sprites(self.left)
        scene.add_sprites(self.right)
        scene.add_sprites(self.top)
        scene.add_sprites(self.bottom)

    def add_borders_to(self, observer):
        observer.bind_border(self.left)
        observer.bind_border(self.right)

    def add_top_to(self, observer):
        observer.bind_top(self.top)
        observer.bind_top(self.bottom)
