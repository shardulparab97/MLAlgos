import collections
import random

# https://medium.com/@tor_92315/machine-learning-and-card-games-6b210f8ec322

def shuffle(deck):
    random.shuffle(deck)
    return deck

def draw(deck):
    if len(deck) == 0:
        print("Deck is empty")
        return
    else:
        return deck.popleft()

# Function to deal cards to players
def deal_cards(num_players, num_cards, deck):
    players = [[] for _ in range(num_players)]
    for _ in range(num_cards):
        for i in range(num_players):
            players[i].append(deck.popleft())
    return players

# Function to get the value of a card
def card_value(card):
    return ranks.index(card[0])


# Function to compare hands and determine the winner
def compare_hands(hand1, hand2):
    hand1.sort(key=card_value, reverse=True)
    hand2.sort(key=card_value, reverse=True)

    for card1, card2 in zip(hand1, hand2):
        if card_value(card1) > card_value(card2):
            return "Player 1 wins!"
        elif card_value(card1) < card_value(card2):
            return "Player 2 wins!"

    return "It's a tie!"

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


