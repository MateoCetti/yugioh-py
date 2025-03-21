import pygame

from interfaces import colors
from .zone import Zone, ZONE_WIDTH, ZONE_HEIGHT

MAT_XY = pygame.Vector2(75, 380)
MAT_WIDTH = 1780
MAT_HEIGHT = 600
ZONES_OFFSET = 80


class FieldInterface():
    def __init__(self):
        super().__init__()
        self.zones_1 = {
            i: Zone(
                pygame.Vector2(
                    MAT_XY.x + (ZONE_WIDTH + 10) * i + ZONES_OFFSET, MAT_XY.y + 10
                )
            )
            for i in range(7)
        }
        self.zones_2 = {
            i: Zone(
                pygame.Vector2(
                    MAT_XY.x + (ZONE_WIDTH + 10) * i + ZONES_OFFSET,
                    MAT_XY.y + ZONE_HEIGHT + 20,
                )
            )
            for i in range(7)
        }

    def draw(self, display):
        pygame.draw.rect(
            display, colors.REVERSE_CARD_BG, (MAT_XY.x, MAT_XY.y, MAT_WIDTH, MAT_HEIGHT)
        )
        for zone in [*self.zones_1.values(), *self.zones_2.values()]:
            zone.draw(display)
