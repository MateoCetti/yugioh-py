import pygame

from .hand import handInterface
from ..components.button import Button
from .. import colors
from ..screen import Screen
from .field import FieldInterface

from events.event_handler import EventHandler
from game.player import Player
from decks.yugi_deck.deck import yugi_deck


class MatchScreen(Screen):
    def __init__(self, screen):
        self.player = Player(lifepoints=8000, deck=yugi_deck)
        self.screen = screen
        self.hand = handInterface(self.player)
        self.field = FieldInterface()
        self.button = Button(
            500, 500, 100, 25, colors.BLUE, "draw", self.hand.draw_card
        )


    def draw_screen(self):
        self.screen.fill(colors.GRAY)
        self.field.draw(self.screen)
        self.button.draw(self.screen)
        self.hand.draw(self.screen)
    
    def intersections(self):
        self.hand.cards_zones(self.field.get_zones())
                    
            


    def handle_events(self) -> bool:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.button.check_if_inside(x,y)
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    x, y = event.pos
                    for card in self.hand.get_cards():
                        aux = card.check_if_inside(x, y)
                        if aux:
                            break
            elif event.type == pygame.KEYDOWN:
                if event.dict["key"] == 27:
                    return False
        self.intersections()
        return True