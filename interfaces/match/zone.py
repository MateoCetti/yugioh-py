import pygame
from interfaces import colors

ZONE_WIDTH = 222
ZONE_HEIGHT = 250

class Zone():
    def __init__(self, xy: pygame.Vector2):
        self.card = None
        self.color = colors.GREEN
        self.rect = pygame.Rect(xy.x, xy.y, ZONE_WIDTH, ZONE_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_if_intersects(self, object):
        if(self.rect.colliderect(object.rect)):
            object.intersected(self)

    def intersected(self, object):
        self.color = colors.RED
    
    def reset_intersect(self):
        self.color = colors.GREEN