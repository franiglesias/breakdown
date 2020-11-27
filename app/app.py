from app.scene.game_scene import GameScene
from app.window import Window


class App(object):
    def __init__(self):
        self.window = Window(width=800, height=600, title='Breakdown')
        self.window.add_scene(scene=GameScene(self.window))

    def run(self):
        return self.window.run()
