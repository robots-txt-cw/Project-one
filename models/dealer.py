from player import Player
from ..utils.constants import CARD_BORDER, CARD_DEALER_FILLER, CARD_HEIGHT


class Dealer(Player):

    def __init__(self):
        super().__init__()

    def printHand(self) -> None:
        print(" DEALER")
        self.hand[1].print()
        print(CARD_BORDER)
        for _ in range(CARD_HEIGHT):
            print(CARD_DEALER_FILLER)
        print(CARD_BORDER)

    def revealHand(self) -> None:
        for i in self.hand:
            i.print()
        print(f"Currently {self.handValue}")

    def playTurn(self):
        while self.handValue < 17:
            pass
