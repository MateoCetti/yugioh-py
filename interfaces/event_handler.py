import pygame



def event_handler(to_check, dragging):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            dragging = True
            for event in to_check:
                event.check_if_inside(x, y)
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                x, y = event.pos
                for event in to_check:
                    aux = event.check_if_inside(x, y)
                    if aux: break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Clic izquierdo
                dragging = False  # Detiene el arrastre
        elif event.type == pygame.KEYDOWN:
            if event.dict["key"] == 27:
                return False
        
    return True, dragging
