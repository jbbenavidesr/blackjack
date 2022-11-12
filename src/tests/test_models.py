"""Unit tests for the models of this blackjack implementation"""
from blackjack.models import Card, CardValues, Deck, Hand, Suits


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


def test_hand_inits_with_cards_passed():
    deck = Deck()
    hand = Hand(deck.cards[:2])
    assert hand.cards == deck.cards[:2]


def test_hand_value_is_correct_with_numbers():
    hand1 = Hand(
        [
            Card(CardValues.TWO, Suits.HEART),
            Card(CardValues.FIVE, Suits.HEART),
        ]
    )
    hand2 = Hand(
        [
            Card(CardValues.THREE, Suits.HEART),
            Card(CardValues.FOUR, Suits.HEART),
        ]
    )
    hand3 = Hand(
        [
            Card(CardValues.EIGHT, Suits.HEART),
            Card(CardValues.TEN, Suits.HEART),
        ]
    )
    assert hand1.value == 7
    assert hand2.value == 7
    assert hand3.value == 18


def test_hand_value_is_correct_with_big_cards():
    hand1 = Hand(
        [
            Card(CardValues.JACK, Suits.HEART),
            Card(CardValues.KING, Suits.HEART),
        ]
    )
    hand2 = Hand(
        [
            Card(CardValues.JACK, Suits.HEART),
            Card(CardValues.TWO, Suits.HEART),
            Card(CardValues.SEVEN, Suits.HEART),
        ]
    )
    hand3 = Hand(
        [
            Card(CardValues.QUEEN, Suits.HEART),
            Card(CardValues.KING, Suits.HEART),
            Card(CardValues.EIGHT, Suits.HEART),
        ]
    )
    assert hand1.value == 20
    assert hand2.value == 19
    assert hand3.value == 28


def test_hand_value_with_ace():
    hand1 = Hand(
        [
            Card(CardValues.ACE, Suits.HEART),
            Card(CardValues.KING, Suits.HEART),
        ]
    )
    hand2 = Hand(
        [
            Card(CardValues.ACE, Suits.HEART),
            Card(CardValues.KING, Suits.HEART),
            Card(CardValues.SIX, Suits.HEART),
        ]
    )
    hand3 = Hand(
        [
            Card(CardValues.ACE, Suits.HEART),
            Card(CardValues.ACE, Suits.SPADE),
        ]
    )
    assert hand1.value == 21
    assert hand2.value == 17
    assert hand3.value == 12
