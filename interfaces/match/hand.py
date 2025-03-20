import pygame
from .card import draw_front_straight_card


def draw_hand(screen, hand):
    initial_xy = pygame.Vector2(500, 750)
    total_cards = len(hand)
    for index, card in enumerate(hand):
        current_xy = pygame.Vector2(initial_xy.x + (400 * index)/total_cards, initial_xy.y)
        draw_front_straight_card(screen, current_xy.x, current_xy.y, card.image, 0.2)
