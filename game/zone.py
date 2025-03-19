import copy
from game.cards.card import Card


class Zone:
    _card = None

    def has_card(self):
        return self._card != None

    def set_card(self, card):
        self._card = card

    def remove_card(self):
        aux_card = self._card
        self._card = None
        return aux_card

    def get_card(self):
        return copy.deepcopy(self.card)

    def __str__(self):
        return self._card.__str__() if self.has_card() else "Nada"
