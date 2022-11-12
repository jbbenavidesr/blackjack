from blackjack.models import Deck, Hand


def main():
    """Entry point for game of blackjack"""

    print("Welcome to Blackjack!\n")

    # Init and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal player and dealer hands
    player_cards = Hand([deck.cards.pop() for _ in range(2)])
    dealer_cards = Hand([deck.cards.pop() for _ in range(2)])

    print(f"You are dealt: {player_cards}")
    print(f"Dealer is dealt: {dealer_cards.cards[0]}, Unknown")

    # Player turn
    while True:
        if player_cards.value > 21:
            print("Your hand value is over 21 and you lose")
            break

        will_hit = input("Would you like to hit or stay? ")

        if will_hit == "hit":
            new_card = deck.cards.pop()
            print(f"You are dealt: {new_card}")
            player_cards.cards.append(new_card)
            print(f"You now have: {player_cards}")

        elif will_hit == "stay":
            break

        else:
            print("This is not a valid option.")


if __name__ == "__main__":
    main()
