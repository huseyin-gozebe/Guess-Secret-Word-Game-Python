# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:24:26 2019

@author: Sony
"""
print("You have three trials! ", "\n")

secret_number = int(input("Input your secret number (0-9): "))
number_of_guesses = 0
guess_limit = 3

while number_of_guesses < guess_limit :
    guess = int(input("Guess the Number: "))
    number_of_guesses +=1
    if secret_number == guess:
        print ("You won in", number_of_guesses, "trial(s)!")
        break       
else:
    print ("Sorry, you completed your 3 trials")
