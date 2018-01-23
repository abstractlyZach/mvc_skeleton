import pygame

from . import events


class Controller(object):
    """Handles input by posting events to the event manager when input
    happens."""
    def __init__(self, event_manager, model):
        self._event_manager = event_manager
        self._event_manager.register_listener(self)
        self._model = model

    def notify(self, event):
        if isinstance(event, events.TickEvent):
            for input_event in pygame.event.get():
                self._handle_event(input_event)

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self._event_manager.post(events.QuitEvent())
        elif (event.type == pygame.KEYUP) and \
                (event.key == pygame.K_ESCAPE):
            self._event_manager.post(events.QuitEvent())
        elif (event.type == pygame.KEYUP):
            self._event_manager.post(events.KeyPressEvent(event.key))


