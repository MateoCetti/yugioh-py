import pygame
from .card import CardInterface
from game.cards.card import Card
from typing import List

class handInterface():
    _hand: List[CardInterface] = []
    
    def __init__(self):
        pass

    def draw(self, screen):
        for card in self._hand:
            card.draw_straight(screen)
    
    def create_card(self, card: Card) -> CardInterface:
        cards = len(self._hand)
        xy = pygame.Vector2(400+200*cards, 700)
        newCard = CardInterface(card.image,xy , 0.2)
        self._hand.append(newCard)
        return newCard

    def get_cards(self):
        return self._hand
