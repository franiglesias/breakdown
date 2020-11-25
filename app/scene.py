import pygame


class Scene(object):
    def __init__(self, window):
        self.window = window

    def run(self):
        self.fill_background(color=(0, 0, 0))
        self.render()
        self.wait_until_quit()
        return 0

    def fill_background(self, color):
        self.window.fill_background(color)

    def wait_until_quit(self):
        running = True
        while running:
            for event in self.get_events():
                if event.type == pygame.QUIT:
                    running = False

    @staticmethod
    def get_events():
        return pygame.event.get()

    @staticmethod
    def render():
        pygame.display.flip()
