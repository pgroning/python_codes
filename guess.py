# This is a simple guess the number game.

from pdb import set_trace # used for debugging
import random

allowedGuesses = 3

guessesTaken = 0

print('Hello! What is your name?')
myName = raw_input()

number = random.randint(1, 20)

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < allowedGuesses:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
