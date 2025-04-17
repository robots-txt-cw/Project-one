#!/usr/bin/python3
import helper
import models


def main():

    helper.printStart()
    dealer = models.Dealer()
    deck = models.Deck()
    user = models.User()

    while helper.canContinue():

        helper.clearShell()
        dealer.reset()
        user.reset()
        deck.resetDeck()

        for _ in range(2):
            dealer.populateHand(deck.popCard())
            user.populateHand(deck.popCard())

        isUserTurn = True
        while isUserTurn:
            helper.clearShell()
            helper.printHands(dealer, user)
            userChoice = user.getUserChoice()
            match userChoice:
                case "s":
                    isUserTurn = False
                case "h":
                    user.populateHand(deck.popCard())
                case "d":
                    user.populateHand(deck.popCard())
                    isUserTurn = False
            if user.isBust():
                isUserTurn = False

        while dealer.handValue < 17:
            dealer.populateHand(deck.popCard())
            if dealer.isBust():
                break

        userWon = helper.isUserWon(dealer, user)
        helper.clearShell()
        helper.revealHands(dealer, user)

        match userWon:
            case True:
                print(f"{models.Colors.GREEN}You Won{models.Colors.END}")
            case False:
                print(f"{models.Colors.RED}You Lost{models.Colors.END}")
            case None:
                print("You Pushed")


if __name__ == "__main__":
    main()
