import random

# Define a Card class to represent each individual card
class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define a Deck class to manage the deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]  # Remove dealt cards from the deck
        return dealt_cards

    def shuffle(self):
        random.shuffle(self.cards)

# Function to display the current hand of cards
def display_hand(hand):
    return ', '.join(str(card) for card in hand)

# Main game logic
def poker_game():
    # Step 1: Initialize the deck and deal the hand
    deck = Deck()
    hand = deck.deal(5)
    print("Your initial hand:")
    print(display_hand(hand))

    # Step 2: Prompt the user to select cards to replace
    replacements = input("\nEnter the card positions (1-5) to replace (e.g., 1, 3, 5): ")
    replacement_indices = [int(x) - 1 for x in replacements.split(',')]  # Convert to 0-based index

    # Step 3: Replace the selected cards with new cards
    for index in replacement_indices:
        if 0 <= index < 5:  # Ensure valid index
            hand[index] = deck.deal(1)[0]

    # Step 4: Show the final hand after the draw
    print("\nYour final hand after the draw:")
    print(display_hand(hand))

if __name__ == "__main__":
    poker_game()
