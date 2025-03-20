import pygame


def draw_front_straight_card(screen, xy: pygame.Vector2, card_image, resize):
    image = pygame.image.load(card_image)
    scaled_image = pygame.transform.scale(
        image, (image.get_width() *resize, image.get_height() *resize)
    )
    screen.blit(scaled_image, xy)
