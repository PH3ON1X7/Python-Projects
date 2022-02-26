# Slot Machine by Ojaswin Khamkar

import random

print(
    """********** CASINO ROYALE ***********
      
-------WELCOME TO THE SLOT MACHINE---------

You will be starting with $100 as your balance. You can keep spining the wheel until YOUR BALANCE IS $0
or IF YOU WISH TO CASH OUT. Each spin will cost you $1.

COMBINATIONS TO WIN:- 

JOKER \t JOKER \t JOKER          | $5000 (Jackpot)
BELL  \t BELL  \t BELL JOKER     | $25
PLUM  \t PLUM  \t PLUM\ JOKER    | $15
ORANGE\t ORANGE\t ORANGE\ JOKER  | $10
CHERRY\t CHERRY\t CHERRY         | $6
CHERRY\t CHERRY\t -              | $2
CHERRY\t -     \t -              | $1

ANY OTHER COMBINATION: -$3"""
)

balance = 100  # initial balance of the player
win = 0
wheel_1 = ""
wheel_2 = ""
wheel_3 = ""

items = ["JOKER", "BELL", "PLUM", "ORANGE", "CHERRY", "LEMON"]


def ask_player():
    global balance, win
    while True:
        answer = input(
            f"You have ${balance} remaining, would you like to continue? (y/n): "
        )
        answer = answer.lower()
        if answer == "y":
            return True
        elif answer == "n":
            print(
                f""""\n\t\t\t------GAME OVER------
                
                BALANCE: {balance}
                See you Soon!!"""
            )
            return False
        else:
            print("Invalid Input, please enter 'y or n'.")


def spin_wheel():
    # Returns a random item from the list
    x = random.randint(0, 5)
    return items[x]


def play():
    global wheel_1, wheel_2, wheel_3, balance
    balance -= 1
    cont = ask_player()
    while balance > 0 and cont == True:
        wheel_1 = spin_wheel()
        wheel_2 = spin_wheel()
        wheel_3 = spin_wheel()
        show_result()
        cont = ask_player()
    else:
        print("\n****YOU HAVE LOST ALL YOUR BALANCE****")


def show_result():
    global wheel_1, wheel_2, wheel_3, balance, win

    if (wheel_1 == "JOKER") and (wheel_2 == "JOKER") and (wheel_3 == "JOKER"):
        print("\n******YOU HIT A JACKPOT!!")
        win = 5000
    elif (
        (wheel_1 == "BELL")
        and (wheel_2 == "BELL")
        and (wheel_3 == "JOKER" or wheel_3 == "BELL")
    ):
        win = 25
    elif (
        (wheel_1 == "PLUM")
        and (wheel_2 == "PLUM")
        and (wheel_3 == "JOKER" or wheel_3 == "PLUM")
    ):
        win = 15
    elif (
        (wheel_1 == "ORANGE")
        and (wheel_2 == "ORANGE")
        and (wheel_3 == "JOKER" or wheel_3 == "ORANGE")
    ):
        win = 10
    elif (wheel_1 == "CHERRY") and (wheel_2 == "CHERRY") and (wheel_3 == "CHERRY"):
        win = 6
    elif (wheel_1 == "CHERRY") and (wheel_2 == "CHERRY") and (wheel_3 != "CHERRY"):
        win = 2
    elif (wheel_1 == "CHERRY") and (wheel_2 != "CHERRY") and (wheel_3 != "CHERRY"):
        win = 1
    else:
        win = -3
    balance += win

    if win > 0:
        print(wheel_1 + "\t" + wheel_2 + "\t" + wheel_3 + f" You WIN ${win}")
    else:
        print(wheel_1 + "\t" + wheel_2 + "\t" + wheel_3 + " You LOSE $3")


play()
