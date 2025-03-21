import pygame

from .hand import handInterface
from .button import Button
from .. import colors
from ..screen import Screen

from events.event_handler import EventHandler
from game.player import Player


class MatchScreen(Screen):
    def __init__(self, screen, player: Player):
        self.event_handler = EventHandler()
        self.player = player
        self.screen = screen
        self.button = Button(
            500, 500, 100, 25, colors.BLUE, "draw", self.player.draw_card
        )
        self.hand = handInterface()
        self.event_handler.add_subscriber("on_mouse_button_down", self.button)

    def _update_events(self):
        if len(self.player.get_hand()) > len(self.hand.get_cards()):
            card = self.hand.create_card(self.player.get_hand()[-1])
            self.event_handler.add_subscriber("on_mouse_button_down", card)

    def handle_events(self) -> bool:
        self._update_events()
        return self.event_handler.handle_events()

    def draw_screen(self):
        self.screen.fill(colors.GRAY)
        self.button.draw(self.screen)
        self.hand.draw(self.screen)
