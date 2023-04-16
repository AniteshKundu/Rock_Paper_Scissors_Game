import random
def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors) : ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choises = {"player": player_choice , "computer": computer_choice}
    return choises
def check_win(player, computer ):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie !"
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes scissors ! You win !"
        else:
            return "Peper cover rock ! You lose ."
    elif player == "paper":
        if computer == "rock":
            return "Paper cover rock ! You win !"
        else:
            return "Scissors cuts paper ! You lose ."
    elif player == "scissor":
        if computer == "paper":
            return "Scissors cuts paper ! You win !"
        else:
            return "Rock smashes Scissors ! You lose ."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"]) 
print(result)