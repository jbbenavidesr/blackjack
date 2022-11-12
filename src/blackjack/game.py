from blackjack.models import Deck, Hand
from blackjack.players import Dealer, Player


class BlackJack:
    """Main Game Handler"""

    def __init__(self, deck: Deck, player: Player, dealer: Dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def start_game(self) -> None:
        while True:
            print("")
            play_hand = input("Would you like to play a hand? ")
            if play_hand == "yes":
                self._play_round()
            elif play_hand == "no":
                print("Okay, hope you come back soon!")
                break
            else:
                print("Invalid option.")

    def _play_round(self) -> None:
        self.deck.reset()
        self.deck.shuffle()

        self.player.add_cards(self.deck.deal(2))
        self.dealer.add_cards(self.deck.deal(2))

        print(f"You are dealt: {self.player.hand}")
        print(f"Dealer is dealt: {self.dealer.hand.cards[0]}, Unknown")

        try:
            self._move(self.player)
        except ValueError:
            print("Your hand value is over 21 and you lose. :(")
            return

        print(f"The dealer has: {self.dealer.hand}")
        try:
            self._move(self.dealer)
        except ValueError:
            print("The dealer busts, you win! :)")
            return

        if self.player.hand.value < self.dealer.hand.value:
            print("The dealer wins, you lose. :(")
        elif self.player.hand.value > self.dealer.hand.value:
            print("You win! :)")
        else:
            print("You Tie.")

    def _move(self, current_player: Player):
        while True:
            if current_player.hand.value > 21:
                raise ValueError(f"Busted! hand value is {current_player.hand.value}")
            move = current_player.make_move()
            if move == "hit":
                new_card = self.deck.deal()
                print(f"You are dealt: {new_card[0]}")
                current_player.hand.add_cards(new_card)
                print(f"You now have: {current_player.hand}")
            else:
                print(f"{current_player} stays.")
                break
