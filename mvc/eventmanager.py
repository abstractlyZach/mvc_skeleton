import logging
import weakref

from . import events


def should_be_logged(event):
    """Returns True if the event should be logged."""
    if not isinstance(event, events.TickEvent):
        return True

class EventManager(object):
    """Coordinates communication between model, view, and controller."""
    def __init__(self):
        self._listeners = weakref.WeakKeyDictionary()
        self._events = []

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
        if should_be_logged(event):
            logging.info(str(event))
        self._events.append(event)
        for listener in self._listeners.keys():
            listener.notify(event)

    @property
    def events(self):
        return self._events
