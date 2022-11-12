from enum import Enum

from blackjack.models import Hand


class Moves(str, Enum):
    HIT = "hit"
    STAY = "stay"


class Player:
    def __init__(self):
        self.hand = Hand()

    def make_move(self):
        while True:
            try:
                return self._ask_move()
            except ValueError:
                print("This is not a valid option.")

    def _ask_move(self):
        move = input("Would you like to hit or stay? ")
        if move in Moves.__members__.values():
            return Moves(move)
        else:
            raise ValueError("Move is not valid!")



class Dealer:

    def __init__(self):
        self.hand = Hand()

    def make_move(self):
        return Moves.HIT if self.hand.value < 17 else Moves.STAY

