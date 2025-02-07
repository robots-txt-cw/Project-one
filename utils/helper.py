from models.user import User
from models.dealer import Dealer
import sys
import os

def handPrinter(user: User, dealer: Dealer) -> None:
    print(" DEALER")
    dealer.printHand()
    print()
    print(" CURRENT HAND")
    user.printHand()


def clearShell() -> None:
    windows = ['win32', 'cygwin']
    os.system("cls" if sys.platform in windows else "clear")

def printStart() -> None:
    print("")