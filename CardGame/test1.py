import collections
import random
def shuffle(deck):
    random.shuffle(deck)
    return deck

def draw(deck):
    if len(deck) == 0:
        print("Deck is empty")
        return
    else:
        return deck.popleft()

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['clubs', 'hearts', 'spades', 'diamonds']

deck = [(rank, suit) for rank in ranks for suit in suits]
deck = collections.deque(deck)
print(deck)

deck = shuffle(deck)
print(deck)

drawn_card = draw(deck)
print(drawn_card)
print(len(deck))


