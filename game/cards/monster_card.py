from .card import Card


class MonsterCard(Card):
    def __init__(self, name, description, attack, defense, level, attribute):
        super().__init__(name, description)
        self.attack = attack
        self.defense = defense
        self.level = level
        self.attribute = attribute

    def __str__(self):
        return super().__str__() + f" ATK: {self.attack} DEF: {self.defense}"
