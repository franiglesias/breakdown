import pygame


class EventMother(object):
    @staticmethod
    def quit():
        return pygame.event.Event(pygame.QUIT)

    @staticmethod
    def any_key_pressed():
        return pygame.event.Event(pygame.KEYDOWN, unicode="a", key=pygame.K_a, mod=pygame.KMOD_NONE)

    @staticmethod
    def key_pressed(key):
        name = 'K_' + key
        getattr(pygame, name)
        return pygame.event.Event(pygame.KEYDOWN, unicode=key, key=pygame.K_a, mod=pygame.KMOD_NONE)
