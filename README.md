# number-guesser
A Python program that randomly generates a number for the user to try and guess.
```
import random 
Create variable “secret”; “secret” gets random.randint(1,100) (random number to guess) 
Create variable “tries”; “tries” gets 0 (iterator) 
Create variable “keepGoing”; “keepGoing” gets True (initializing sentry) 
while keepGoing is True, (condition to stay in loop) 
    tries += 1 (positively iterates “tries”) 
    Create variable “userGuess”; “userGuess” gets input(“What is your guess?”) 
    Create variable “correct”; “correct” gets userGuess.isnumeric() (this python string 
    method checks to see if user input is numeric. If it is numeric, the variable gets “True”. If 
    it is not numeric, variable gets “False” and skips over comparison step straight to the next 
    guess. User has wasted a guess by not giving me a number. 
    if correct = True str is converted to int and compared to variable “secret”: 
        if userGuess > secret:  
            print(“Too high”) 
        elif userGuess < secret:  
            print(“Too low”) 
        else: 
            print(f”You got it in {tries} turns!”) 
            print(“You win! Good job!”) 
            keepGoing = False (changing sentry) 
    else: 
        if tries >= 7: 
            print(“You should be able to solve this in 7 tries or less.”) 
            print(f“You lose! The number was {secret}.”) 
            keepGoing = False (changing sentry) 
    if correct == False: 
        print(“That’s not a number.”)
```