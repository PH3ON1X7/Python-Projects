#Rock Paper Scissors performed by Ojaswin Khamkar

import random

def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
        
uwin = 0
cwin = 0
while True:
    user = input("Press 'r' for Rock, 'p' for Paper, and 's' for Scissors: ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        print('ROUND TIED')
    elif winner(user, computer):
        uwin += 1
        print("YOU WON THIS ROUND")
    elif winner(computer, user):
        cwin += 1
        print("YOU LOST THIS ROUND")
    
    elif user == 'stop':
        print("Final Score: ")
        print(f"Computer Score = {cwin}")
        print(f"Your Score = {uwin}")
        break
    

        
