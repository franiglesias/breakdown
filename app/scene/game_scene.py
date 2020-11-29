import pygame

from pygame.sprite import Group
from pygame.time import Clock

from app.scene.field.field import Field
from app.scene.position import Position
from app.scene.scene import Scene
from app.scene.size import Size
from game.ball import Ball
from game.engine.keyboard import KeyboardControlEngine
from game.pad import Pad

FPS = 180


class GameScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.pad = self.build_pad()
        self.ball = self.build_ball()
        self.all_sprites = Group()
        self.add_sprites(sprite=self.pad)
        self.add_sprites(sprite=self.ball)
        field = self.build_field()
        field.add_sprites_to(scene=self)
        field.add_borders_to(observer=self.pad)

        field.add_borders_to(observer=self.ball)
        field.add_top_to(observer=self.ball)

        self.ball.bind_top(top=self.pad)

    @staticmethod
    def build_field():
        return Field(size=Size(800, 600), position=Position(0, 0))

    @staticmethod
    def build_ball():
        return Ball(size=Size(15, 15), position=Position(400, 300), color=(255, 255, 255))

    @staticmethod
    def build_pad():
        pad = Pad(size=Size(75, 15), position=Position(400, 550), color=(255, 255, 255))
        pad.bind_control_engine(engine=KeyboardControlEngine())
        return pad

    def add_sprites(self, sprite):
        self.all_sprites.add(sprite)

    def run(self):
        running = True
        clock = Clock()
        while running:
            self.fill_background(color=(0, 0, 0))
            for event in self.get_events():
                if event.type == pygame.QUIT:
                    running = False
                self.pad.handle(event)

            self.all_sprites.update()
            self.all_sprites.draw(self.window.screen)

            self.render()
            clock.tick(FPS)
        return 0
