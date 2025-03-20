import pygame

def event_handler(to_check):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for event in to_check:
                event.check_if_inside(x, y) 
        elif event.type == pygame.KEYDOWN:
            if event.dict["key"] == 27:
                return False
    return True
