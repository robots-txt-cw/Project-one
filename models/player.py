from card import Card

class Player:
    def __init__(self):
        self.hand: list[Card]
        self.handValue = 0
    
    def _updateHandValue(self) -> None:
        '''Mainly the logic for face cards. Updates Player.handValue'''
        self.handValue = 0
        for card in self.hand:
            if type(card.cardValue) == int:
                self.handValue += card.cardValue
            elif card.cardValue == 'k' or 'q' or 'j':
                self.handValue += 10
            elif card.cardValue == 'a':
                self.handValue += 11 if self.handValue + 11 <= 21 else 1

    def populateHand(self, drawnCard: list[Card] | Card) -> None:
        '''Populates the player's hand with a card or set of cards. Updates both Player.hand and Player.handValue
        
        Args:
            drawnCard List[Card]: an array of cards given out during the start of the round.
            drawnCard Card: card drawn after hitting
        '''
        if type(drawnCard) is list:
            self.hand = drawnCard
        else:
            self.hand.append(drawnCard)

        self._updateHandValue()

    
    def isBust(self) -> bool:
        '''Checks if player busts or not.
            Returns:
                True: Player's hand value is > 21
                False: Player's hand value is <= 21'''
        if self.handValue > 21:
            return True
        return False

