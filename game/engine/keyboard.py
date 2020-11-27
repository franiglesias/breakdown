import pygame


class KeyboardControlEngine(object):
    def __init__(self, pad):
        self.pad = pad
        self.pad.bind_control_engine(self)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_pad_left()
            elif event.key == pygame.K_RIGHT:
                self.move_pad_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.stop_pad()
            elif event.key == pygame.K_RIGHT:
                self.stop_pad()

    def move_pad_right(self):
        self.pad.right()

    def move_pad_left(self):
        self.pad.left()

    def stop_pad(self):
        self.pad.stop()
