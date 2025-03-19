import pygame
import interface.colors as colors

def draw_rectangle_with_text(x, y, width, height, text, color, font, screen):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, colors.WHITE)
    screen.blit(text_surface, (x + 10, y + 10))


def draw_hand(hand, font, screen):
    initial_xy = pygame.Vector2(300, 750)
    for index, card in enumerate(hand):
        current_xy = pygame.Vector2(initial_xy.x + 210 * index, initial_xy.y)
        draw_rectangle_with_text(
            current_xy.x, current_xy.y, 200, 250, card.name, colors.NORMAL_MONSTER_BG, font, screen
        )


def screen_fill(screen):
    screen.fill(colors.GRAY)


def event_handler(to_check):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            to_check[0].check_if_inside(x,y)
        elif event.type == pygame.KEYDOWN:
            if event.dict["key"] == 27:
                return False
    return True
