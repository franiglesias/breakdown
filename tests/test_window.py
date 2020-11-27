import unittest
from unittest import TestCase, mock

from app.window import Window
from tests.event_mother import EventMother


class TestWindow(TestCase):

    def setUp(self) -> None:
        self.window = Window(800, 600, 'Test')

    scene_ref = 'app.scene.scene.Scene'

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch(scene_ref)
    def test_exit_if_scene_ends_without_error(self, events, scene):
        scene.run.return_value = 0
        self.window.add_scene(scene)
        self.assertEqual(0, self.window.run())

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch(scene_ref)
    def test_exit_with_error_if_scene_returns_error(self, events, scene):
        scene.run.return_value = -1
        self.window.add_scene(scene)
        self.assertEqual(-1, self.window.run())

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    @unittest.mock.patch(scene_ref)
    @unittest.mock.patch(scene_ref)
    def test_exit_with_error_if_any_scene_returns_error(self, events, scene_1, scene_2):
        scene_1.run.return_value = -1
        scene_2.run.return_value = 0
        self.window.add_scene(scene_1)
        self.window.add_scene(scene_2)
        self.assertEqual(-1, self.window.run())
