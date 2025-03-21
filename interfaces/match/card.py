import pygame
from events.event import Event

class CardInterface(Event):
    def __init__(self, image, xy: pygame.Vector2, resize):
        aux =  pygame.image.load(image)
        self.xy = xy
        self.wh = pygame.Vector2(
            aux.get_width()*resize, aux.get_height()*resize
        )  # width and height
        self.image = pygame.transform.scale(
           aux,
            (aux.get_width() * resize, aux.get_height() * resize),
        )

    def draw_straight(self, screen):
        screen.blit(self.image, self.xy)

    def check_if_inside(self, x, y) -> bool:
        if self.xy.x < x < (self.xy.x + self.wh.x) and self.xy.y < y < (
            self.xy.y + self.wh.y
        ):
            self.xy = pygame.Vector2(x-self.wh.x/2, y-self.wh.y/2)
            return True
        return False
