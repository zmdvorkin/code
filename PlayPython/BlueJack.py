import random
from icecream import ic 
dealer_cards = []
player_cards = []
def is_gameover(dealer_cards, player_cards):
    dealer_sum = sum(dealer_cards) # dealer_cards[0] + dealer_cards[1]
    player_sum = sum(player_cards) # player_cards[1] + player_cards[0]
    ic(player_cards)
    ic(dealer_cards)
    ic(dealer_sum, player_sum)
    if dealer_sum > 21:
        print("The dealer has busted!")
        return True
    if dealer_sum == 21:
        print("Dealer gets bluejack! You lose :(")
        return True
    if player_sum == 21:
        print("You got BlueJack! Thats tubular :)")
        return True
    if player_sum > 21: 
        print("You busted :(")
        return True
    return False

def hand_to_string(cards):

    str = ""
    for card in cards:
        str += f"{card}, "
    return str

def play_game():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1,11))
    print(dealer_cards)
    while len(player_cards) != 2:
        player_cards.append(random.randint(1,11))

    while (True):
        is_game_over_t = is_gameover(dealer_cards, player_cards)
        if (is_game_over_t):
            return

        print(f"Your cards are {hand_to_string(player_cards)}." )

        dealer_sum = sum(dealer_cards) # dealer_cards[0] + dealer_cards[1]
        player_sum = sum(player_cards) # player_cards[1] + player_cards[0]
        
        UserAction1 = input (f"Your cards add up to {player_sum}, press H to hit, anything else to hold")
        if UserAction1.lower() == "h":
            player_cards.append(random.randint(1,11))
        xx = is_gameover(dealer_cards,player_cards)
        if xx == True:
            return
        # Need to recheck if game over because getting the card might put us over

        # Do dealer actions
        if dealer_sum < 15:
            dealer_cards.append(random.randint(1,11))
        
        else:
            dealer_sum = sum(dealer_cards) # dealer_cards[0] + dealer_cards[1]
            player_sum = sum(player_cards) # player_cards[1] + player_cards[0]
            ic(player_cards)
            ic(dealer_cards)
            ic(dealer_sum, player_sum)
            if dealer_sum > player_sum:
                print("You won! :D")
                return
            else:
                print("Dealer wins :(")
                return
play_game()