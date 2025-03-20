import pygame
from .card import CardInterface


def draw_hand(screen, hand):
    initial_xy = pygame.Vector2(500, 750)
    total_cards = len(hand)
    cards = []
    for index, card in enumerate(hand):
        current_xy = pygame.Vector2(
            initial_xy.x + (400 * index) / total_cards, initial_xy.y
        )
        cardDraw = CardInterface(card.image, current_xy)
        cardDraw.draw_straight(screen, 0.2)
        cards.append(cardDraw)
    return cards
