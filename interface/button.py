import pygame
import interface.colors as colors

class Button:
    def __init__(self, x, y, width, height, color, text,func):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.function = func

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = font.render(self.text, True, colors.WHITE)
        screen.blit(text_surface, (self.x + 10, self.y + 10))

    def check_if_inside(self, x,y):
        if(x > self.x and x < self.x+self.width
           and y > self.y and y< self.y+self.height):
            self.function()