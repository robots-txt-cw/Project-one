from player import Player


class User(Player):

    def printHand(self):
        for i in self.hand:
            i.print()
        print(f"Currently {self.handValue}")

    def _getPlayOptions(self, turns: int) -> list[str]:
        '''Private method.
        Returns the options the player has available to them from a given amount of previous turns.
        Args:
            turns: The amount of previous turns the player has played. Used to determine if "Double Down" and "Split" is available.
        '''
        options = ['s', 'h']
        # Double Down
        if turns == 0:
            options.append('d')
        # Split
        if turns == 0 and self.hand[0].cardValue == self.hand[1].cardValue:
            options.append('s')
        return options

    def playTurn(self):
        pass
