class Hand:
    hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_count(self):
        count = 0

        for card in self.hand:
            count = count + card[2]
       
        print("Count: " + str(count))

    def print_hand(self):
        for card in self.hand:
            print(card)