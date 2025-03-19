from game.zone import Zone


class Player:
    _lifepoints = 8000
    _field = (
        Zone(),
        Zone(),
        Zone(),
        Zone(),
        Zone(),
    )
    _graveyard = []

    _hand = []

    def __init__(self, lifepoints, deck):
        self._lifepoints = lifepoints
        self._deck = deck

    def add_lifepoints(self, lifepoints):
        self._lifepoints += lifepoints

    def substract_lifepoints(self, lifepoints):
        self._lifepoints -= lifepoints

    def draw_card(self):
        self._hand.append(self._deck.pop())

    def get_hand(self):
        return self._hand.copy()

    def get_field(self):
        return self._field

    def place_card_on_zone(self, card_index, zoneIndex):
        self._field[zoneIndex].set_card(self._hand.pop(card_index))
