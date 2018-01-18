from mvc import eventmanager
from mvc import events
from mvc import model

class QuitsAfterFourTicks(object):
    """sends a quit event after 4 ticks"""
    def __init__(self, event_manager):
        self.tick_count = 0
        self._event_manager = event_manager
        self._event_manager.register_listener(self)

    def notify(self, event):
        if isinstance(event, events.TickEvent):
            self.tick_count += 1
            if self.tick_count >= 4:
                self._event_manager.post(events.QuitEvent())



def test_model_four_ticks_before_quit():
    event_manager = eventmanager.EventManager()
    game_state = model.Model(event_manager)
    quitter = QuitsAfterFourTicks(event_manager)
    game_state.run()
    assert len(event_manager.events) == 5

