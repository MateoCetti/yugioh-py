import pygame
from .card import CardInterface
from game.player import Player
from typing import List
from interfaces.match.zone import Zone

class handInterface():
    _hand: List[CardInterface] = []
    
    
    def __init__(self, player: Player):
        self._player: Player = player

    def draw(self, screen):
        for card in self._hand:
            card.draw_straight(screen)
    
    def draw_card(self) -> CardInterface:
        card = self._player.draw_card()
        if not card: return
        cards = len(self._hand)
        xy = pygame.Vector2(400+200*cards, 700)
        newCard = CardInterface(card.image,xy , 0.2)
        self._hand.append(newCard)
        return newCard

    def get_cards(self):
        return self._hand

    def cards_zones(self, zones: List[Zone]):
        for card in self._hand:
            for zone in zones:
                if card.check_if_intersects(zone):
                    if(pygame.mouse.get_pressed()[0]):
                        zone.intersected(card)
                        return
                    else:
                        zone.card = card
                        self._hand.pop(self._hand.index(card))
                        zone.reset_intersect()
                        return
                else: zone.reset_intersect()