# Dungeons and Dragons by Ojaswin Khamkar

import random

monsterlist = ['Bruxa', "Striga", "Dragon", "Evil Elf", "Leshy",
               "Kikimora", "Archgriffin", 'Grgoyle']

weapons = ['Silver Sword', 'Iron Sword', 'Axe', 'Magic Spells']


print('\t\t-----SETTING THE SCENE-----')
print("\n\nYou are walking through a village, it's dark outside, it getting cold with every passing movement." +
      "\nAll of sudden you hear someone shouting horridly --- 'Aaaaaaa help...help me !!', and then there was silence." +
      ' You begin to wonder that, "What might have happened? What is wrong with this place?"')

#Creating a fight scene
def fight():
    monHealth = 100
    youHealth = 100
    result = False
    
    print('\n\nThe fight is about to begin, You now have to CHOOSE A WEAPON from your arsenal. Remember to choose wisely: ' + str(weapons))
    weaponChoice = input("What weapon do you want to use? ").lower()

    if weaponChoice == 'silver sword':
        weaponDmg = random.randint(1, 30)

    elif weaponChoice == 'iron sword':
        weaponDmg = random.randint(1, 10)

    elif weaponChoice == 'axe':
        weaponDmg = random.randint(1, 20)

    elif weaponChoice == 'magic spells':
        weaponDmg = random.randint(1, 50)

    else:
        weaponChoice = 'Bare Hands'
        weaponDmg = random.randint(0, 5)
    monsterDmg = random.randint(5, 40)

    for i in range(0, 3):
        monHealth -= weaponDmg
        youHealth -= monsterDmg

    if youHealth >= monHealth:
        result = True
        print('\n\nAfter a long fight the monster seems to have lost all his strength, now all you need is one good attack and the monster is done for.'+
              " Gathering all your remaining strength you make a move and with one final strike......." + 
              " ...YOU SLAY THE MONSTER!!")
        return result
        
    return result   


play_again = 'y'
while (play_again == 'y'):
    monster = random.choice(monsterlist)
    print("\n\nThen all of a sudden a " + monster + ' jumps in front of you..."RAWRRRRRRR !!' +
          "\n\nNOW YOU HAVE CHOICE....")

    answer = input("WHAT DO YOU WANT TO DO? - Fight, Run:  ").lower()
    
    #When the player wants to fight
    if answer == 'fight':
        
        if fight() == True:
            print("\nYou have saved everyone from the evil monster.")
            print('\n\n-------CONGRATULATIONS, YOU WON-------')
            break
            
        else:
            print("\n\nA long fight takes place, both you and the monster have taken serious damage."+ 
                  'But in the end the monster turns to strong for you. The monster overpowers you and then EATS YOU')
            print("\n\n-------GAME OVER, YOU ARE DEAD!-------") 
            break
    
    #When the player wants to run
    elif answer == 'run':
        runn = ['CATCHES UPTO YOU', 'KILLS YOU']
        ch = random.choice(runn)

        if ch == 'CATCHES UPTO YOU':
            print('\n\nYou run from the scene, you run as fast as you can. But you soon realize that the monster is two fast' +
                  ' for you. And then the monster ' + 'CATCHES UPTO YOU' + '. As things stand you have no chance but TO FIGHT FOR YOUR LIFE!!')
            
            if fight() == True:
                print("\nYou have saved everyone from the evil monster.")
                print('\n\n-------CONGRATULATIONS, YOU WON-------')
                break
            else:
                print("\n\nA long fight takes place, both you and the monster have taken serious damage."+ 
                      'But in the end the monster turns to strong for you. The monster overpowers you and then EATS YOU')
                print("\n\n-------GAME OVER, YOU ARE DEAD!-------") 
                break
            
        if ch == 'KILLS YOU':
            print("\n\nYou begin to run as fast as your body permits, afterall you are running for your LIFE!" +
                  " You soon realize that running away from the monster was a mistake which only made it more angry." +
                  ' The moster catches upto you and knocks you down!')
            print('\nBefore you can do anything to save your life, the monster TEARS YOU APPART thus KILLING YOU!' +
                  "\n\n-------GAME OVER, YOU ARE DEAD!-------")

    play_again = input("\n\nDo you want to play again? - (y, n)")

    else:
        print("Please enter a valid choice")
