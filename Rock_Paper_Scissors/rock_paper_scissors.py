import random

#Keeping score tracking
player_wins = 0
computer_wins = 0
tie = 0

def get_choices():
    all_choices = ['rock', 'paper','scissors']

    while True:
        player_choice = input("Enter your choice :-> Rock, paper or scissors ::").lower()
        if player_choice in all_choices:
                #Generating Computer choice
                computer_choice = random.choice(all_choices).lower()
                return {"player":player_choice,"Computer":computer_choice}
        else:
            print("Invalid choice Entered, Please Try again")

def check_win(player, computer):
    global player_wins, computer_wins, tie

    #Checking who will win
    if player == computer:
        print("It's a Tie")
        tie += 1

    elif player == "scissors":
        if computer == "rock":
            print("Computer Won")
            computer_wins +=1
        else :
            print("Player Won")
            player_wins +=1

    elif player == "rock":
            if computer == "paper":
                print("Computer Won")
                computer_wins +=1
            else :
                print("Player Won")
                player_wins +=1
                

    elif player == "paper":
        if computer == "scissors":
            print("Computer Won")
            computer_wins +=1
        else :
            print("Player Won")
            player_wins +=1
                    
    else:
        return "Invalid choice! Please choose rock, paper or scissors."

while True:
    choices = get_choices()
    print(f"Computer Chose :{choices['Computer']}, Player Chose: {choices['player']}")
    check_win(choices['player'],choices['Computer'])

    play_again=input("Do you want to play again ? Y / N :").upper()

    if play_again == "N":
        #Score card Printing
        print("Thank you for playing:")
        print("\n========== FINAL SCORE ==========")
        print(f"Player Wins: {player_wins}")
        print(f"Computer Wins: {computer_wins}")
        print(f"Ties: {tie}")
        print("=================================")
        break

