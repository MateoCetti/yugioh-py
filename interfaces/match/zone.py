import pygame
from interfaces import colors

ZONE_WIDTH = 222
ZONE_HEIGHT = 250

class Zone():
    def __init__(self, xy: pygame.Vector2):
        self.xy = xy
        self.card = None
    
    def draw(self, screen):
        pygame.draw.rect(screen, colors.GREEN, (self.xy.x, self.xy.y, ZONE_WIDTH, ZONE_HEIGHT))