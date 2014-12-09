#Jeeson Baktha
#Iteration Spot Check Q2
#12 November 2014

import random

guessed = False
number =  random.randrange(1,100)
noOfTurns = 0
userguess = 0
while guessed != True:
    noOfTurns = noOfTurns + 1
    userguess = int(input("Enter your guess for the number: "))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")
print("You took {0} turns to guess the number ".format(noOfTurns))
print("The number was: {0}".format(number))
