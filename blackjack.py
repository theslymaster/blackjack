import random
import sys

from deck import Deck
from hand import Hand

dealer_hand = Hand()
player_hand = Hand()
    
deck = Deck()

player_score = 0

def populate_hand(hand):
    for i in range(1):
        hand.add_card(deck.get_card())

def game():
    populate_hand(dealer_hand)
    populate_hand(player_hand)

    dealer_hand.print_hand()
    dealer_hand.hand_count()

    player_hand.print_hand()
    player_hand.hand_count()

def menu():
    print("Select an option:")
    print("1. New Game")
    print("2. Exit")

    answer = input(">> ")

    if answer == "1":
        game()
    elif answer == "2":
        exit()
    else:
        return

def main():
    if "2." in sys.version:
        print("Please run the game using Python 3")
        return

    while True:
        menu()

main()