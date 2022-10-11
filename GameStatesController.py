import enum


class game_states(enum.Enum):
    main_menu = 0
    game = 1
    
class game_states_controller(object):
    def __init__(self):
        self.state = game_states.main_menu
        
    def switch_game(self):
        self.state = game_states.game
    