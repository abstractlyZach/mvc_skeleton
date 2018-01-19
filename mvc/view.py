import pygame

from mvc import events


class GraphicalView(object):
    """Draws the model's state to the screen."""
    def __init__(self, event_manager, model):
        event_manager.register_listener(self)
        self._model = model
        self._is_initialized = False
        self._screen = None
        self._small_font = None

    def notify(self, event):
        if isinstance(event, events.QuitEvent):
            # is this correct?
            pygame.quit()
        elif isinstance(event, events.InitializeEvent):
            self.initialize()
        elif isinstance(event, events.TickEvent):
            self.render_all()

    def render_all(self):
        if not self._is_initialized:
            return
        # clear display
        self._screen.fill((0, 0, 0))
        some_words = self._small_font.render('The View is drawing on your '
                                             'screen!', True, (0, 255, 0))
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
        print('VIEW INITIALIZED')
