from app.scene import Scene
from app.window import Window


class App(object):
    def __init__(self):
        self.window = Window(width=800, height=600, title='Breakdown')
        self.window.add_scene(scene=Scene(self.window))

    def run(self):
        return self.window.run()
