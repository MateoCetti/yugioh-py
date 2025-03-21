import abc

class Screen(metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()
   
    def handle_events(self):
        return None

    def draw_screen(self):
        return None