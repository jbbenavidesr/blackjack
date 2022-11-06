# Black jack

Continuing with my project to learn more of software design and in particular object oriented design,
I will proceed to build a card game engine. In order to have a concrete example, I'll develop it with
the game Black jack on my mind and the first version will consist of a simple blackjack game. However,
the idea is for this library to be flexible enough so that I can add other games easily, probably just
reimplementing a game class that uses logic of cards.

I had been wanting to implement an object oriented model of cards and a card game so I took
[this project from programming expert](https://www.programmingexpert.io/projects/blackjack-card-game)
as a guide for having some kind of user requirements to follow.

## Black jack game

Here I write a sample run of a CLI version of this game that will be developed:

```
Welcome to Blackjack!

You are starting with $500. Would you like to play a hand? yes
Place your bet: -5
The minimum bet is $1.
Place your bet: 2.50
You are dealt: 2♦, A♥
The dealer is dealt: 7♦, Unknown
Would you like to hit or stay? nothing
That is not a valid option. 
Would you like to hit or stay? hit
You are dealt: K♠
You now have: 2♦, A♥, K♠
Would you like to hit or stay? hit
You are dealt: Q♣
You now have: 2♦, A♥, K♠, Q♣
Your hand value is over 21 and you lose $2.50 :(

You are starting with $497.50. Would you like to play a hand? yes
Place your bet: 100
You are dealt: K♦, A♥
The dealer is dealt: J♦, Unknown
The dealer has: J♦, T♥
Blackjack! You win $150 :)

You are starting with $647.50. Would you like to play a hand? yes
Place your bet: 2500
You do not have sufficient funds.
Place your bet: 647.50
You are dealt: 2♦, 4♥
The dealer is dealt: A♠, Unknown
Would you like to hit or stay? hit
You are dealt: Q♦
You now have: 2♦, 4♥, Q♦
Would you like to hit or stay? stay
The dealer has: A♠, 3♥
The dealer hits and is dealt: J♣
The dealer has: A♠, 3♥, J♣
The dealer busts, you win $647.50 :)

You are starting with $1295. Would you like to play a hand? yes
Place your bet: 295
You are dealt: T♦, T♥
The dealer is dealt: 7♠, Unknown
Would you like to hit or stay? stay
The dealer has: 7♠, 3♥
The dealer hits and is dealt: A♠
The dealer has: 7♠, 3♥, A♠
The dealer stays.
The dealer wins, you lose $295 :(

You are starting with $1000. Would you like to play a hand? yes
Place your bet: 1000
You are dealt: Q♦, K♥
The dealer is dealt: 9♠, Unknown
Would you like to hit or stay? stay
The dealer has: 9♠, A♥
The dealer stays.
You tie. Your bet has been returned.

You are starting with $1000. Would you like to play a hand? yes
Place your bet: 1000
You are dealt: 4♠, 7♣
The dealer is dealt: 2♥, Unknown
Would you like to hit or stay? hit
You are dealt: 9♦
You now have: 4♠, 7♣, 9♦
Would you like to hit or stay? stay
The dealer has: 2♥, 6♥
The dealer hits and is dealt: A♠
The dealer has: 2♥, 6♥, A♠
The dealer stays.
You win $1000!

You are starting with $2000. Would you like to play a hand? yes
Place your bet: 2000
You are dealt: 3♦, 5♥
The dealer is dealt: 8♠, Unknown
Would you like to hit or stay? stay
The dealer has: 8♠, 9♥
The dealer stays.
The dealer wins, you lose $2000 :(

You've ran out of money. Please restart this program to try again. Goodbye.
```
