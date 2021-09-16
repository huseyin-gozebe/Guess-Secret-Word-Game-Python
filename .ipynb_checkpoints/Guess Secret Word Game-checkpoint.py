 # -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:38:04 2020

@author: Sony
"""
#Guess Secret Word Game by HUSEYIN GOZEBE

starting = input("Type / Help / for Rules, / Quit / to Quit, or Press / any key / to Continue :  ")
starting = starting.upper()

if starting == "QUIT":
    quit()

elif starting == "HELP":    
    print(
          "**************************************************************************************************",
          " Rules of the Game: ",
          " 1. First Player types a Secret Word that is a Single Word",
          "    Then, Second Player Guesses the Secret Word",
          " 2. Only Letters must be Used",
          " 3. Your Guess Limit is 9",
          " 4. Scoring; ",
          "    If You Know a Letter in the Same Rank You Get + 1",
          "    If You Know a Letter in the Different Rank You Get - 1",
          "    For Instance;",
          "    First Example; Secret Word is WHERE and Your Guess is HORSE",
          "    Second Example; Secret Word is PANDA and Your Guess is SNAKE",
          "    Third Example; Secret Word is PLAIN and Your Guess is HIPPO",
          "                 W   H   E   R   E          P   A   N   D   A          P   L   A   I   N ",
          "                 H   O   R   S   E          S   N   A   K   E          H   I   P   P   O ",
          "                -1      -1      +1             -1  -2                     -1  -1  -1     ",
          "    Current Score:    -2   + 1                     -3                         -3         ",
          "    First Example; the H and R Letters in Different Ranks, but the E Letter in the Same Rank",
          "    Second Example; the N and A Letters (2 times in Secret Word) in Different Ranks",
          "    Third Example; the P Letter (2 times in Your Guess) and the I Letter in Different Ranks",   
          "**************************************************************************************************",
          sep = "\n", end = "\n"
          )
    
number_of_guesses = 0
guess_limit = 9
alphabet = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M",
            "N","O","Ö","P","Q","R","S","Ş","T","U","Ü","V","Y","W","X","Z"]

while True:
    
    #secret_word = input("Input Your Secret Word : ") 
    #print(1000 * "   ", "\n")    
    file = open("Secret Words.txt", "r")
    secret_word = file.read()
    file.close()
    secret_word_upper = secret_word.upper()    
              
    for letter in secret_word_upper:
        if letter not in alphabet:
            print("Your Guess must Include only Letters", "\n")
            break
    else:
        break                
            
number_of_letters = len(secret_word)
print(number_of_letters * "  *  ", "\n")
print("Secret Word Consists of", number_of_letters, "Letters"
      , "\n")                                          
            
while number_of_guesses < guess_limit:
    
    while True:        
        
        while True:
            
            guess = input("Guess Secret Word: ")
            lenght_of_guess = len(guess)
            guess_upper = guess.upper()            

            for letter in guess_upper: 
                if letter not in alphabet:
                    print("Your Guess must Include only Letters", "\n")
                    break       
            else:
                break
    
        if lenght_of_guess != number_of_letters:
            print("Your Guess must Have the Same Amount of Letters as Secret Word", "\n")
          
        else:        
            break
        
    #Lists are used instead of strings for handling index isssues from now on

    number_of_guesses += 1
    unique = []
    guess_upper_list = list(guess_upper)
    new_guess_upper_list = guess_upper_list  
    secret_word_upper_list = list(secret_word_upper) 
    new_secret_word_upper_list = secret_word_upper_list 
        
    if secret_word_upper == guess_upper:
        print ("Congragulations! You Knew the Secret Word in", number_of_guesses, "Trial(s)!")
        break    
    
    else:
        positive_points = 0
        negative_points = 0      
                                           
        for i in range(number_of_letters):
                            
            if guess_upper_list[i] == secret_word_upper_list[i]:

                #print(secret_word_upper_list[i])

                positive_points += 1
                #print(positive_points)

                unique.append(i)
                #print(unique)
            
        for index in unique: #This section is for keeping the same amount of elements in lists             

           new_secret_word_upper_list.pop(index)
           new_secret_word_upper_list.insert(index, "+")
           new_guess_upper_list.pop(index)
           new_guess_upper_list.insert(index, "*")

           #print(new_secret_word_upper_list)
           #print(new_guess_upper_list)
                            
        for i in range(number_of_letters):
            
            for j in range(number_of_letters):
                
                if i != j and new_secret_word_upper_list[i] == new_guess_upper_list[j]:
                    
                    #print(new_secret_word_upper_list[i])
                    negative_points += 1                            
                
    print("Your Current Score is", "+", positive_points, "-", negative_points,  "\n")
        
else:
    print("Sorry, You Finished Your", guess_limit ,"Trials", "\n")
    print("The Secret Word is", "\"", secret_word_upper, "\"")
