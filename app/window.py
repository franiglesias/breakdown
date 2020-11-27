import pygame


class Window(object):
    def __init__(self, width, height, title):
        self.screen = self.build_screen(width=width, height=height, title=title)
        self.scenes = []

    def add_scene(self, scene):
        self.scenes.append(scene)

    @staticmethod
    def build_screen(width, height, title):
        pygame.display.set_caption(title)
        return pygame.display.set_mode((width, height))

    def run(self):
        pygame.init()
        exit_code = 0
        for scene in self.scenes:
            exit_code = scene.run()
            if exit_code < 0:
                break

        pygame.quit()
        return exit_code

    def fill_background(self, color):
        self.screen.fill(color)
