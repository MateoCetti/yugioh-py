import pygame

from .. import colors
from ..screen import Screen
from ..components.button import Button

from events.event_handler import EventHandler

class MenuScreen(Screen):
    def __init__(self, screen):
        self.event_handler = EventHandler()
        self.screen = screen
        self.button = Button(
            500, 500, 100, 25, colors.BLUE, "play", self.sape
        )
        self.event_handler.add_subscriber("on_mouse_button_down", self.button)

    def sape(self):
        print("hola")
        

    def handle_events(self) -> bool:
        return self.event_handler.handle_events()

    def draw_screen(self):
        self.screen.fill(colors.GRAY)
        self.button.draw(self.screen)
