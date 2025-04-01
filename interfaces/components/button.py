import pygame
import interfaces.colors as colors

class Button:

    def __init__(self, x, y, width, height, color, text,func):
        self.font = pygame.font.Font(None, 20)
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.text = text
        self.function = func

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, colors.WHITE)
        screen.blit(text_surface, (self.rect.left + 10, self.rect.top + 10))

    def check_if_inside(self, x,y):
        if(self.rect.collidepoint(x,y)):
            self.function()