import pygame


class Event(object):
    """Superclass for events."""
    def __init__(self):
        self._name = 'Generic Event'

    def __str__(self):
        return self._name


class InitializeEvent(Event):
    def __init__(self):
        self._name = 'Initialize Event'


class QuitEvent(Event):
    """Event created when user quits the program."""
    def __init__(self):
        self._name = 'Quit Event'


class TickEvent(Event):
    """Event for every tick of the model."""
    def __init__(self):
        self._name = 'Tick Event'


class InputEvent(Event):
    """Event created when user gives input."""
    def __init__(self):
        self._name = 'Input Event'


class KeyPressEvent(InputEvent):
    def __init__(self, key):
        self._name = 'Key Press Event'
        self._key = key

    def __str__(self):
        key_name = pygame.key.name(self._key)
        return '{}: {}'.format(self._name, key_name)

    @property
    def key(self):
        return self._key


class ClickEvent(InputEvent):
    def __init__(self, position):
        self._name = 'Click Event'
        self._position = position

    def __str__(self):
        return '{}: {}'.format(self._name, self._position)



