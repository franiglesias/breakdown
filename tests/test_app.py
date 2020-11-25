import unittest
from unittest import mock, TestCase
from app.app import App
from tests.event_mother import EventMother


class AppTestCase(TestCase):

    def setUp(self) -> None:
        self.app = App()

    @unittest.mock.patch('pygame.event.get', return_value=[EventMother.quit()])
    def test_app_should_run_and_stop_when_quit(self, event_mock):
        self.assertEqual(0, self.app.run())


if __name__ == '__main__':
    unittest.main()
