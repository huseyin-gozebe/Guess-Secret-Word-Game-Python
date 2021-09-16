# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:38:04 2020

@author: Sony
"""
#Guess my Word Game

number_of_guesses = 0
guess_limit = 5
alphabet = ["A","B","C","D","E","F","G","H","I","J","K",
            "L","M","N","O","P","Q","R","S","T","U","Y","W","X","Z"]

while True:
    
    secret_word = str(input("Input your secret word : "))
    print(10 * " ", "\n")
    secret_word_upper = secret_word.upper()    
              
    for letter in secret_word_upper:
        if letter not in alphabet:
            print("Your word should include only letters", "\n")
            break
    else:
        break                
            
number_of_letters = len(secret_word)
print(number_of_letters * "  _  ", "\n")
print("My word consists of", number_of_letters, "letters", "\n")                                          
            
while number_of_guesses < guess_limit:
    
    while True:
        
        guess = str(input("Guess my Word: "))
        lenght_of_guess = len(guess)
    
        if lenght_of_guess > number_of_letters:
            print("Your guess should not have more letters than secret word", "\n")
        else:        
            break
                    
    guess_upper = guess.upper()
    number_of_guesses += 1
    
    if secret_word_upper == guess_upper:
        print ("Congragulations! You found my word in", number_of_guesses, "trial(s)!")
        break 
    else:
        number_of_right_letter = 0        
        unique = ""
        
        for item in secret_word_upper:
            if item not in unique:
               unique += item
                              
        unique_upper = unique.upper()
        
        for letter in unique_upper:
            if letter in guess_upper:
                number_of_right_letter += 1
        print("You have found", number_of_right_letter, "letter(s)", "\n")                       
else:
    print("Sorry, you completed your", guess_limit ,"trial(s)", "\n")
    print("Secret word was", "\"", secret_word_upper, "\"")    
