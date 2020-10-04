import random

class Deck:

    DEFAULT_DECK = [
        ('A', 'Hearts', (1, 11)), ('2', 'Hearts', 2), ('3', 'Hearts', 3), ('4', 'Hearts', 4), ('5', 'Hearts', 5), ('6', 'Hearts', 6), ('7', 'Hearts', 7),
        ('8', 'Hearts', 8), ('9', 'Hearts', 9), ('10', 'Hearts', 10), ('J', 'Hearts', 10), ('Q', 'Hearts', 10), ('K', 'Hearts', 10),
        ('A', 'Diamonds', (1, 11)), ('2', 'Diamonds', 2),  ('3', 'Diamonds', 3), ('4', 'Diamonds', 4), ('5', 'Diamonds', 5), ('6', 'Diamonds', 6), 
        ('7', 'Diamonds', 7), ('8', 'Diamonds', 8), ('9', 'Diamonds', 9), ('10', 'Diamonds', 10), ('J', 'Diamonds', 10), ('Q', 'Diamonds', 10),
        ('K', 'Diamonds', 10), ('A', 'Spades', (1, 11)),('2', 'Spades', 2),  ('3', 'Spades', 3), ('4', 'Spades', 4), ('5', 'Spades', 5), ('6', 'Spades', 6), 
        ('7', 'Spades', 7), ('8', 'Spades',8 ), ('9', 'Spades', 9), ('10', 'Spades', 10), ('J', 'Spades', 10), ('Q', 'Spades', 10), ('K', 'Diamonds', 10), 
        ('A', 'Clubs', (1, 11)), ('2', 'Clubs', 2), ('3', 'Clubs', 3), ('4', 'Clubs', 4), ('5', 'Clubs', 5), ('6', 'Clubs', 6), ('7', 'Clubs', 7),
        ('8', 'Clubs', 8), ('9', 'Clubs', 9), ('10', 'Clubs', 10), ('J', 'Clubs', 10), ('Q', 'Clubs', 10), ('K', 'Clubs', 10)
    ]

    shuffled_deck = []

    def __init__(self):
        self.shuffle()

    def print_deck(self):
        for card in self.shuffled_deck:
            print(card)

    def shuffle(self):
        for card in self.DEFAULT_DECK:
            self.shuffled_deck.append(card)

        for i in range(3):
            random.shuffle(self.shuffled_deck)

    def get_card(self):
        if len(self.shuffled_deck) == 0:
            self.shuffle()

        self.print_deck()

        print("====================")

        card = random.choice(self.shuffled_deck)
        self.shuffled_deck.remove(card)

        print("Adding card: " + str(card))

        self.print_deck()

        print("====================")

        return card