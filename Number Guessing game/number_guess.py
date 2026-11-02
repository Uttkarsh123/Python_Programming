import random
num = random.randint(1,100)

guess_count=0
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++ NUMBER GUESSING GAME+++++++++++++")
print("+++++++ Guess the number in 7 attempts ++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++")
while True:
    user_guess = int(input("Enter a number between 1 and 100:"))
    guess_count+=1
    if user_guess > num:
        print("Too High")
    elif user_guess < num:
        print("Too Low")
    else:
        print(f"Congratulations! You guessed it right in {guess_count} attempts")
        break

    if guess_count == 7:
        print(f"Game Over! Correct number was {num}")
        break

