from enum import Enum

from blackjack.models import Hand


class Moves(str, Enum):
    HIT = "hit"
    STAY = "stay"


class Player:
    def __init__(self, initial_balance: float = 500):
        self.hand = Hand()
        self.balance = initial_balance

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

    @property
    def has_blackjack(self) -> bool:
        return self.hand.value == 21 and len(self.hand) == 2

    def bet(self, minimum_bet: float) -> float:
        while True:
            try:
                bet = float(input("Place your bet: "))
            except ValueError:
                print("Please enter a valid number.")
            else:
                if bet > self.balance:
                    print("You don't have sufficient funds!")
                elif bet < minimum_bet:
                    print(f"The minimum bet is ${minimum_bet}")
                else:
                    return bet


class Dealer:

    def __init__(self):
        self.hand = Hand()

    def make_move(self):
        return Moves.HIT if self.hand.value < 17 else Moves.STAY

    @property
    def has_blackjack(self) -> bool:
        return self.hand.value == 21 and len(self.hand) == 2
