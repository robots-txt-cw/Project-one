from models.user import User
from models.dealer import Dealer
import sys
import os

def handPrinter(user: User, dealer: Dealer):
    print(" DEALER")
    dealer.printHand()
    print()
    print(" CURRENT HAND")
    user.printHand()


def clearShell():
    windows = ['win32', 'cygwin']
    os.system("cls" if sys.platform in windows else "clear")

def printStart():
    print("")