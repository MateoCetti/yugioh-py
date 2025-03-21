import pygame
from game.player import Player

from interfaces.match.match_screen import MatchScreen


def print_hand(hand):
    print("\n".join(f"{i} {str(obj)}" for i, obj in enumerate(hand)))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    
    running = True
    match_screen = MatchScreen(screen)
    while running:
        running = match_screen.handle_events()
        match_screen.draw_screen()
        pygame.display.flip()
        clock.tick(60)
    
    print("quitting")
    pygame.quit()
