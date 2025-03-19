import pygame
from game.player import Player
from decks.yugi_deck import yugi_deck
from interface.test import event_handler, screen_fill, draw_hand
from interface.button import Button
from interface import colors

def print_hand(hand):
    print("\n".join(f"{i} {str(obj)}" for i, obj in enumerate(hand)))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 16)
    # Fuente
    player_1 = Player(lifepoints=8000, deck=yugi_deck.copy())
    running = True
    button = Button(500,500,100,50,colors.BLUE,"draw", player_1.draw_card)
    while running:
        screen_fill(screen)
        draw_hand(player_1.get_hand(), font, screen)
        running = event_handler([button])
        button.draw(screen, font)
        pygame.display.flip()
        clock.tick(60)
    print("quitting")
    pygame.quit()
