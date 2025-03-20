import abc

class Event(metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()

    def check_if_inside(self):
        return None