# Emily Adams
# Number Guesser Blackbelt
# Started September 9, 2025, Due September 12, 2025
# This project generates a random number for the user to guess.

import random
secret = random.randint(1,1000)
tries = 0
keepGoing = True
while keepGoing:
    tries += 1
    userGuess = input("What is your guess? ")
    correct = userGuess.isnumeric()
    if correct:
        userGuessInt = int(userGuess)
        if userGuessInt > secret:
            print("Too high")
        elif userGuessInt < secret:
            print("Too low")
        else:
            print(f"You got it in {tries} turns!")
            print("You win!")
            keepGoing = False
    else:
        if tries >= 14:
            print("You should be able to solve this in 14 tries or less.")
            print(f"You lose! The number was {secret}.")
            keepGoing = False
    if correct == False:
        print("That's not a number...")

# Binary search algorithm: check the value in the center of the array. If target is higher, search right half; if target is lower, search left half.
# Continue this for the new reduced half of the array until target value is found.
# The number of tries has been doubled to account for the larger dataset, although I find that I guess it after an average of 10 tries.
