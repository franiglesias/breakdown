import unittest
from unittest import TestCase, mock

from app.window import Window
from tests.event_mother import EventMother


class TestWindow(TestCase):

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch('app.scene.Scene')
    def test_exit_if_scene_ends_without_error(self, events, scene):
        scene.run.return_value = 0
        window = Window(800, 600, 'Test')
        window.add_scene(scene)
        self.assertEqual(0, window.run())

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch('app.scene.Scene')
    def test_exit_with_error_if_scene_returns_error(self, events, scene):
        scene.run.return_value = -1
        window = Window(800, 600, 'Test')
        window.add_scene(scene)
        self.assertEqual(-1, window.run())

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch('app.scene.Scene')
    @unittest.mock.patch('app.scene.Scene')
    def test_exit_with_error_if_any_scene_returns_error(self, events, scene_1, scene_2):
        scene_1.run.return_value = -1
        scene_2.run.return_value = 0
        window = Window(800, 600, 'Test')
        window.add_scene(scene_1)
        window.add_scene(scene_2)
        self.assertEqual(-1, window.run())
