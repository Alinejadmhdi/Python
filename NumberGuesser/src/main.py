import random

def validate_guess(guess):
    if not guess.isdigit():
        print("Please enter a valid number!")
    if guess.lower() == 'q':
        print("Goodbye!")
        return
    else:
        guess = int(guess)
        return guess

def start_game():
# Creating a random number
    answer = random.randint(1, 100)
    userScore = 100

    while True:
        guess = input("Take a guess between 1 and 100! or enter q to exit:\n")
        guess = validate_guess(guess)
        if not guess:
            continue

        if userScore == 0:
            print("Game Over")
            break
        if guess == answer:
            print(f"You won, You've scored {userScore} out of 100!")
            break
        elif guess < answer:
            print("Higher!")
            userScore -= 5
        else:
            print("Lower!")
            userScore -= 5

start_game()

