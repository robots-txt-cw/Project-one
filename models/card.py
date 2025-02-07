from ..utils.constants import CARD_BORDER, CARD_FILLER, CARD_HEIGHT

class Card:

    def __init__(self, value: int | str, suite: str):
        self.cardValue = value
        self.cardSuite = suite

    def print(self):
        suiteIcons = {
            "heart": "\u2665",
            "diamond": "\u2666",
            "spade": "\u2660",
            "club": "\u2663"
        }
        faceIcons = {
            "k": "\u2654",
            "q": "\u2655",
            "j":"JACK",
            "a": "ACE"
        }

        print(CARD_BORDER)
        print(f"|  {suiteIcons[self.cardSuite]}  {self.cardValue if type(self.cardValue) == int else faceIcons[self.cardValue]}")
        for _ in range(CARD_HEIGHT):
            print(CARD_FILLER)
        print(CARD_BORDER)
