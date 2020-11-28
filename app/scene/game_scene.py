import pygame
from pygame.sprite import Group

from app.scene.field.field import Field
from app.scene.position import Position
from app.scene.scene import Scene
from app.scene.size import Size
from game.engine.keyboard import KeyboardControlEngine
from game.pad import Pad


class GameScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.pad = self.build_pad()
        self.all_sprites = Group()
        self.add_sprites(sprite=self.pad)
        field = Field(size=Size(800, 600), position=Position(0, 0))
        field.add_sprites_to(scene=self)
        field.add_borders_to(pad=self.pad)

    @staticmethod
    def build_pad():
        pad = Pad(size=Size(75, 15), position=Position(400, 550), color=(255, 255, 255))
        pad.bind_control_engine(engine=KeyboardControlEngine())
        return pad

    def add_sprites(self, sprite):
        self.all_sprites.add(sprite)

    def run(self):

        running = True
        while running:
            self.fill_background(color=(0, 0, 0))
            for event in self.get_events():
                if event.type == pygame.QUIT:
                    running = False
                self.pad.handle(event)

            self.all_sprites.update()
            self.all_sprites.draw(self.window.screen)

            self.render()
        return 0
