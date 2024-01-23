
#Basic Baccarat Gamesource venv/bin/activate

import random

def create_deck():
    # A list of all possible card ranks: 2 to 10, Jack, Queen, King, Ace
    ranks = [str(n) for n in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']

    # A list of all possible card suits: Hearts, Diamonds, Clubs, Spades
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # Create a deck of cards. Each card is a tuple with a rank and a suit.
    deck = [(rank, suit) for rank in ranks for suit in suits]

    return deck


def shuffle_deck(deck):
    # Randomly rearrange the elements in the deck
    random.shuffle(deck)

def deal_cards(deck, num_cards):
    # Deal the specified number of cards from the top of the deck
    dealt_cards = deck[:num_cards]

    # Remove the dealt cards from the deck
    deck = deck[num_cards:]

    return dealt_cards, deck

def place_bet(player_money):
    # Ask the player how much they want to bet
    bet_amount = float(input("How much would you like to bet? "))

    # Make sure the player has enough money to place the bet
    while bet_amount > player_money:
        print("You don't have enough money to place that bet.")
        bet_amount = float(input("How much would you like to bet? "))

    # Ask the player who they want to bet on
    bet_on = input("Who would you like to bet on (Player, Banker, or Tie)? ")

    return bet_amount, bet_on

def calculate_hand_value(hand):
    # Initialize the hand value to 0
    hand_value = 0

    # Define the card values
    card_values = {str(n): n for n in range(2, 11)}
    card_values['Ace'] = 1
    card_values['Jack'] = card_values['Queen'] = card_values['King'] = 0

    # Add up the values of the cards in the hand
    for card in hand:
        hand_value += card_values[card[0]]

    # The value of a hand is the last digit of the sum of the card values
    hand_value %= 10

    return hand_value

def evaluate_winner(player_hand, banker_hand):
    # Calculate the values of the hands
    player_value = calculate_hand_value(player_hand)
    banker_value = calculate_hand_value(banker_hand)

    # Determine the winner
    if player_value > banker_value:
        return 'Player'
    elif player_value < banker_value:
        return 'Banker'
    else:
        return 'Tie'



def play_baccarat(player_money):
    # Create and shuffle a deck of cards
    deck = create_deck()
    shuffle_deck(deck)

    # Deal two cards each to the player and the banker
    player_hand, deck = deal_cards(deck, 2)
    banker_hand, deck = deal_cards(deck, 2)

    # Evaluate the winner
    winner = evaluate_winner(player_hand, banker_hand)

    # Place a bet
    bet_amount, bet_on = place_bet(player_money)

    # Update the player's money based on the result of the game
    if winner == bet_on:
        if winner == 'Tie':
            # If it's a tie and the player bet on a tie, they get eight times their bet amount
            player_money += bet_amount * 8
        else:
            # If the player wins their bet, they get twice their bet amount
            player_money += bet_amount
    else:
        # If the player loses their bet, they lose their bet amount
        player_money -= bet_amount

    return player_money

def main():
    # The player starts with $100
    player_money = 100.0

    # Play a game of Baccarat
    player_money = play_baccarat(player_money)

if __name__ == "__main__":
    main()