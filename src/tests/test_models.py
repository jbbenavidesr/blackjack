"""Unit tests for the models of this blackjack implementation"""
from blackjack.models import CardValues, Deck, Suits


def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck_has_13_cards_of_each_suit():
    deck = Deck()
    for suit in Suits:
        cards_with_this_suit = [card for card in deck.cards if card.suit is suit]
        assert len(cards_with_this_suit) == 13


def test_deck_has_card_with_each_suit_for_each_value():
    deck = Deck()
    for value in CardValues:
        suits_for_this_value = [card.suit for card in deck.cards if card.value is value]
        for suit in Suits:
            assert suits_for_this_value.count(suit) == 1


def test_deck_shuffle_changes_the_list_of_cards():
    deck = Deck()

    starting_cards = deck.cards[:]
    deck.shuffle()
    assert starting_cards != deck.cards
