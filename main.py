import logging

from mvc import eventmanager
from mvc import model
from mvc import view
from mvc import controller


def set_up_logging():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main():
    set_up_logging()
    # handles initialize, quit, and ticks
    main_event_manager = eventmanager.EventManager()
    input_event_manager = eventmanager.EventManager()
    game_model = model.Model(main_event_manager, input_event_manager)
    keyboard = controller.Controller(main_event_manager,
                                     input_event_manager,
                                     game_model)
    graphics = view.GraphicalView(main_event_manager, game_model)
    game_model.run()


if __name__ == '__main__':
    main()