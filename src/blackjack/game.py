from blackjack.models import Deck, Hand
from blackjack.players import Dealer, Player


class Blackjack:
    """Main Game Handler"""
    MINIMUM_BET: float = 1

    def __init__(self, deck: Deck, player: Player, dealer: Dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def start_game(self) -> None:
        while True:
            print("")
            if self.player.balance < self.MINIMUM_BET:
                print("You've ran out of money. "
                      "Please restart this program to try again. Goodbye.")
                break
            play_hand = input(
                f"You are starting with ${self.player.balance}. "
                "Would you like to play a hand? "
            )
            if play_hand == "yes":
                self._play_round()
            elif play_hand == "no":
                print(f"You've ended with ${self.player.balance}. "
                      "Hope you come back soon! Goodbye.")
                break
            else:
                print("Invalid option. Type yes or no.")

    def _play_round(self) -> None:

        bet = self.player.bet(self.MINIMUM_BET)

        self.deck.reset()
        self.deck.shuffle()
        self.player.hand.cards = []
        self.dealer.hand.cards= []

        self.player.hand.add_cards(self.deck.deal(2))
        self.dealer.hand.add_cards(self.deck.deal(2))

        print(f"You are dealt: {self.player.hand}")
        print(f"Dealer is dealt: {self.dealer.hand.cards[0]}, Unknown")

        if self.player.has_blackjack:
            print(f"The dealer has: {self.dealer.hand}")
            if not self.dealer.has_blackjack:
                prize = bet * 1.5
                self.player.balance += prize
                print(f"Blackjack! You win ${prize}!")
            else:
                print("You Tie. Your bet has been returned.")



        try:
            self._move(self.player)
        except ValueError:
            self.player.balance -= bet
            print(f"Your hand value is over 21 and you lose ${bet}. :(")
            return

        print(f"The dealer has: {self.dealer.hand}")
        try:
            self._move(self.dealer)
        except ValueError:
            self.player.balance += bet
            print(f"The dealer busts, you win ${bet}! :)")
            return

        if self.player.hand.value < self.dealer.hand.value:
            self.player.balance -= bet
            print(f"The dealer wins, you lose ${bet}. :(")
        elif self.player.hand.value > self.dealer.hand.value:
            self.player.balance += bet
            print(f"You win ${bet}! :)")
        else:
            print("You Tie. Your bet has been returned.")

    def _move(self, current_player: Player):
        if current_player is self.player:
            name = "You"
            verb = "are"
            end = ""
        else:
            name = "The dealer"
            verb = "is"
            end = "s"

        while True:
            if current_player.hand.value > 21:
                raise ValueError(f"Busted! hand value is {current_player.hand.value}")
            move = current_player.make_move()
            if move == "hit":
                new_card = self.deck.deal()
                print(f"{name} {verb} dealt: {new_card[0]}")
                current_player.hand.add_cards(new_card)
                print(f"{name} now have: {current_player.hand}")
            else:
                print(f"{name} stay{end}.")
                break
