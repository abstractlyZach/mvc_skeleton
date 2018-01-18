import weakref


class EventManager(object):
    """Coordinates communication between model, view, and controller."""
    def __init__(self):
        self._listeners = weakref.WeakKeyDictionary()

    def register_listener(self, listener):
        """Adds a listener to our notification list."""
        self._listeners[listener] = 1

    def unregister_listener(self, listener):
        """Remove a listener from our notification list. Auto-removes any
        listeners who stop existing because of the weak-key dictionary."""
        if listener in self._listeners.keys():
            del self._listeners[listener]

    def post(self, event):
        """Notify all the listeners that an event has occurred."""
        # print(str(event))
        for listener in self._listeners.keys():
            listener.notify(event)