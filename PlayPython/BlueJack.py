import random
from typing import List
from icecream import ic 
dealer_cards = []
player_cards = []

class Noun: 
    def verb1(self, param1):
        self.adjectives = "Funny"
        self.adverb =  "Fast"
        pass

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self._points = 0
        if value.isnumeric():
            value_as_int = int(value)
            is_valid_value = value_as_int >= 2 and value_as_int <= 10
            if is_valid_value:
                self._points = value_as_int
            else:
                raise Exception("Error")
        else:
            # 
            is_face_card = value  == "K" or value == "Q" or value == "J" or value == "A"
            if is_face_card:
                self._points = 10 
            else:
                raise Exception ("Not valid value")


    def __str__(self):
        return f"[{self.value}:{self.suite}]"
    
    def __repr__(self):
        return self.__str__()

    def points(self):
        return self._points

def GetRandomCard():
    values = ['A','Q','K','J']
    for i in list(range(2,11)):
        values += [f'{i}']
  
    value = random.choice(values)
    suites = ['Heart','Diamond','Club','Spade']
    suite = random.choice(suites)
    return Card(suite,value)

def points(cards:List[Card]):
    sum = 0
    for card in cards:
        sum += card.points()
    return sum

def is_gameover(dealer_cards, player_cards):
    dealer_sum = points(dealer_cards) # dealer_cards[0] + dealer_cards[1]
    player_sum = points(player_cards) # player_cards[1] + player_cards[0]
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
        dealer_cards.append(GetRandomCard())
    print(dealer_cards)
    while len(player_cards) != 2:
        player_cards.append(GetRandomCard())

    while (True):
        is_game_over_t = is_gameover(dealer_cards, player_cards)
        if (is_game_over_t):
            return

        print(f"Your cards are {hand_to_string(player_cards)}." )

        dealer_sum = points(dealer_cards) # dealer_cards[0] + dealer_cards[1]
        player_sum = points(player_cards) # player_cards[1] + player_cards[0]
        
        UserAction1 = input (f"Your cards add up to {player_sum}, press H to hit, anything else to hold")
        if UserAction1.lower() == "h":
            player_cards.append(GetRandomCard())
        xx = is_gameover(dealer_cards,player_cards)
        if xx == True:
            return
        # Need to recheck if game over because getting the card might put us over

        # Do dealer actions
        if dealer_sum < 15:
            dealer_cards.append(GetRandomCard())
        
        else:
            dealer_sum = points(dealer_cards) # dealer_cards[0] + dealer_cards[1]
            player_sum = points(player_cards) # player_cards[1] + player_cards[0]
            ic(player_cards)
            ic(dealer_cards)
            ic(dealer_sum, player_sum)
            if dealer_sum > player_sum:
                print("You won! :D")
                return
            else:
                print("Dealer wins :(")
                return




c1 = GetRandomCard()
c2 = GetRandomCard()



# def trash():
#    print(GetRandomCard())
# for _ in range(10):
#    trash()

play_game()
