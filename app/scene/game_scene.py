import pygame
from pygame.sprite import Group

from app.scene.scene import Scene
from game.engine.keyboard import KeyboardControlEngine
from game.pad import Pad


class GameScene(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.pad = self.build_pad()
        self.all_sprites = Group()
        self.add_sprites(self.pad)

    @staticmethod
    def build_pad():
        pad = Pad(size=(75, 15),position=(530, 400),color=(255, 255, 255))
        KeyboardControlEngine(pad)
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
