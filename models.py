from constants import CARD_BORDER, CARD_HEIGHT, CARD_FILLER, CARD_DEALER_FILLER
import random


class Card:

    def __init__(self, value: int | str, suite: str):
        self.cardValue = value
        self.cardSuite = suite

    def print(self) -> None:
        suiteIcons = {
            "heart": "\u2665",
            "diamond": "\u2666",
            "spade": "\u2660",
            "club": "\u2663",
        }
        faceIcons = {"k": "\u2654", "q": "\u2655", "j": "JACK", "a": "ACE"}

        print(CARD_BORDER)
        print(
            f"| {suiteIcons[self.cardSuite]}  {self.cardValue if type(self.cardValue) == int else faceIcons[self.cardValue]}"
        )
        for _ in range(CARD_HEIGHT):
            print(CARD_FILLER)
        print(CARD_BORDER)


class Deck:

    def __init__(self):
        self.deckList: list[Card] = Deck._create()
        self.cardsInUse: list[Card] = []

    @staticmethod
    def _create() -> list[Card]:
        createdDeck: list[Card] = []

        faces = ["k", "q", "j", "a"]
        suites = ["heart", "diamond", "spade", "club"]

        # Add 4 decks
        for _ in range(4):
            for suite in suites:
                for i in range(2, 11):
                    createdDeck.append(Card(i, suite))
                for face in faces:
                    createdDeck.append(Card(face, suite))

        random.shuffle(createdDeck)
        return createdDeck

    def popCard(self) -> Card:
        """Returns a popped card from the deck. Main function to deal out cards."""
        random.shuffle(self.deckList)

        poppedCard = self.deckList.pop()
        self.cardsInUse.append(poppedCard)
        return poppedCard

    def resetDeck(self) -> None:
        for i in self.cardsInUse:
            self.deckList.append(i)

        self.cardsInUse = []


class Player:
    def __init__(self):
        self.hand: list[Card] = []
        self.handValue = 0

    def _updateHandValue(self) -> None:
        """Mainly the logic for face cards. Updates Player.handValue"""
        self.handValue = 0
        for card in self.hand:
            if type(card.cardValue) == int:
                self.handValue += card.cardValue
            elif card.cardValue == "k" or "q" or "j":
                self.handValue += 10
            elif card.cardValue == "a":
                self.handValue += 11 if self.handValue + 11 <= 21 else 1

    def populateHand(self, drawnCard: list[Card] | Card) -> None:
        """Populates the player's hand with a card or set of cards. Updates both Player.hand and Player.handValue

        Args:
            drawnCard List[Card]: an array of cards given out during the start of the round.
            drawnCard Card: card drawn after hitting
        """
        if type(drawnCard) is list:
            self.hand = drawnCard
        else:
            self.hand.append(drawnCard)

        self._updateHandValue()

    def isBust(self) -> bool:
        """Checks if player busts or not.
        Returns:
            True: Player's hand value is > 21
            False: Player's hand value is <= 21"""
        if self.handValue > 21:
            return True
        return False

    def reset(self) -> None:
        self.hand = []
        self.handValue = 0


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
        print(" DEALER")

        for i in self.hand:
            i.print()
        print(f"Currently {self.handValue}")


class User(Player):

    optionsDict = {"s": "(S)tand", "h": "(H)it", "d": "(D)ouble Down"}

    def __init__(self):
        super().__init__()
        self.turns: int = 0

    def printHand(self) -> None:

        print(" CURRENT HAND")
        for i in self.hand:
            i.print()
        print(f"Currently {self.handValue}")

    def _getPlayOptions(self) -> list[str]:
        """Private method.
        Returns the options the player has available to them from a given amount of previous turns.
        Return:
            List of available options
        Notes:
            inefficient. Each turn requires this method to be called, resulting in multiple logic statements.
            - Could possibly store the values in array, only adding
        """
        options = ["s", "h"]
        # Double Down
        if self.turns == 0:
            options.append("d")

        return options

    def reset(self) -> None:
        super().reset()
        self.turns = 0

    def getUserChoice(self) -> str:
        """Returns the option user wants to do for their turn"""
        options: list[str] = []

        for i in self._getPlayOptions():
            if User.optionsDict[i]:
                options.append(User.optionsDict[i])

        desiredChoice = str.lower(input(f"{', '.join(options)}: "))

        while desiredChoice not in User.optionsDict.keys():
            print("Incorect input. (ex. Stand = 's' or 'S'): ")
            desiredChoice = str.lower(input(f"{', '.join(options)}: "))

        return desiredChoice
