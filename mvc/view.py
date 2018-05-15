import logging
import pygame

from mvc import events


class GraphicalView(object):
    """Draws the model's state to the screen."""
    def __init__(self, main_event_manager, model):
        main_event_manager.register_listener(self)
        self._model = model
        self._is_initialized = False
        self._screen = None
        self._small_font = None

    def notify(self, event):
        if isinstance(event, events.QuitEvent):
            self._handle_quit()
        elif isinstance(event, events.InitializeEvent):
            self.initialize()
        elif isinstance(event, events.TickEvent):
            self.render_all()

    def _handle_quit(self):
        self._is_initialized = False
        # ends the pygame graphical display
        pygame.quit()


    def render_all(self):
        if not self._is_initialized:
            return
        # clear display
        self._screen.fill((0, 0, 0))
        some_words = self._small_font.render(
            self._model.text,
            True,
            (0, 255, 0)
        )
        self._screen.blit(some_words, (0, 0))
        pygame.display.update()

    def initialize(self):
        """Set up the pygame graphical display and load graphical resources."""
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('demo game')
        self._screen = pygame.display.set_mode((600, 60))
        self._small_font = pygame.font.Font(None, 40)
        self._is_initialized = True
        logging.info('VIEW INITIALIZED')
