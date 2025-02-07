# CSC 1019 Project 1 (Terminal Jack)

This CLI based Blackjack game utilizes **Object Oriented Programming**, **Moduels**, **Parallel Arrays (Dicts)**, and **Nested Loops**

### Project Requirments

> - Modules - /models
> - Parallel Arrays (Dicts) - /models/card.py
> - Nested Loops - /models/deck.py
> - [Psuedocode](https://docs.google.com/document/d/1f2Hn8JHXtVvwcB-JNACIGDwMxlJp3PZSVbY7nKyXmII/edit?usp=sharing)
> - [Flowchart]()

## Playing The Game

The program depends on inputs from the user. Inputs are not case-sensitive and only one character is needed, full words are optional.
Typical Prompts will read:
`(H)it, (S)tand, (D)ouble Down, Spli(T): `
You will have an option to quit the program before a game starts, but you cannot quit in the middle of a round. Like the actual game, you can't just up and leave the table in the middle of a round.
`Press any key to continue or (Q)uit: `

### Rules of Blackjack
The general rule is to beat the dealer by having a higher value of cards. During the start of the round, the dealer and player are dealt two cards each. The player's cards are face up, the dealer only has one card face up.
- The suite does not matter.
- Having a value of 21 is considered "Blackjack". This is also the maximum value you can have in blackjack. Going over 21 is considered "Bust".
- Number cards 2-10 are valued at the numbers.
- All face cards (King, Queen, Jack) are valued at 10.
- Ace cards are valued at 11 if you won't go over 21, otherwise it's valued at 1.
- The Dealer must stay on 17.

The four choices you have during a turn is as follows:
- **Hit**. Take another card.
- **Stand**. Take no more cards. 
- **Double Down**. Only available after the initial deal. Take exactly one card, you cannot hit again.
- **Split**. Only available after the initial deal and only if you have a pair. Any two cards that are each worth 10 (Tens, Jacks, Queens, or Kings) are considered a pair. Essentially having two hands.

After your turn, the dealer will continue to hit until his cards are valued 17 or higher.
Whoever has the higher value, wins.


The game does not feature simulated betting. Felt a bit unethical when writing this game.

## Dependences

All imported modules are either locally defined or built in. No other dependences are needed.