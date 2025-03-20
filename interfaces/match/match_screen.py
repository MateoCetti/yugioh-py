import pygame

from .hand import handInterface
from .button import Button
from .. import colors

from game.player import Player

class MatchScreen():
    def __init__(self, screen, player: Player):
        self.player = player
        self.screen = screen
        self.hand = handInterface()

    def _screen_fill(self):
        self.screen.fill(colors.GRAY)


    def draw_screen(self):
        button = Button(500, 500, 100, 25, colors.BLUE, "draw", self.player.draw_card)
        self._screen_fill()
        button.draw(self.screen)
        if (len(self.player.get_hand()) > len(self.hand.get_cards())):
            self.hand.create_card(self.player.get_hand()[-1])
        self.hand.draw(self.screen)
        return [button, *self.hand.get_cards()]