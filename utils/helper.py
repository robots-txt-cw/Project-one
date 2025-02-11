import sys
import os
from ..models import User, Dealer


def clearShell() -> None:
    windows = ["win32", "cygwin"]
    os.system("cls" if sys.platform in windows else "clear")


def canContinue() -> bool:
    """Little confusing. Reurns False if user wants to quit. Returns True if user is continuing."""
    userInput = str.lower(input("Press any key to continue or (Q)uit"))
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
    user.printHand()
