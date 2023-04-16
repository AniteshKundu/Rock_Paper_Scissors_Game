import random
def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors) : ")
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)
    choises = {"player": player_choice , "computer": computer_choice}
    return choises
def check_win(player, computer ):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie !"
    elif player == "Rock":
        if computer == "Scissor":
            return "Rock smashes scissors ! You win !"
        else:
            return "Peper cover Rock ! You lose ."
    elif player == "Paper":
        if computer == "Rock":
            return "Paper cover Rock ! You win !"
        else:
            return "Scissors cuts Paper ! You lose ."
    elif player == "Scissor":
        if computer == "Paper":
            return "Scissors cuts Paper ! You win !"
        else:
            return "Rock smashes Scissors ! You lose ."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"]) 
print(result)