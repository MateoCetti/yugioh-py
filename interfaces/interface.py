import pygame
from .match.match_screen import MatchScreen
from .screen import Screen

class Interface:
    def __init__(self):
        pygame.init()
        self.display = None
        self.clock = None
        self.screen: Screen | None = None

    def start(self):
        self.display = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.screen: Screen = MatchScreen(self.display)

    def stop(self):
        print("Quitting.")
        pygame.quit()

    def iterate(self) -> bool:
        running = self.screen.handle_events()
        self.screen.draw_screen()
        pygame.display.flip()
        self.clock.tick(60)
        return running

