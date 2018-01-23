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
        self._text = 'The View is drawing on your screen!'
        self._starting_new_word = False

    def notify(self, event):
        if isinstance(event, events.QuitEvent):
            # ends the pygame graphical display
            pygame.quit()
        elif isinstance(event, events.InitializeEvent):
            self.initialize()
        elif isinstance(event, events.TickEvent):
            self.render_all()
        elif isinstance(event, events.KeyPressEvent):
            self._handle_keypress(event)

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


    def render_all(self):
        if not self._is_initialized:
            return
        # clear display
        self._screen.fill((0, 0, 0))
        some_words = self._small_font.render(self._text, True, (0, 255, 0))
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
