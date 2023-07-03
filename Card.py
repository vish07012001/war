class Card:
    # Card class consisting of suits, ranks and values
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', 'King', 'Queen', 'Jack', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten']
    # Values will be used to compare cards of two players using int values
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
