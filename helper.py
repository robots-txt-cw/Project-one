import sys
import os
from models import User, Dealer


def clearShell() -> None:
    windows = ["win32", "cygwin"]
    os.system("cls" if sys.platform in windows else "clear")


def canContinue() -> bool:
    """Little confusing. Reurns False if user wants to quit. Returns True if user is continuing."""
    userInput = str.lower(input("Press Enter key to continue or (Q)uit: "))
    return False if (userInput == "q" or userInput == "quit") else True


def printStart() -> None:
    print(
        """                                                                                                                        
@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@@@   @@@  @@@  @@@   @@@@@@   @@@               @@@   @@@@@@    @@@@@@@  @@@  @@@  
@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@               @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
  @@!    @@!       @@!  @@@  @@! @@! @@!  @@!  @@!@!@@@  @@!  @@@  @@!               @@!  @@!  @@@  !@@       @@!  !@@  
  !@!    !@!       !@!  @!@  !@! !@! !@!  !@!  !@!!@!@!  !@!  @!@  !@!               !@!  !@!  @!@  !@!       !@!  @!!  
  @!!    @!!!:!    @!@!!@!   @!! !!@ @!@  !!@  @!@ !!@!  @!@!@!@!  @!!               !!@  @!@!@!@!  !@!       @!@@!@!   
  !!!    !!!!!:    !!@!@!    !@!   ! !@!  !!!  !@!  !!!  !!!@!!!!  !!!               !!!  !!!@!!!!  !!!       !!@!!!    
  !!:    !!:       !!: :!!   !!:     !!:  !!:  !!:  !!!  !!:  !!!  !!:               !!:  !!:  !!!  :!!       !!: :!!   
  :!:    :!:       :!:  !:!  :!:     :!:  :!:  :!:  !:!  :!:  !:!   :!:         !!:  :!:  :!:  !:!  :!:       :!:  !:!  
   ::     :: ::::  ::   :::  :::     ::    ::   ::   ::  ::   :::   :: ::::     ::: : ::  ::   :::   ::: :::   ::  :::  
   :     : :: ::    :   : :   :      :    :    ::    :    :   : :  : :: : :      : :::     :   : :   :: :: :   :   :::  
                                                                                                                        """
    )


def printHands(dealer: Dealer, user: User) -> None:
    dealer.printHand()
    print("")
    print("")
    user.printHand()


def isUserWon(dealer: Dealer, user: User) -> bool | None:

    if user.isBust():
        return False
    if user.handValue < dealer.handValue and not dealer.isBust():
        return False
    if user.handValue == dealer.handValue:
        return None

    return True


def revealHands(dealer: Dealer, user: User) -> None:
    dealer.revealHand()
    print("")
    print("")
    user.printHand()
