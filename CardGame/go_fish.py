import random

# Define ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['club', 'diamond', 'spade', 'heart']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)


# Function to check for books in a player's hand
def check_books(player):
    rank_counts = {}
    books = []

    # Count the occurrences of each rank
    for card in player:
        rank = card[0]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    # Check for books (sets of four cards of the same rank)
    for rank, count in rank_counts.items():
        if count == 4:
            books.append(rank)

    return books


# Function for one player to ask another for cards of a certain rank
def ask_for_cards(player_index, target_player_index, target_rank, players_hands):
    # Check if the target rank is present in the target player's hand
    target_player_hand = players_hands[target_player_index]
    cards_given = [card for card in target_player_hand if card[0] == target_rank]

    if len(cards_given) > 0:
        print(f"Player {target_player_index + 1} gives player {player_index + 1} {len(cards_given)} {target_rank}s")
        players_hands[player_index].extend(cards_given)
        players_hands[target_player_index] = [card for card in target_player_hand if card[0] != target_rank]
        return True
    else:
        print(f"Player {target_player_index + 1} says: Go Fish!")
        return False

# Function for Go Fish: Player draws a card from the deck
def go_fish(player_index, players_hands):
    if len(deck) > 0:
        drawn_card = deck.pop()
        players_hands[player_index].append(drawn_card)
        print(f"Player {player_index + 1} draws a card from the deck.")
        return drawn_card[0]
    else:
        print("Deck is empty!")


# Function to ask another player for cards and check for books
def ask_and_check_books(player_index, target_player_index, players_hands):
    target_rank = input(f"Player {player_index + 1}, choose a rank to ask player {target_player_index + 1} for: ")

    if target_rank not in ranks:
        print("Invalid rank!")
        return

    if ask_for_cards(player_index, target_player_index, target_rank, players_hands):
        books = check_books(players_hands[player_index])
        if books:
            print(f"Player {player_index + 1} got a book of {books[-1]}s!")
            print("Books:", books)
    else:
        go_fish(player_index, players_hands)


# Function to deal cards to players
def deal_cards(num_players, num_cards):
    players = [[] for _ in range(num_players)]
    for _ in range(num_cards):
        for i in range(num_players):
            players[i].append(deck.pop())
    return players


# Function to check for books in a player's hand
def check_books(player):
    books = []
    for rank in ranks:
        count = sum(1 for card in player if card[0] == rank)
        if count == 4:
            books.append(rank)
    return books

# better way out
def check_books(player):
    rank_counts = {}
    books = []

    # Count the occurrences of each rank
    for card in player:
        rank = card[0]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    # Check for books (sets of four cards of the same rank)
    for rank, count in rank_counts.items():
        if count == 4:
            books.append(rank)

    return books



# Function to play a round of Go Fish
# def go_fish(players, player_index, target_rank):
    # if target_rank not in ranks:
    #     print("Invalid rank!")
    #     return False
    #
    # target_cards = [card for card in players[player_index] if card[0] == target_rank]
    # if len(target_cards) == 0:
    #     print("Go Fish! You draw a card from the deck.")
    #     drawn_card = deck.pop()
    #     players[player_index].append(drawn_card)
    #     if drawn_card[0] == target_rank:
    #         print("You got what you asked for!")
    #         return True
    #     else:
    #         return False
    # else:
    #     players[player_index].extend(target_cards)
    #     players[player_index] = [card for card in players[player_index] if card[0] != target_rank]
    #     print("You got what you asked for!")
    #     return True


# Main function to play Go Fish
def play_go_fish(num_players):
    players_hands = deal_cards(num_players, 5)
    books = [[] for _ in range(num_players)]

    current_player = 0
    while True:
        print(f"\nPlayer {current_player + 1}'s turn")
        print("Your hand:", players_hands[current_player])

        target_rank = input("Choose a rank to ask for: ")
        if not go_fish(players_hands, current_player, target_rank):
            print("Go Fish! It's the next player's turn.")
            current_player = (current_player + 1) % num_players
        else:
            books[current_player].extend(check_books(players_hands[current_player]))
            print("Books:", books[current_player])

        if not deck:
            print("No more cards in the deck. Game over!")
            break
        if all(len(hand) == 0 for hand in players_hands):
            print("All players are out of cards. Game over!")
            break


# Function to play a round of Go Fish
# def go_fish(players, player_index, target_rank):
#     if target_rank not in ranks:
#         print("Invalid rank!")
#         return False
#
#     target_cards = [card for card in players[player_index] if card[0] == target_rank]
#     if len(target_cards) == 0:
#         print("Go Fish! You draw a card from the deck.")
#         drawn_card = deck.pop()
#         players[player_index].append(drawn_card)
#         if drawn_card[0] == target_rank:
#             print("You got what you asked for!")
#             return True
#         else:
#             return False
#     else:
#         players[player_index].extend(target_cards)
#         players[player_index] = [card for card in players[player_index] if card[0] != target_rank]
#         print("You got what you asked for!")
#         return True
#
# # Play the game with 2 players
def test_go_fish_game():
    # Set a seed for reproducibility
    random.seed(42)

    # Deal cards to players
    players_hands = deal_cards(3, 5)

    # Display players' hands
    print("Initial hands:")
    print("Player 1's hand:", players_hands[0])
    print("Player 2's hand:", players_hands[1])

    # Player 1 asks Player 2 for cards and checks for books
    print("\nPlayer 1's turn:")
    ask_and_check_books(0, 1, players_hands)

    # Player 2 asks Player 1 for cards and checks for books
    print("\nPlayer 2's turn:")
    ask_and_check_books(1, 0, players_hands)

    # Player 1 goes fishing if needed
    # print("\nPlayer 1's turn:")
    # if len(deck) > 0:
    #     go_fish(0, players_hands)
    # else:
    #     print("Deck is empty!")
    #
    # # Player 2 goes fishing if needed
    # print("\nPlayer 2's turn:")
    # if len(deck) > 0:
    #     go_fish(1, players_hands)
    # else:
    #     print("Deck is empty!")

    # Display final hands and books
    print("\nFinal hands:")
    print("Player 1's hand:", players_hands[0])
    print("Player 2's hand:", players_hands[1])
    print("Player 1's books:", check_books(players_hands[0]))
    print("Player 2's books:", check_books(players_hands[1]))


# Run the test case
test_go_fish_game()

