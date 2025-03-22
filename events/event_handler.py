import pygame
# from event import Event
EVENT_TYPES = ("on_mouse_button_down", "on_mouse_motion", "on_key_down", "intersection")


class EventHandler:
    def __init__(self):
        self.subscribers = {
            event_type: [] for event_type in EVENT_TYPES
        }
        self.dragging = False

    def add_subscriber(self, event_type, subscriber):
        self.subscribers[event_type].append(subscriber)

    def remove_subscriber(self, event_type, index):
        self.subscribers[event_type].pop(index)

    def handle_events(self) -> bool:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.dragging = True
                # TODO: check if object is on top of others
                for event in self.subscribers["on_mouse_button_down"]:
                    is_inside = event.check_if_inside(x, y)
                    if(is_inside):
                        self.subscribers["on_mouse_motion"].append(event)
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    x, y = event.pos
                    for event in self.subscribers["on_mouse_motion"]:
                        aux = event.check_if_inside(x, y)
                        if aux:
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                if event.button == 1:  # Clic izquierdo
                    self.subscribers["on_mouse_motion"] = []
            elif event.type == pygame.KEYDOWN:
                if event.dict["key"] == 27:
                    return False
                
        for event in self.subscribers["intersection"]:
            for event2 in self.subscribers["intersection"]:
                if (event != event2 and event.check_if_intersects(event2)):
                    event2.intersected(event)

        return True
