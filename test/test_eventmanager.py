from unittest import mock

from mvc import eventmanager
from mvc import events

class ListenerSpy(object):
    def __init__(self):
        self.notify = mock.MagicMock()


def test_post_calls_notify_once():
    event_manager = eventmanager.EventManager()
    spy = ListenerSpy()
    event_manager.register_listener(spy)
    assert spy.notify.call_count == 0
    event_manager.post(events.Event())
    assert spy.notify.call_count == 1

def test_post_notifies_with_proper_event():
    event_manager = eventmanager.EventManager()
    spy = ListenerSpy()
    event_manager.register_listener(spy)
    event_manager.post(events.TickEvent())
    args, kwargs = spy.notify.call_args
    assert len(args) == 1
    assert isinstance(args[0], events.TickEvent)

def test_multiple_listeners_all_get_notified():
    event_manager = eventmanager.EventManager()
    spies = [ListenerSpy() for i in range(100)]
    for spy in spies:
        event_manager.register_listener(spy)
    event_manager.post(events.QuitEvent())
    for spy in spies:
        assert spy.notify.call_count == 1
        args, kwargs = spy.notify.call_args
        assert isinstance(args[0], events.QuitEvent)

def test_unregister_stops_notification():
    event_manager = eventmanager.EventManager()
    spy = ListenerSpy()
    event_manager.register_listener(spy)
    event_manager.unregister_listener(spy)
    event_manager.post(events.QuitEvent())
    assert spy.notify.call_count == 0
