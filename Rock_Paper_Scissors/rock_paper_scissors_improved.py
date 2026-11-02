
import random

player_wins = 0
computer_wins = 0
ties = 0

def get_choices():
    all_choices = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
        if player_choice in all_choices:
            computer_choice = random.choice(all_choices)
            return player_choice, computer_choice
        print("Invalid choice! Please try again.")

def check_win(player, computer, player_wins, computer_wins, ties):
    if player == computer:
        print("It's a Tie!")
        ties += 1
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("Player Wins!")
        player_wins += 1
    else:
        print("Computer Wins!")
        computer_wins += 1
    return player_wins, computer_wins, ties

def show_score(player_wins, computer_wins, ties):
    print("\n========== SCOREBOARD ==========")
    print(f"Player Wins: {player_wins}")
    print(f"Computer Wins: {computer_wins}")
    print(f"Ties: {ties}")
    print("================================")

def play_again():
    while True:
        choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'
        print("Invalid input! Enter Y or N.")

while True:
    player, computer = get_choices()
    print(f"\nComputer Chose: {computer}")
    print(f"Player Chose: {player}")
    player_wins, computer_wins, ties = check_win(player, computer, player_wins, computer_wins, ties)
    show_score(player_wins, computer_wins, ties)
    if not play_again():
        break

print("\n========== FINAL RESULT ==========")
if player_wins > computer_wins:
    print("Congratulations! You are the overall winner!")
elif computer_wins > player_wins:
    print("Computer is the overall winner!")
else:
    print("The game ended in an overall tie!")

show_score(player_wins, computer_wins, ties)
print("\nThanks for playing!")
