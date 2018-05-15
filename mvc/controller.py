import pygame

from . import events


class Controller(object):
    """Handles input by posting events to the event manager when input
    happens."""
    def __init__(self, main_event_manager, input_event_manager, model):
        main_event_manager.register_listener(self)
        self._input_event_manager = input_event_manager
        self._model = model

    def notify(self, event):
        if isinstance(event, events.TickEvent):
            for input_event in pygame.event.get():
                self._handle_event(input_event)

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self._input_event_manager.post(events.QuitEvent())
        elif (event.type == pygame.KEYUP) and \
                (event.key == pygame.K_ESCAPE):
            self._input_event_manager.post(events.QuitEvent())
        elif (event.type == pygame.KEYUP):
            self._input_event_manager.post(events.KeyPressEvent(event.key))


