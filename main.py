#!/usr/bin/python3
from utils import helper
import models


def main():

    helper.printStart()
    dealer = models.Dealer()
    deck = models.Deck()
    user = models.User()

    while helper.canContinue():

        helper.clearShell()

        for _ in range(2):
            dealer.populateHand(deck.popCard())
            user.populateHand(deck.popCard())

        helper.printHands()


if __name__ == "__main__":
    main()
