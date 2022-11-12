from blackjack.game import Blackjack
from blackjack.models import Deck
from blackjack.players import Dealer, Player


def main():
    """Entry point for game of blackjack"""

    print("Welcome to Blackjack!")

    game = Blackjack(
        deck=Deck(),
        player=Player(),
        dealer=Dealer(),
    )
    game.start_game()


if __name__ == "__main__":
    main()
