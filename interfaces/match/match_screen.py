from interfaces.match.hand import draw_hand
from .button import Button
from .. import colors

from game.player import Player

def _screen_fill(screen):
    screen.fill(colors.GRAY)

def draw_screen(screen, player: Player):
    hand = player.get_hand()
    button = Button(500, 500, 100, 25, colors.BLUE, "draw", player.draw_card)
    _screen_fill(screen)
    button.draw(screen)
    cards = draw_hand(screen, hand)
    return [button, *cards]