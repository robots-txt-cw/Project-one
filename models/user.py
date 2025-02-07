from player import Player
from card import Card




class User(Player):

    def __init__(self):
        super().__init__()
        self.splitHand: list[Card] | None = None

    def printHand(self) -> None:
        for i in self.hand:
            i.print()
        print(f"Currently {self.handValue}")

    def _getPlayOptions(self, hand: list[Card], turns: int) -> list[str]:
        '''Private method.
        Returns the options the player has available to them from a given amount of previous turns.
        Args:
            turns: The amount of previous turns the player has played. Used to determine if "Double Down" and "Split" is available.
        Return:
            List of available options
        '''
        options = ['s', 'h']
        # Double Down
        if turns == 0:
            options.append('d')
        # Split

        def checksplit() -> bool:
            available = True
            if turns > 0 and self.hand:
                available = False
            if hand[0].cardValue != hand[1].cardValue:
                available = False

            return available

        if checksplit():
            options.append('s')
        return options

    def playTurn(self):
        pass
