import pygame
from events.event import Event

class CardInterface(Event):
    def __init__(self, image, xy: pygame.Vector2, resize):
        aux =  pygame.image.load(image)
        self.image = pygame.transform.scale(
           aux,
            (aux.get_width() * resize, aux.get_height() * resize),
        )
        self.rect = self.image.get_rect()

    def draw_straight(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_if_inside(self, x, y) -> bool:
        if self.rect.collidepoint((x,y)):
            self.rect.topleft = (x-self.rect.width/2, y-self.rect.height/2)
            return True
        return False
    
    def check_if_intersects(self, object):
        if(self.rect.colliderect(object.rect)):
            object.intersected(self)

    def intersected(self, object):
        print(f"${id(object)}: {object.rect} | {id(self)} {self.rect}")
