# Cards implemetation.

from random import randrange

RANK = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]


class draw_random_card:
    def random_rank(self):
        random_rank_index = randrange(0, len(RANK))
        random_rank = RANK[random_rank_index]
        return random_rank

    def random_suit(self):
        random_suit_index = randrange(0, len(SUIT))
        random_suit = SUIT[random_suit_index]
        return random_suit


class card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def set_rank(self):
        rank_instance = self.rank()
        rank_instance.random_rank()

    def set_suit(self):
        suit_instance = self.suit()
        suit_instance.random_suit()

    def set_name(self):
        card_rank = self.rank(self)
        card_suit = self.suit(self)
        self.name = card_rank + " of " + card_suit
        print("{}".format(self.name))


def main():
    draw_card = card(draw_random_card.random_rank, draw_random_card.random_suit)
    draw_card.set_name()

if __name__ == '__main__':
    main()
