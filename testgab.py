import random

# Define ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create deck
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle deck
random.shuffle(deck)

# Function to calculate hand value
def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Deal initial hands
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

print("Player's hand:", player_hand, "Value:", hand_value(player_hand))
print("Dealer's hand:", [dealer_hand[0], ('?', '?')], "Value:", hand_value([dealer_hand[0]]))

# Player's turn
while hand_value(player_hand) < 21:
    action = input("Hit or Stand? (h/s): ").lower()
    if action == 'h':
        player_hand.append(deck.pop())
        print("Player's hand:", player_hand, "Value:", hand_value(player_hand))
        if hand_value(player_hand) > 21:
            print("Bust! You lose.")
            exit()
    elif action == 's':
        break
    else:
        print("Invalid input.")

# Dealer's turn
while hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())

print("Dealer's hand:", dealer_hand, "Value:", hand_value(dealer_hand))

# Determine winner
player_val = hand_value(player_hand)
dealer_val = hand_value(dealer_hand)

if player_val > 21:
    print("You bust! Dealer wins.")
elif dealer_val > 21:
    print("Dealer busts! You win.")
elif player_val > dealer_val:
    print("You win!")
elif player_val < dealer_val:
    print("Dealer wins.")
else:
    print("Push!")