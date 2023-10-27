
from Card import Card
from BlackJackGame import blackjack_game

# Start Game

if __name__ == '__main__':

    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # The suit value
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661",
                    "Clubs": "\u2667", "Diamonds": "\u2662"}

    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    # The deck of cards
    deck = []

    # Loop for every type of suit
    for suit in suits:

        # Loop for every type of card in a suit
        for card in cards:

            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    blackjack_game(deck)
