#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random

def intro ():
    print ("Hello User! you're in luck! We're gonna play a guessing game! ")
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, welcome again to this program! I'm thinking of a number from 0-100. Can you guess it? """. format(name))


def info ():
    guess= random.randint (0,100)
    check= True
    while check:
        answer = int(input ("your guess: "))
        if answer == guess:
            print ("\nWinner Winner! Chicken Dinner\n")
            break
        if  answer > guess:
            print ("greater than")
            continue
        if answer < guess:
            print ("less than")
            continue

intro()
info ()

again = str(input("Do you want to play again (type y/n): ")).lower()
if again == "y":
    intro ()
else:
    exit ()