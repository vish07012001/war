from War.war.Card import Card
import random


class Deck:
    # Deck class consisting of init method to create a deck of 52 cards
    def __init__(self):
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
        self.shuffle()

    # Shuffle method to shuffle cards
    def shuffle(self):
        random.shuffle(self.all_cards)

    # used to pop one card from deck of cards
    def deal_one(self):
        return self.all_cards.pop()
