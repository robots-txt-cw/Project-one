import random
from card import Card
from typing import *


class Deck:

    def __init__(self):
        self.deckList: List[Card] = Deck._create()
        self.cardsInUse: List[Card]

    @staticmethod
    def _create() -> List[Card]:
        createdDeck: List[Card] = []

        faces = ["k", "q", "j", "a"]
        suites = ["heart", "diamond", "spade", "club"]

        for suite in suites:
            for i in range(2, 11):
                createdDeck.append(Card(i, suite))
            for face in faces:
                createdDeck.append(Card(face, suite))

        random.shuffle(createdDeck)
        return createdDeck

    def playCard(self) -> Card:
        '''Returns a popped card.'''
        random.shuffle(self.deckList)

        poppedCard = self.deckList.pop()
        self.cardsInUse = poppedCard
        return poppedCard

    def resetDeck(self) -> None:
        for i in self.cardsInUse:
            self.deckList.append(i)

        self.cardsInUse = []
