import pygame


class CardInterface:
    def __init__(self, image, xy: pygame.Vector2):
        self.image = pygame.image.load(image)
        self.xy = xy
        self.wh = pygame.Vector2(
            self.image.get_width(), self.image.get_height()
        )  # width and height

    def draw_straight(self, screen, resize):
        scaled_image = pygame.transform.scale(
            self.image,
            (self.image.get_width() * resize, self.image.get_height() * resize),
        )
        screen.blit(scaled_image, self.xy)

    def check_if_inside(self, x, y):
        if (
            x > self.xy.x
            and x < self.xy.x + self.wh.x
            and y > self.xy.y
            and y < self.xy.y + self.wh.y
        ):
            self.xy = pygame.Vector2(x, y)
