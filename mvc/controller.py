class Controller(object):
    """Handles input by posting events to the event manager when input
    happens."""
    def __init__(self, event_manager, model):
        self._event_manager = event_manager
        self._event_manager.register_listener(self)
        self._model = model

    def notify(self, event):
        pass
