import random

# ComputeWin(player_choice, stephen_choice, "scissors", "paper", "rock")
def ComputeWin(what_the_player_chose, what_stephan_chose, to_evalute, win_condition, lose_condition):
    if what_the_player_chose == to_evalute  and what_stephan_chose == win_condition:
        return True

    if  what_the_player_chose == to_evalute and what_stephan_chose == lose_condition:
        return False

    return None

player_choice = "How should I know?"

# int means it's a whole 
stephen_choice_index = random.randint(0,2) # 0,1,2

choices = ["rock", "paper", "scissors"]

stephen_choice = choices[stephen_choice_index]

### What if the user didn't make a valid choice?

while True:
    # break
    player_choice = input (f"Rock, Paper Or Scissors?\n")
    player_choice = player_choice.lower()
    if  player_choice in choices:
        break
    
    print (f"{player_choice} is not valid! Try again")
    

print (f"The computer chose {stephen_choice}")


if player_choice == stephen_choice:
    print ("Ugh you broke the game. Try again, you tied.")

isWin = ComputeWin(player_choice, stephen_choice, "scissors", "paper", "rock")
if isWin == True: 
    print("You won!")
isWin = ComputeWin(player_choice, stephen_choice, "rock", "scissors", "paper")
isWin = ComputeWin(player_choice, stephen_choice, "paper", "rock", "scissors")