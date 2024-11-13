import random
# Creating a random number
answer = random.randint(1, 100)
while True:
    if userScore == 0:
        print("Game Over")
    guess = input("Take a guess! or enter q to exit:\n")
    if guess.lower() == 'q':
        print("Goodbye!")
        break
    else:
        guess = int(guess)
    userScore = 100
    if guess == answer:
        print(f"You won, You've scored {userScore} out of 100!")
    elif guess < answer:
        print("Higher!")
        userScore -= 5
    else:
        print("Lower!")
        userScore -= 5