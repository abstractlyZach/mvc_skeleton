import pygame

from . import events
from . import settings


class Model(object):
    """Tracks the game state."""
    def __init__(self, main_event_manager, input_event_manager):
        self._main_event_manager = main_event_manager
        self._main_event_manager.register_listener(self)
        input_event_manager.register_listener(self)
        self._running = False
        self._clock = pygame.time.Clock()
        self._text = 'The View is drawing on your screen!'
        self._starting_new_word = False

    @property
    def text(self):
        return self._text

    def notify(self, event):
        if isinstance(event, events.QuitEvent):
            self._running = False
        elif isinstance(event, events.KeyPressEvent):
            self._handle_keypress(event)

    def run(self):
        """Starts the game loop. Pumps a tick into the event manager for
        each loop."""
        self._running = True
        self._main_event_manager.post(events.InitializeEvent())
        while self._running:
            tick = events.TickEvent()
            self._main_event_manager.post(tick)
            self._clock.tick(settings.FPS)

    def _handle_keypress(self, event):
        key_text = pygame.key.name(event.key)
        if len(key_text) == 1:
            self._update_text_with_char_input(key_text)
        else:
            self._handle_non_alphanum_keypress(key_text)

    def _update_text_with_char_input(self, new_char):
        if self._starting_new_word:
            self._text = new_char
            self._starting_new_word = False
        else:
            self._text += new_char

    def _handle_non_alphanum_keypress(self, key_text):
        if key_text == 'return':
            self._starting_new_word = True
        elif key_text == 'space':
            self._update_text_with_char_input(' ')
        elif key_text == 'backspace':
            self._backspace()
        else:
            pass

    def _backspace(self):
        self._text = self._text[:-1]

