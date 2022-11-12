"""Models for Blackjack domain"""
import random
from enum import Enum


class Suits(Enum):
    DIAMOND = "\u2666"
    HEART = "\u2665"
    CLUB = "\u2663"
    SPADE = "\u2660"


class CardValues(Enum):
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN = range(2, 11)
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"


class Card:
    """Model of a Card

    In a game of cards, the most fundamental object is the card, it has a value, a suit
    and a color. However, the information of the color comes with the suit and usually
    has no effect in the game so it will be ommited in this model.

    A card has no behaviour, it only exists as part of a deck or a hand and is used
    during the game
    """

    def __init__(self, value: CardValues, suit: Suits):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value.value}{self.suit.value}"

    def __repr__(self):
        return f"Card(value={self.value.value}, suit={self.suit.value})"


class Deck:
    """Model of a deck of cards.

    This deck will be a simple 52 card deck containing 13 cards of each of the 4 suits.
    For the moment this implementation won't include jokers. They will be added in the
    future in case they are needed.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.cards: list[Card] = []
        for suit in Suits:
            for value in CardValues:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n: int = 1) -> list[Card]:
        return [self.cards.pop() for _ in range(n)]



class Hand:
    """Model of a hand in blackjack

    This hand holds the game of a player or dealer and calculates its value.
    For the moment it is blackjack specific.
    """

    def __init__(self, cards: list[Card] = None):
        self.cards = cards or []

    def add_cards(self, cards: list[Card]) -> None:
        self.cards += cards

    @property
    def value(self) -> int:
        total = 0
        aces = 0
        for card in self.cards:
            if card.value in [CardValues.JACK, CardValues.QUEEN, CardValues.KING]:
                total += 10
            elif card.value is CardValues.ACE:
                aces += 1
            else:
                total += card.value.value
        if aces > 0:
            for _ in range(aces):
                if total + 11 <= 21:
                    total += 11
                else:
                    total += 1

        return total

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
