from abc import ABC


class Card(ABC):
    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def __str__(self):
        return f"{self.name}"
