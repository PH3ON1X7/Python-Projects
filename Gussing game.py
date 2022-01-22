#Program to guess the Random Number generated by the compiler.
#Performed by Ojaswin Khamkar

import random

def guess(x):
    random_number = random.randint(1, x)
    print("___You have 3 chances to guess the correct number___")
    chance = 0
    guess = 0
    
    while chance <= 2:
        chance += 1
        guess = int(input(f"Enter a number between 1 and {x}: "))
        
        if guess < random_number:
            print("The number you guessed is LESSER than the Random Number")
            
        elif guess > random_number:
            print("The number you guessed is GREATER than the Random Number")
            
        else:
            print(f"\nHurray!! You have guessed the correct number in {chance} tries.")
            break
    
    else:
        print(f"\nGAME OVER! Correct number was {random_number}")
        
guess(10)